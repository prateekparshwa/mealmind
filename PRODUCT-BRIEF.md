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

### Public baselines (from Swiggy's FY24-25 Annual Report and Q3 FY26 shareholder letter)

| Metric | Value | Source |
|---|---|---|
| B2C orders (FY24-25) | 923M | [Annual Report FY24-25, p18](https://www.swiggy.com/corporate/wp-content/uploads/2025/07/Swiggy-Annual-Report-FY-2024-25.pdf) |
| Average Monthly Transacting Users (FY24-25) | 17.7M | Annual Report, p18 |
| Platform order frequency (FY24-25) | 4.43 orders/user/month | Annual Report, p18 |
| **Platform MTU (Q3 FY26)** | **24.3M (+37% YoY)** | [Q3 FY26 Shareholder Letter, p5](https://www.swiggy.com/corporate/wp-content/uploads/2026/01/Q3-FY2026-Shareholder-letter.pdf) |
| **Platform frequency (Q3 FY26)** | **4.04 orders/user/month — DOWN from 4.46 a year earlier** | Q3 FY26 letter, p5 |
| Food delivery AOV (FY24-25) | ₹458 (up from ₹407 in FY22) | Annual Report, p28 |
| Food delivery MTU (Q3 FY26) | 18.1M | Q3 FY26 letter, p6 |
| Instamart AOV (Q3 FY26) | ₹746 (up from ₹487 in Q1 FY25) | Q3 FY26 letter, p7 |
| Instamart MTU (Q3 FY26) | 12.8M (up from 5.2M in Q1 FY25) | Q3 FY26 letter, p7 + [Q2 FY25 letter, p7](https://www.swiggy.com/corporate/wp-content/uploads/2024/12/Letter-to-Shareholders_Q2FY25.pdf) |
| Cross-vertical engagement | *"Over 30% of our users engage with more than one service on the platform"* | Annual Report, p32 (Instamart section) |
| New-user cross-pollination | *"~29% of new Instamart users were new to Swiggy overall"* — meaning 71% came from the existing Food/Dineout base | Annual Report, p20 (CEO message) |
| Swiggy One members (2025) | *"Swiggy One membership base crossed 5.7 million members"* | Annual Report, p8 |

### The key insight

Two disclosed facts together form the thesis:

1. **Frequency is the binding constraint, not acquisition.** Platform MTU grew 37% YoY, but orders-per-user-per-month *declined* from 4.46 to 4.04 (Q3 FY26 letter). Swiggy is adding users faster than it is getting them to order.

2. **Cross-pollination is Swiggy's stated growth lever.** The CEO message explicitly credits cross-pollination from Instamart for the Food Delivery MTU acceleration. 30%+ of users are already multi-service. The compounding is there — but it's passive.

An agent that reads a user's calendar and pre-plans orders across Food, Instamart, and Dineout attacks both constraints simultaneously — it raises frequency *and* actively orchestrates cross-vertical behaviour instead of waiting for it to happen organically.

### Agent-tier hypothesis — to validate in pilot

Swiggy does not publicly disclose Swiggy One–specific churn or segment-level retention; those require internal data. The pilot below is designed to measure the deltas an agent tier could produce against Swiggy's own baselines:

- **Orders per user per month** among agent-tier subscribers — hypothesis: reverse the frequency decline; lift to ≥6 (vs 4.04 Q3 FY26 platform average)
- **Multi-service engagement rate** — hypothesis: lift the disclosed 30%+ baseline to ≥60% *weekly* cross-vertical activity (not just any-time overlap)
- **Subscription churn** via agent lock-in — hypothesis: ≥30% relative reduction vs matched Swiggy One control
- **Basket size uplift** — hypothesis: ~10% increase, especially on Instamart (already trending up at 40% YoY from ₹534 → ₹746 AOV)

All four are bets. The pilot's purpose is to replace them with Swiggy's numbers.

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
