# Multi-Perspective Ideation — Calendar-Aware Meal Agent (Swiggy Builders Club)

**Product concept:** A proactive food concierge that reads the user's calendar and autonomously orchestrates Swiggy Food, Instamart, and Dineout around their day.

**Target segment:** Busy urban professionals, 25–40, tier-1 Indian cities (Bangalore, Mumbai, Delhi-NCR, Hyderabad), current Swiggy monthly spend ₹8k–₹30k.

**Primary user outcome:** Stop thinking about food. Agent executes, user approves. Reclaim ~30 mins/day + eliminate decision fatigue + kill food waste from calendar-food misalignment.

**Initial-discovery mode:** We're testing whether this product should exist, not iterating a live product. Ideas below weight toward *what to validate first*.

---

## Perspective 1 — Product Manager (Market Fit, Value, Competitive Advantage)

### PM-1. Swiggy One bundling as the distribution wedge
Position the agent as an **exclusive Swiggy One premium feature**. Doubles as a retention moat for Swiggy's subscription (reduces churn), and an acquisition channel (people upgrade to get the agent). Converts the Builders Club submission into a direct business case for Swiggy's subscription team.

### PM-2. Household / family mode
Let users merge 2–4 calendars (spouse, partner, kids). Agent reconciles: "Both of you have client dinners Thursday → book one shared Dineout instead of two separate orders." Expands TAM from individual to household; 3–4× basket size.

### PM-3. "Meal autonomy score" — a shareable weekly metric
A single number each week: "Your agent saved you 47 minutes and ₹320 vs. your historical baseline." Gamified, screenshot-worthy, drives organic growth via social sharing. Creates a North Star the user feels.

### PM-4. Executive assistant enterprise tier
Sell to companies as a perk for busy execs. Company pays ₹999/month/exec; Swiggy gets guaranteed order volume, the exec gets an EA-grade food concierge. Smaller segment but higher LTV and a clear B2B narrative for Swiggy's enterprise team.

### PM-5. Anti-abandonment analytics flip
Reframe the agent to Swiggy leadership not as "another app" but as a **churn-reduction lever**. Swiggy loses money every time a user opens the app, scrolls 8 minutes, and closes without ordering. The agent eliminates that failure mode. Pitch with a specific metric: "reduce Swiggy app-open-without-order events by X%."

---

## Perspective 2 — Product Designer (UX, Onboarding, Engagement)

### D-1. WhatsApp-first conversational onboarding (no app install)
Entire onboarding happens in WhatsApp. Agent DMs you, asks 5 questions about diet/budget/cuisines, learns. Zero app install, zero App Store friction — critical for tier-1 India where WhatsApp is the default interface. Also makes user-testing trivial: just send a WhatsApp link.

### D-2. One-tap visual morning digest
The 7am digest is NOT a text list. It's 3 cards: breakfast photo + restaurant + arrival time, lunch card, dinner card. Each with a single "Approve" button. Modeled after how users already scan email previews on lock screen.

### D-3. Prominent undo / skip everywhere
Proactive agents feel scary. Every decision the agent makes shows a giant "Skip" or "Undo" button for 60 seconds after it fires. Trust is built in the early weeks by showing the user they're always in control.

### D-4. Calendar overlay integration
Instead of a new surface, inject food intent directly into Google Calendar: tiny food-emoji markers on events ("🍱 12:15 — lunch ordered"). Users see the agent's plan in the tool they already live in.

### D-5. Sunday-night weekly review ritual
Every Sunday 8pm, agent sends a review: what it did, what you overrode, patterns it's learning, suggestions to adjust. Turns the user into a co-pilot; makes the learning loop visible; creates a weekly engagement ritual.

---

## Perspective 3 — Software Engineer (Technical Innovation, APIs, Platform)

### E-1. Dual-model intent router (Sonnet for planning, Haiku for classification)
Use cheap fast Haiku to classify each calendar event ("meeting", "client-dinner", "travel", "workout"). Use Sonnet only for the small number of high-stakes planning decisions. 10× cheaper per user/day while keeping plan quality high.

### E-2. Progressive autonomy via confidence thresholds
Every agent decision has a confidence score. Below 70% → ask user. Above 70% → auto-execute. Threshold starts conservative and raises as the user's historical override rate drops. The agent earns autonomy over weeks, mirroring how humans trust assistants.

### E-3. Event-sourced decision log
Every reasoning step is logged (calendar event → classification → decision → MCP call → outcome). Serves three purposes: (a) user-facing transparency ("why did you order sushi?"), (b) debugging when things go wrong, (c) training data if Swiggy ever productizes.

### E-4. Calendar webhook-driven deltas (not daily polling)
Subscribe to Google Calendar push notifications. Only re-plan when events change. Cuts compute by ~95% vs. daily full scans and makes the agent feel real-time when meetings get rescheduled.

### E-5. Graceful degradation to suggestion mode
If an MCP call fails (rate limit, auth issue, stockout), the agent never hard-fails. It degrades to: "Here's what I would have ordered — tap to do it yourself in the Swiggy app." User experience stays intact; reliability is perceived higher than actual uptime.

---

## Prioritized Top 5 Ideas (ranked for Builders Club submission)

Weighted toward: **core value delivery**, **speed to validate**, **differentiation**.

### 1. Dual-model intent router + progressive autonomy (E-1 + E-2)
**Why this is #1:** This IS the product's intelligence. Without a router that classifies events correctly and an autonomy threshold that earns trust over time, the agent is either annoying (asks too much) or dangerous (auto-orders wrong things). Ship this right and the demo video writes itself. Ship it wrong and nothing else matters.
**Assumption to test:** Can Haiku classify typical calendar events (with titles like "Sync w/ Priya", "PRD review", "Dinner with Rahul at Bandra") with >90% accuracy? *Validation:* label 200 calendar events from 5 beta users, measure classification accuracy.

### 2. WhatsApp-first onboarding (D-1)
**Why #2:** Removes the single biggest adoption barrier in India — app installs. Every beta tester can be recruited with a link. Every Swiggy executive reviewing your submission can use it themselves in 60 seconds. Massively accelerates the validation cycle and makes the product feel India-native.
**Assumption to test:** Will users grant Calendar OAuth through a WhatsApp-initiated flow? *Validation:* run 10 live onboarding tests; measure drop-off at OAuth step. Target >70% completion.

### 3. Prominent undo + Sunday-night review (D-3 + D-5)
**Why #3:** Proactive commerce is a trust problem, not a tech problem. Users will only let an agent *act* for them if they trust (a) they can always undo, and (b) they can see what it did and why. These two interaction patterns are the trust wedge. Skip them and you get one bad auto-order and a churned user.
**Assumption to test:** Does a visible undo button + weekly review measurably reduce "I'm scared of this product" feedback? *Validation:* compare NPS / qualitative trust scores between a cohort with undo+review and one without after 2 weeks.

### 4. Household / family mode (PM-2)
**Why #4:** Validates a 3–4× larger market. Even if MVP is single-user, the brief must show the household roadmap because it's how Swiggy thinks about basket economics. Don't build it in MVP; design for it and mention it in the product brief.
**Assumption to test:** Do couples/flatmates want to merge food decisions, or do they prefer independence? *Validation:* 6 interviews with cohabiting urban pros. Test willingness to share calendars.

### 5. Swiggy One bundling narrative (PM-1)
**Why #5:** This is the business-model hook that turns a cool demo into a Swiggy-shaped pitch. Pure narrative — no build required. But it's what makes your submission feel like a PM who understands Swiggy's P&L, not a developer who built a toy. Include as a 1-page section in the product brief: "If Swiggy productized this, here's the bundle, the pricing, and the retention math."
**Assumption to test:** Would existing Swiggy One subscribers value the agent enough to count it as a retention factor? *Validation:* 10-person survey with current Swiggy One subscribers.

---

## What to explicitly *not* build in MVP (YAGNI)

- Enterprise tier (PM-4) — great v2 story, no bandwidth for MVP.
- Anti-abandonment analytics (PM-5) — belongs in the brief, not the build.
- Meal autonomy score (PM-3) — nice-to-have; ship after week-4 retention is proven.
- Calendar overlay integration (D-4) — technically heavier than email/WhatsApp digest; defer.
- Event-sourced decision log UI (E-3) — keep the *data* log for debugging, defer the user-facing transparency UI.

---

## Next Step

When you're ready to build, invoke **`superpowers:writing-plans`** in a fresh Claude Code session with this doc + the main plan file as inputs. That will turn these 5 prioritized ideas into a concrete week-by-week implementation plan.
