# writing-triage

Review the provided text (or the most recent output) for AI writing signals
and rewrite to correct any issues found.

TRIGGER when: user runs `/writing-triage`, asks to "check this for AI writing",
"triage this writing", "does this sound AI-generated", or pastes text and asks
for a writing quality review.

DO NOT TRIGGER when: user is asking about the writing-triage skill itself,
editing the skill file, or working on code rather than prose.

---

## Instructions

### Step 1 — Identify the text to review

If the user provided text or a file path, use that.
If not, review the most recent output you generated in this conversation.
If neither exists, ask: "What text should I review? Paste it here or give me a file path."

### Step 2 — Load the detection framework

Read `.claude/skills/writing-triage.md` for the full detection categories:
1. Linguistic patterns (structural repetition, vague generalities, unnatural transitions, voice uniformity)
2. Factual plausibility (statistics, quotes, research studies)
3. Tone and style consistency (voice drift, passive voice overuse, missing experiential detail)

### Step 3 — Run the triage

Scan the text against all three detection categories. For each signal found:
- Name the category and specific indicator
- Quote the problematic excerpt (keep it short)
- Explain why it reads as AI-generated

### Step 4 — Produce the assessment

Output this structure:

---

**AI Writing Triage Review**

**Overall risk signal:** Low / Moderate / High

**Detected indicators:**
- [Category]: [Indicator] — [brief explanation]

**Evidence:**
> [quoted excerpt] — [what's wrong with it]

**Recommended corrections:**
- [Specific rewrite suggestion for each flagged item]

---

### Step 5 — Offer to rewrite

After delivering the assessment, ask:
"Want me to rewrite the flagged sections? I'll correct the AI signals and
keep the substance intact."

If the user says yes, rewrite only the flagged sections — don't restructure
the entire piece. Preserve the original voice, tone, and intent.

---

## Persona note

This command operates above all three context personas. Voice should be
direct and specific — name the exact problem and the exact fix. Don't
hedge about whether something "might" be AI-generated. Call it clearly,
fix it concretely.
