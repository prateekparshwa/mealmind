# MealMind — Calendar-Aware Meal Agent for Swiggy

> Swiggy loses money every time a user opens the app, scrolls for 8 minutes, and closes without ordering. MealMind eliminates that failure mode by deciding *for* the user, in advance — orchestrating Food, Instamart, and Dineout around the user's calendar.

**Submitted for [Swiggy Builders Kitchen](https://mcp.swiggy.com/builders/#about), April 2026.**

**What this repo contains:**
- `agent.py` — working prototype of the dual-model intent router (Haiku 4.5 classifier + Sonnet 4.6 planner) with a progressive-autonomy confidence gate.
- `SWIGGY-ONE-PRO-NARRATIVE.md` — business case for a ₹499/month Swiggy One Pro tier that bundles this agent, with retention math and cross-MCP revenue hypothesis.
- `IDEATION.md` — multi-perspective PM/Designer/Engineer ideation that led to the shortlist.

**Author:** Prateek Parshwa ([LinkedIn](https://www.linkedin.com/in/prateekparshwa)) — Product Manager, built with Claude Code.

---

## The Prototype

A runnable demo of the dual-model intent router with progressive autonomy.

## What This Does

Given a day's calendar events, the agent:

1. **Classifies** each event with **Haiku 4.5** (fast + cheap): is this a meeting, client dinner, travel block, workout, free evening?
2. **Plans** food decisions for the day with **Sonnet 4.6** (smart + deliberate): for each classified event, should we order food? Book a Dineout? Skip?
3. **Gates** each decision through a confidence threshold: above the threshold → auto-execute; below → ask the user.

It runs end-to-end against a sample calendar so you can see the full flow without any external integration.

## Why The Architecture Matters

- **Dual-model split** keeps cost ~10× lower than using Sonnet everywhere while preserving plan quality where it counts.
- **Progressive autonomy** (the confidence threshold) is the trust wedge — the agent earns the right to auto-execute as it proves itself.
- **Prompt caching** is enabled on both the classifier and planner system prompts — this matters for Swiggy's cost story (see the One Pro narrative doc).

## Setup (for a non-coder, ~5 minutes)

1. **Install Python 3.11+** if you don't have it. Check with `python --version` in terminal. Download from python.org if missing.

2. **Get an Anthropic API key:** https://console.anthropic.com → Settings → API Keys → Create Key. Copy it.

3. **In this folder, run:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file** in this folder by copying `.env.example`:
   ```bash
   copy .env.example .env
   ```
   Then open `.env` in a text editor and paste your API key after `ANTHROPIC_API_KEY=`.

5. **Run the agent:**
   ```bash
   python agent.py
   ```

You'll see classified events, the day's plan, and which decisions auto-executed vs. got flagged for human review.

## Files

| File | Purpose |
|---|---|
| `agent.py` | Main orchestration — loads events, runs classifier → planner → autonomy gate |
| `sample_events.json` | 10 realistic calendar events for a typical urban professional |
| `requirements.txt` | Python dependencies |
| `.env.example` | Template for your API key |

## How to Test With Your Own Calendar

Replace `sample_events.json` with your real events in this format:

```json
[
  {
    "title": "Sync with Priya",
    "start": "2026-04-24T10:00:00",
    "end": "2026-04-24T10:30:00",
    "attendees": ["priya@example.com"],
    "location": ""
  }
]
```

Export from Google Calendar: Settings → Import & Export → Export. Convert .ics to JSON with any online converter, then swap in this file.

## Next Steps (for the full Builders Club submission)

- [ ] Wire up Google Calendar OAuth for live event fetching (replace `sample_events.json`).
- [ ] Wire up actual Swiggy MCP calls for Food, Instamart, Dineout (currently the plan prints decisions instead of firing orders).
- [ ] Add the WhatsApp morning digest (Twilio) — Idea #2 from the ideation doc.
- [ ] Add the override-tracking logic so the autonomy threshold raises as the user stops rejecting plans — the *progressive* part of progressive autonomy.

Use `superpowers:writing-plans` in a fresh Claude Code session to plan each step properly before building.
