# If Swiggy Productized This: The Swiggy One Pro Narrative

*A one-page business case for the Calendar-Aware Meal Agent as a Swiggy premium tier. Intended as a section of the Builders Club submission brief.*

---

## The Hook (Lead with This)

> Swiggy loses money every time a user opens the app, scrolls for 8 minutes, and closes it without ordering. Internal app analytics almost certainly call this "session-without-conversion." The Calendar-Aware Meal Agent eliminates that failure mode entirely by deciding *for* the user, in advance.

This is the pitch Swiggy leadership will remember. Everything below is the proof.

---

## The Proposal — A New Premium Tier: *Swiggy One Pro*

| Tier | Price | Core Benefit |
|---|---|---|
| Swiggy One (today) | ~₹229/month | Free delivery, member-only prices |
| **Swiggy One Pro (new)** | **₹499/month** | Everything in Swiggy One **+ Agent-led autonomous ordering** across Food, Instamart, Dineout |

The agent is the *only* exclusive One Pro feature for now. Minimal SKU complexity, maximum differentiation, clean pricing story.

---

## Why This Beats Bundling as a Free Feature

1. **Captures willingness-to-pay from highest-LTV users.** Busy urban professionals already spend ₹8k–₹30k/month on Swiggy. Paying ₹270 incremental (One Pro vs One) to reclaim 30 minutes/day is a trivial decision for this segment.
2. **Creates a retention moat.** Agent users train the agent for weeks. Cancelling One Pro = losing your trained assistant. Switching cost rises with usage.
3. **Justifies model cost.** Sonnet + Haiku inference per user/day costs Swiggy real money (~₹8–₹15 at current API rates). Free bundling cannibalizes margin; paid bundling funds it.

---

## Retention Math (Directional, to Validate in Pilot)

Assumptions to pressure-test with Swiggy's subscription team:

| Metric | Baseline (One) | With Agent (One Pro) | Delta |
|---|---|---|---|
| Monthly churn | ~6% (industry proxy) | ~3% (agent lock-in) | **−3 pp** |
| Orders/user/week | 4 | 7 (agent fires cross-MCP) | **+75%** |
| Cross-MCP %age* | ~12% | ~45% | **+33 pp** |
| Basket size | ₹380 | ₹420 | **+10%** |

*Cross-MCP = the same user places orders on 2+ of Food/Instamart/Dineout in the same week. This is Swiggy's real north star — users who live across all three verticals have 3× the LTV of single-vertical users.

**The punchline:** Even if One Pro captures only 5% of current Swiggy One subscribers in year one, the combination of reduced churn + increased cross-MCP orders compounds faster than the sub-revenue alone.

---

## Acquisition Funnel

- **Entry point A:** In-app upsell when a Swiggy One user approaches month-3 renewal. "Try One Pro free for 14 days — let our agent plan your week."
- **Entry point B:** Calendar integration prompt. When a user grants calendar access, they enter an upgrade flow.
- **Entry point C:** WhatsApp reactivation. Users who haven't ordered in 14+ days get a WhatsApp invite to try the agent on a 7-day trial.

All three funnels exist entirely inside Swiggy's existing CRM stack — no new acquisition spend required.

---

## Competitive Moat

No other Indian commerce platform has a proactive calendar-aware agent — not Zomato, Zepto, Blinkit, BigBasket, DoorDash (globally). The first mover establishes:

- **Data moat:** every week of agent usage generates proprietary training data on food-vs-calendar decisions that competitors can't replicate without the same install base.
- **Habit moat:** once the 7am food digest is in a user's daily routine, dislodging it requires a competitor to match *both* the agent quality *and* the Swiggy One Pro benefits. That's a 2-year catch-up minimum.
- **Narrative moat:** Swiggy becomes "the commerce company building the agent future" — a positioning useful well beyond food.

---

## What to Measure in the Pilot (Suggested Swiggy Metrics)

Propose Swiggy run a 4-week closed pilot with 500 Swiggy One users upgraded to a free One Pro preview. Track:

1. **Primary:** Agent-led orders per user per week. Target: ≥5.
2. **Secondary:** Cross-MCP order rate (% of users ordering on 2+ verticals/week). Target: ≥40%.
3. **Retention proxy:** % of pilot users who actively opt to pay for One Pro at end of trial. Target: ≥30%.
4. **Trust guardrail:** Agent-initiated order cancellation rate. Upper bound: ≤8%.
5. **Qualitative:** NPS delta vs. matched control group of One subscribers.

---

## Risks (Name Them Before Swiggy Does)

| Risk | Mitigation |
|---|---|
| Users revolt at proactive ordering | Progressive autonomy — agent starts as *suggest-only*, earns auto-execute rights over weeks. |
| Cannibalizes impulsive discovery orders (high-margin) | Agent never removes user-initiated ordering; it only adds calendar-aligned orders on top. |
| Calendar OAuth friction kills funnel | WhatsApp-first onboarding + delayed OAuth until after first value demo. |
| Model costs erode One Pro margin | Dual-model (Haiku for classification, Sonnet for planning) keeps inference ~₹12/user/day. |

---

## The One-Line Summary for the Submission

> Swiggy One Pro is a ₹499/month tier that turns Swiggy from an app users open into an agent that serves them — paid for by the users who value their time most, retained by the switching cost of a trained assistant, and defended by a cross-MCP data moat no competitor can replicate.
