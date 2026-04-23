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

### Public baselines (Swiggy disclosures)

| Metric | Value | Source |
|---|---|---|
| Annual transacting users | 46.8M (FY24), up from 35.1M (FY22) | [Annual Report FY24–25](https://www.swiggy.com/corporate/wp-content/uploads/2025/07/Swiggy-Annual-Report-FY-2024-25.pdf) |
| Food delivery orders | 577M (FY24) — implies ~12 orders/user/year on the blended base | Annual Report FY24–25 |
| Food delivery AOV | ₹436 (Q1 FY25), up from ₹407 (FY22) | [Q2 FY25 Shareholder Letter](https://www.swiggy.com/corporate/wp-content/uploads/2024/12/Letter-to-Shareholders_Q2FY25.pdf) |
| Instamart AOV | ₹487 → ₹527 → ₹697 → ₹746 across Q1 FY25 → Q3 FY26 | [Q3 FY26 Shareholder Letter](https://www.swiggy.com/corporate/wp-content/uploads/2026/01/Q3-FY2026-Shareholder-letter.pdf) |
| Instamart quarterly active users | 12.8M (Q3 FY26), handling 106.4M orders; up from ~12M in Q2 FY26 | [Q3 FY26 Shareholder Letter](https://www.swiggy.com/corporate/wp-content/uploads/2026/01/Q3-FY2026-Shareholder-letter.pdf) |
| Swiggy One membership | ~5.7M members (2025) | Annual Report FY24–25 |
| Stated strategic aspiration | 110M users × ≥15 orders/month across verticals | Annual Report FY24–25 |

The gap between today's ~46.8M × ~12 orders/year blended baseline and the 110M × 15-orders/month aspiration implies **order frequency**, not user acquisition, is the binding constraint on Swiggy's growth math. An agent that orders on behalf of users attacks that constraint directly.

### Agent-tier hypothesis — to validate in pilot

Swiggy does not publicly disclose Swiggy One–specific churn, cross-vertical overlap, or segment-level retention. Those baselines require internal data. The pilot below is designed to measure the deltas an agent tier could produce against whatever Swiggy's actual internal baselines are:

- **Orders per user per week** among agent-tier subscribers — hypothesis: ≥50% lift vs matched Swiggy One control
- **Cross-vertical activity** (% of users transacting on 2+ of Food/Instamart/Dineout weekly) — hypothesis: ≥30 pp increase
- **Subscription churn** through agent lock-in — hypothesis: ≥30% relative reduction
- **Basket size** — hypothesis: ~10% increase

All four are bets, not data points. The pilot's primary purpose is to replace them with Swiggy's numbers.

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
