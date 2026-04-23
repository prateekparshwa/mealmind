"""
Calendar-Aware Meal Agent — Intent Router Prototype.

Idea 1 from the Swiggy Builders Club plan:
  classify events (Haiku) -> plan meals (Sonnet) -> gate with confidence threshold.
"""
from __future__ import annotations

import json
import os
import sys
from dataclasses import dataclass
from pathlib import Path

from anthropic import Anthropic
from dotenv import load_dotenv

HAIKU = "claude-haiku-4-5-20251001"
SONNET = "claude-sonnet-4-6"

EVENT_CATEGORIES = [
    "meeting_light",
    "meeting_heavy",
    "client_dinner",
    "travel",
    "workout",
    "free_evening",
    "other",
]

CLASSIFIER_SYSTEM = f"""You classify calendar events for a food-ordering agent.

Output one JSON object per event with:
  - category: one of {EVENT_CATEGORIES}
  - confidence: float 0-1 (how sure you are)
  - reasoning: one short sentence

Category rules:
  - meeting_light: <=1h meeting, no hosting, <=3 attendees
  - meeting_heavy: >1h OR >=4 attendees OR high-stakes (board, all-hands, client review)
  - client_dinner: evening event with external attendees OR explicit "dinner"/"lunch with client"
  - travel: flights, long commutes, airport-related
  - workout: gym, yoga, run, cycling, sport
  - free_evening: unscheduled evening block (7pm-10pm) OR title like "free", "nothing", "open"
  - other: anything not clearly above

Return ONLY a JSON array. No prose, no markdown."""

PLANNER_SYSTEM = """You are a meal-planning agent for a busy urban professional in a tier-1 Indian city.

For each classified event, decide ONE action:
  - order_food     : schedule a Swiggy Food delivery timed around this event
  - book_dineout   : book a Dineout restaurant reservation
  - suggest_instamart : pre-schedule grocery delivery (for travel return, weekend, etc.)
  - skip           : no food action needed

Rules:
  - meeting_heavy overlapping lunch (12-2pm) -> order_food to arrive just before
  - client_dinner -> book_dineout near event location, match attendee count
  - travel departing morning -> suggest_instamart for return day
  - workout -> order_food (protein meal) to arrive within 60 min post-workout
  - free_evening -> skip (let user decide) unless historical pattern suggests otherwise
  - meeting_light -> skip unless adjacent to a meal slot with no other plan

Output JSON array, one object per event:
  - action: one of [order_food, book_dineout, suggest_instamart, skip]
  - reason: one short sentence
  - confidence: float 0-1
  - timing_hint: string like "11:45 delivery" or "8pm reservation" or null

Return ONLY a JSON array. No prose."""


@dataclass
class ClassifiedEvent:
    event: dict
    category: str
    confidence: float
    reasoning: str


@dataclass
class PlannedDecision:
    event: dict
    category: str
    action: str
    reason: str
    confidence: float
    timing_hint: str | None


def load_events(path: Path) -> list[dict]:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def classify_events(client: Anthropic, events: list[dict]) -> list[ClassifiedEvent]:
    """Uses Haiku with prompt caching on the large static system prompt."""
    resp = client.messages.create(
        model=HAIKU,
        max_tokens=2048,
        system=[
            {
                "type": "text",
                "text": CLASSIFIER_SYSTEM,
                "cache_control": {"type": "ephemeral"},
            }
        ],
        messages=[
            {
                "role": "user",
                "content": f"Classify these events:\n\n{json.dumps(events, indent=2)}",
            }
        ],
    )
    raw = resp.content[0].text.strip()
    parsed = json.loads(raw)
    if len(parsed) != len(events):
        raise ValueError(f"Classifier returned {len(parsed)} results for {len(events)} events")
    return [
        ClassifiedEvent(
            event=event,
            category=item["category"],
            confidence=float(item["confidence"]),
            reasoning=item["reasoning"],
        )
        for event, item in zip(events, parsed)
    ]


def plan_meals(client: Anthropic, classified: list[ClassifiedEvent]) -> list[PlannedDecision]:
    """Uses Sonnet with prompt caching on the planner system prompt."""
    payload = [
        {
            "title": c.event["title"],
            "start": c.event["start"],
            "end": c.event["end"],
            "attendees_count": len(c.event.get("attendees", [])),
            "location": c.event.get("location", ""),
            "category": c.category,
        }
        for c in classified
    ]
    resp = client.messages.create(
        model=SONNET,
        max_tokens=2048,
        system=[
            {
                "type": "text",
                "text": PLANNER_SYSTEM,
                "cache_control": {"type": "ephemeral"},
            }
        ],
        messages=[
            {
                "role": "user",
                "content": f"Plan meals for these classified events:\n\n{json.dumps(payload, indent=2)}",
            }
        ],
    )
    raw = resp.content[0].text.strip()
    parsed = json.loads(raw)
    if len(parsed) != len(classified):
        raise ValueError("Planner returned wrong number of decisions")
    return [
        PlannedDecision(
            event=c.event,
            category=c.category,
            action=item["action"],
            reason=item["reason"],
            confidence=float(item["confidence"]),
            timing_hint=item.get("timing_hint"),
        )
        for c, item in zip(classified, parsed)
    ]


def apply_autonomy_gate(decisions: list[PlannedDecision], threshold: float) -> None:
    """Progressive autonomy: above threshold auto-execute, below -> ask user.

    Real implementation would fire MCP calls here. For the prototype we print.
    """
    print("\n" + "=" * 72)
    print(f"AUTONOMY GATE  (confidence threshold = {threshold:.2f})")
    print("=" * 72)
    auto, ask, skipped = 0, 0, 0
    for d in decisions:
        marker = "AUTO " if d.confidence >= threshold and d.action != "skip" else (
            "SKIP " if d.action == "skip" else "ASK  "
        )
        if marker == "AUTO ":
            auto += 1
        elif marker == "ASK  ":
            ask += 1
        else:
            skipped += 1
        title = d.event["title"][:40]
        timing = f" [{d.timing_hint}]" if d.timing_hint else ""
        print(f"  {marker} {d.action:18s} conf={d.confidence:.2f}  {title:42s}{timing}")
        print(f"        -> {d.reason}")
    print("-" * 72)
    print(f"  auto-executed: {auto}   ask-user: {ask}   skipped: {skipped}")


def main() -> int:
    load_dotenv()
    if not os.getenv("ANTHROPIC_API_KEY"):
        print("ERROR: set ANTHROPIC_API_KEY in .env (see .env.example)", file=sys.stderr)
        return 1

    here = Path(__file__).parent
    events = load_events(here / "sample_events.json")
    print(f"Loaded {len(events)} calendar events.\n")

    client = Anthropic()

    print("=" * 72)
    print("STEP 1 — CLASSIFYING EVENTS (Haiku 4.5)")
    print("=" * 72)
    classified = classify_events(client, events)
    for c in classified:
        print(f"  {c.category:16s} conf={c.confidence:.2f}  {c.event['title'][:40]}")
        print(f"        -> {c.reasoning}")

    print("\n" + "=" * 72)
    print("STEP 2 — PLANNING MEALS (Sonnet 4.6)")
    print("=" * 72)
    decisions = plan_meals(client, classified)
    for d in decisions:
        print(f"  {d.action:18s} conf={d.confidence:.2f}  {d.event['title'][:40]}")
        print(f"        -> {d.reason}")

    autonomy_threshold = 0.70
    apply_autonomy_gate(decisions, threshold=autonomy_threshold)

    print("\nDone. Next step: replace 'apply_autonomy_gate' with real Swiggy MCP calls.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
