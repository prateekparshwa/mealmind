# Product Brief — MealMind

## Problem

Busy urban professionals in India's tier-1 cities lose 6–10 minutes per ordering session scrolling Swiggy, frequently closing the app without ordering. The bottleneck isn't restaurant supply or delivery speed — it's that food decisions collide with calendar chaos. Back-to-back meetings mean skipped lunches. Client dinners get booked at the wrong place, last-minute. Travel weeks end with spoiled groceries. Decision fatigue at 9:30 PM produces the same biryani, ordered again.

## Product

MealMind is a proactive agent that reads the user's calendar and autonomously orchestrates Swiggy Food, Instamart, and Dineout around their day — ordering breakfast before standups, booking Dineout for client dinners, pausing Instamart during travel weeks. Each morning it sends a WhatsApp digest with one-tap approvals. The user stops opening the app to decide.

## User Outcome

Reclaim ~30 minutes per day. Eliminate 9:30 PM decision fatigue. Kill the food waste that comes from calendar–grocery misalignment during travel. Turn Swiggy from an app you open into an agent that serves you.

## Why This Matters to Swiggy

Swiggy owns all three verticals that busy users juggle — Food, Instamart, Dineout — but they currently operate as separate apps in the user's mind. An agent layer unifies them into a single workflow, which produces three effects:

1. **Converts lost sessions into orders.** Every *open app → scroll → close* session is a revenue leak. The agent eliminates the failure mode by deciding in advance.
2. **Drives cross-vertical behavior.** Users transacting across 2+ verticals have materially higher LTV than single-vertical users. The agent naturally orchestrates across all three.
3. **Creates a retention moat.** A trained agent accumulates preference data over weeks. Churning means losing the assistant — switching cost rises with usage.

## Monetization Path

Positioned as a premium upgrade to Swiggy's existing subscription — the tier this agent naturally slots into. The target segment, busy professionals already spending ₹8–30k/month on Swiggy, has high willingness to pay for autonomy, because their constraint is time, not rupees.

**Indicative pricing for a pilot:** ~₹499/month, tiered above Swiggy One. This funds dual-model inference (~₹12/user/day at current rates) while capturing incremental willingness-to-pay from the segment that values time most.

**Directional impact model** (to pressure-test in a closed pilot):

| Metric | Baseline (Swiggy One) | With Agent Tier | Delta |
|---|---|---|---|
| Monthly churn | ~6% | ~3% (agent lock-in) | **−3 pp** |
| Orders per user per week | 4 | 7 (cross-vertical orchestration) | **+75%** |
| Cross-vertical rate (% users active on 2+ verticals/week) | ~12% | ~45% | **+33 pp** |
| Basket size | ₹380 | ₹420 | **+10%** |

Even at 5% adoption among current Swiggy One subscribers in year one, reduced churn plus increased cross-vertical activity compound materially faster than the incremental subscription revenue alone.

## Acquisition Funnel

All three entry points live inside Swiggy's existing stack — no new acquisition spend required.

1. **Renewal upsell.** Offered to Swiggy One users approaching month-3 renewal. *"Try the agent free for 14 days — let it plan your week."*
2. **Calendar-integration prompt.** Users who grant calendar access enter an upgrade flow.
3. **Reactivation.** Users who haven't ordered in 14+ days get a WhatsApp invite to a 7-day agent trial.

## Competitive Moat

No other Indian commerce platform — Zomato, Zepto, Blinkit, BigBasket — has a proactive, calendar-aware agent today. First-mover advantage establishes three defensible layers:

- **Data moat.** Each week of agent usage generates proprietary training data on food-vs-calendar decisions that competitors cannot replicate without a matching install base.
- **Habit moat.** Once the morning food digest is a daily ritual, a competitor must match both agent quality *and* the subscription tier benefits to dislodge it — a 2-year catch-up minimum.
- **Narrative moat.** Swiggy becomes the commerce company building the agent future — a positioning useful well beyond food.

## Proposed Pilot Design

A 4-week closed pilot with ~500 Swiggy subscribers upgraded to a free preview. Target metrics:

| Metric | Target |
|---|---|
| Agent-led orders per user per week | ≥ 5 |
| Cross-vertical order rate (% of users ordering on 2+ verticals/week) | ≥ 40% |
| % of pilot users opting to pay at trial end | ≥ 30% |
| Agent-initiated order cancellation rate (guardrail) | ≤ 8% |
| NPS delta vs matched control group of Swiggy One subscribers | positive |

## Risks & Mitigations

| Risk | Mitigation |
|---|---|
| Users resist proactive ordering | Progressive autonomy — agent starts as *suggest-only* and earns auto-execute rights as the user's override rate drops. |
| Cannibalizes high-margin discovery orders | Agent never removes user-initiated ordering; it only adds calendar-aligned orders on top. |
| Calendar OAuth friction kills the funnel | WhatsApp-first onboarding; defer OAuth until after first value demonstration. |
| Model costs erode subscription margin | Dual-model split — Haiku 4.5 for cheap event classification, Sonnet 4.6 only for high-stakes planning — keeps inference ~₹12/user/day. |

## Roadmap

- **v1 (current prototype):** Single-user, Food + Instamart + Dineout orchestration, WhatsApp morning digest with one-tap approvals.
- **v2:** Household mode — merge partner / family calendars for shared food planning.
- **v3:** Enterprise tier — executive assistant for founders and CXOs, sold to companies as a perk.
- **v4:** Native integration inside the Swiggy app if productized.
