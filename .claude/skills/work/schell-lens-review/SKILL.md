---
name: schell-lens-review
description: "Structured design review using Schell's 116 lenses — evaluate any framework, product standard, or product. Use this skill when the user wants to run a lens-based design review, generate design improvement backlogs, or evaluate a body of work through design lenses."
---

# Schell Lens Review

**Source:** The Art of Game Design: A Book of Lenses, 3rd Edition — Jesse Schell

**Purpose:** Apply Schell's 116 lenses as a structured design review protocol against any framework, product standard, or product. Produces recommended lens set, collaborative lens walkthrough, and a prioritized backlog of changes.

---

## LENS QUESTIONS REFERENCE

**Before running this skill, load the lens questions from:**
```
.claude/skills/work/schell-lens-review/LENSES.md
```

This file contains the authoritative question set transcribed directly from the book. Do not proceed without reading it first.

---

## WHEN TO USE THIS SKILL

Trigger this skill when the user wants to:
- Evaluate a framework, product standard, or product through design lenses
- Understand what to test for or improve in a body of work
- Run a repeatable design quality review
- Generate a backlog of design improvements

---

## COMPLETE LENS INDEX (3rd Edition, Official)

| # | Lens |
|---|------|
| 1 | The Lens of Emotion |
| 2 | The Lens of Essential Experience |
| 3 | The Lens of the Venue |
| 4 | The Lens of Surprise |
| 5 | The Lens of Fun |
| 6 | The Lens of Curiosity |
| 7 | The Lens of Endogenous Value |
| 8 | The Lens of Problem Solving |
| 9 | The Lens of the Elemental Tetrad |
| 10 | The Lens of Holographic Design |
| 11 | The Lens of Unification |
| 12 | The Lens of Resonance |
| 13 | The Lens of Infinite Inspiration |
| 14 | The Lens of the Problem Statement |
| 15 | The Lens of the Eight Filters |
| 16 | The Lens of Risk Mitigation |
| 17 | The Lens of the Toy |
| 18 | The Lens of Passion |
| 19 | The Lens of the Player |
| 20 | The Lens of Pleasure |
| 21 | The Lens of Flow |
| 22 | The Lens of Needs |
| 23 | The Lens of Motivation |
| 24 | The Lens of Novelty |
| 25 | The Lens of Judgment |
| 26 | The Lens of Functional Space |
| 27 | The Lens of Time |
| 28 | The Lens of the State Machine |
| 29 | The Lens of Secrets |
| 30 | The Lens of Emergence |
| 31 | The Lens of Action |
| 32 | The Lens of Goals |
| 33 | The Lens of Rules |
| 34 | The Lens of Skill |
| 35 | The Lens of Expected Value |
| 36 | The Lens of Chance |
| 37 | The Lens of Fairness |
| 38 | The Lens of Challenge |
| 39 | The Lens of Meaningful Choices |
| 40 | The Lens of Triangularity |
| 41 | The Lens of Skill vs. Chance |
| 42 | The Lens of Head and Hands |
| 43 | The Lens of Competition |
| 44 | The Lens of Cooperation |
| 45 | The Lens of Competition vs. Cooperation |
| 46 | The Lens of Reward |
| 47 | The Lens of Punishment |
| 48 | The Lens of Simplicity/Complexity |
| 49 | The Lens of Elegance |
| 50 | The Lens of Character |
| 51 | The Lens of Imagination |
| 52 | The Lens of Economy |
| 53 | The Lens of Balance |
| 54 | The Lens of Accessibility |
| 55 | The Lens of Visible Progress |
| 56 | The Lens of Parallelism |
| 57 | The Lens of the Pyramid |
| 58 | The Lens of the Puzzle |
| 59 | The Lens of Control |
| 60 | The Lens of Physical Interface |
| 61 | The Lens of Virtual Interface |
| 62 | The Lens of Transparency |
| 63 | The Lens of Feedback |
| 64 | The Lens of Juiciness |
| 65 | The Lens of Primality |
| 66 | The Lens of Channels and Dimensions |
| 67 | The Lens of Modes |
| 67½ | The Lens of Metaphor |
| 68 | The Lens of Moments |
| 69 | The Lens of the Interest Curve |
| 70 | The Lens of Inherent Interest |
| 71 | The Lens of Beauty |
| 72 | The Lens of Projection |
| 73 | The Lens of the Story Machine |
| 74 | The Lens of the Obstacle |
| 75 | The Lens of Simplicity and Transcendence |
| 76 | The Lens of the Hero's Journey |
| 77 | The Lens of the Weirdest Thing |
| 78 | The Lens of Story |
| 79 | The Lens of Freedom |
| 80 | The Lens of Help |
| 81 | The Lens of Indirect Control |
| 82 | The Lens of Collusion |
| 83 | The Lens of Fantasy |
| 84 | The Lens of the World |
| 85 | The Lens of the Avatar |
| 86 | The Lens of Character Function |
| 87 | The Lens of Character Traits |
| 88 | The Lens of the Interpersonal Circumplex |
| 89 | The Lens of the Character Web |
| 90 | The Lens of Status |
| 91 | The Lens of Character Transformation |
| 92 | The Lens of Inner Contradiction |
| 93 | The Lens of The Nameless Quality |
| 93½ | The Lens of Presence |
| 94 | The Lens of Atmosphere |
| 95 | The Lens of Spectation |
| 95½ | The Lens of Cheatability |
| 96 | The Lens of Friendship |
| 97 | The Lens of Expression |
| 98 | The Lens of Community |
| 99 | The Lens of Griefing |
| 100 | The Lens of Love |
| 101 | The Lens of the Team |
| 102 | The Lens of Documentation |
| 103 | The Lens of Playtesting |
| 104 | The Lens of Technology |
| 105 | The Lens of the Crystal Ball |
| 106 | The Lens of Utopia |
| 107 | The Lens of the Client |
| 108 | The Lens of the Pitch |
| 109 | The Lens of Profit |
| 110 | The Lens of Transformation |
| 111 | The Lens of Responsibility |
| 112 | The Lens of the Raven |
| ∞ | The Lens of Your Secret Purpose |

---

## WORKFLOW

### STEP 1 — GATHER INPUTS

Ask the user for the following, one at a time:

**A) Review Mode** — which applies?
- "What is built already" — reviewing existing work
- "What is being built" — reviewing work in progress
- "Lens review only" — no artifact, just lens evaluation and questions

**B) Body of Work** — ask the user to describe or share:
- What the framework, product, or standard is
- Its purpose and intended outcomes
- Any artifacts, documents, or specifics they want to share

**C) Personas** — ask the user to define each persona:
- Name / role
- Goals and motivations
- Pain points and frustrations
- What success looks like for them

Confirm all inputs are received before proceeding.

---

### STEP 2 — LENS RECOMMENDATION

Review the full lens index above against the body of work and personas provided. For each lens, load its questions from `LENSES.md` and evaluate:
- Is this lens directly applicable to the body of work?
- Does it reveal something meaningful about the user experience?
- Does it surface a risk, gap, or opportunity specific to this context?

Output a recommended lens set in three tiers:

**TIER 1 — CRITICAL (must review)**
Lenses where the body of work is highly exposed. List each with a 1-2 sentence rationale specific to the work and personas.

**TIER 2 — IMPORTANT (should review)**
Lenses that are relevant and will surface useful improvements. Rationale required per lens.

**TIER 3 — OPTIONAL (worth considering)**
Lenses that may apply depending on direction. Brief note on why they are conditional.

Every recommended lens must be justified against the specific body of work and personas. Lenses that do not apply should be silently excluded.

Ask the user to confirm, adjust, or reprioritize before proceeding.

---

### STEP 3 — LENS REVIEW SESSION

Work through each confirmed lens one at a time, starting with Tier 1.

For each lens:
1. **State the lens** — number, name, and plain-language description of what it evaluates
2. **Read the official questions** from `LENSES.md` and present them in context
3. **Apply it** — analyze the body of work through this lens, per persona where relevant
4. **Surface findings** — what is working, what is missing, what is at risk
5. **Ask the user** — one focused question to draw out their perspective
6. **Capture the verdict** — agree on a summary finding before moving on

Keep a running log of findings. Depth per lens is more valuable than speed.

---

### STEP 4 — BACKLOG OUTPUT

After completing the review, produce a structured backlog:

**Format per item:**
- **Item title** — short, action-oriented
- **Source lens** — which lens surfaced this
- **Persona(s) affected** — who this impacts
- **Finding** — what the lens revealed
- **Recommended action** — what to do about it
- **Priority** — High / Medium / Low
- **Type** — Fix / Improve / Explore / Validate

Sort by Priority descending. Offer to export as a document if the user wants a shareable artifact.

---

## EXTENSIBILITY NOTES

This skill works across any body of work. When applying to consumer products, games, or other contexts:
- Lenses related to character (#50, #85-91), story (#73, #75-78), and world (#84) become more prominent
- Lenses related to community (#96-99), expression (#97), and fantasy (#83) may shift from Tier 3 to Tier 1
- Adjust persona framing to fit the product context

The recommendation logic in Step 2 handles this automatically.

---

## PRINCIPLES

- Never pre-select lenses — always recommend with rationale, then confirm
- Always read official questions from `LENSES.md` before applying any lens
- Every lens applied must be specific to the work and personas, not generic
- Depth over breadth — thorough review of 12 lenses beats shallow pass of 40
- The backlog is the deliverable — the review session is the means to produce it
- Be honest when a lens does not apply rather than forcing a fit
