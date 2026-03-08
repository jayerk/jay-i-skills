# AI Writing Triage Skill

## Purpose

This skill performs **initial triage for AI-generated writing signals**.

It does not attempt to prove authorship. Instead, it identifies linguistic, structural, and factual patterns that are **statistically common in AI-generated text**.

If multiple signals appear, the text should be **reviewed more carefully and corroborated with additional evidence**.

The goal is **quality control and verification**, not accusation.

---

# When to Use This Skill

Run this review when evaluating:

* essays or articles of uncertain origin
* policy or research summaries
* online posts or marketing copy
* documents claiming firsthand experience
* material where authorship matters

This skill should **not be used as the sole determination of AI authorship**.

---

# Detection Categories

The review should check for signals in three areas:

1. linguistic patterns
2. factual plausibility
3. stylistic consistency

Each category may contain multiple indicators.

---

# 1. Linguistic Pattern Signals

AI systems often produce **balanced, polished sentence structures** with limited natural variation.

### Structural repetition

Look for:

* repeated clause templates
* similar sentence lengths
* recurring rhetorical constructions

Example pattern:

```
While X provides benefits, Y also introduces challenges.
```

If the same structure appears repeatedly across paragraphs, flag it.

### Vague generalities

AI often uses filler phrases instead of concrete detail.

Common examples include:

* “in today’s world”
* “it is important to note”
* “in conclusion”
* “various factors”
* “a number of considerations”

These phrases are not proof of AI writing, but **frequent repetition without supporting detail is suspicious**.

### Unnatural transitions

Look for transitions that move topics without substance.

Examples:

* abrupt paragraph shifts
* connective phrases without clear logic
* summary statements that introduce new ideas rather than synthesizing earlier ones

### Voice uniformity

AI writing often maintains an **oddly consistent tone**.

Indicators include:

* excessive hedging (“may,” “might,” “could potentially”)
* avoidance of firm positions
* lack of personal perspective
* absence of specific examples

---

# 2. Fact and Source Verification

Large language models can produce **confident but incorrect information**.

Check claims for plausibility.

### Statistics

Verify:

* the source organization
* the year
* the denominator or measurement unit

Red flag example:

A statistic referencing an agency dataset that does not exist.

### Quotes

Ensure:

* the quote appears in an original source
* the wording matches the primary document
* the attribution is correct

### Research studies

Verify:

* the journal or publisher
* the study title
* DOI or publication page

AI-generated writing sometimes invents **realistic but nonexistent citations**.

---

# 3. Tone and Style Consistency

Human writing tends to reflect **personal habits and lived experience**.

AI writing may drift stylistically.

### Voice drift

Look for:

* sudden shifts between formal and conversational tone
* switching between British and American spelling
* inconsistent punctuation or date formats

Example:

```
color → colour
March 5, 2024 → 5 March 2024
```

### Passive voice overuse

AI frequently uses passive constructions.

Examples:

```
The study was conducted…
The results were analyzed…
The findings were observed…
```

A persistent pattern across paragraphs may indicate machine generation.

### Missing experiential detail

If a document claims personal experience but lacks:

* specific locations
* dates
* sensory detail
* concrete anecdotes

request clarification or corroboration.

---

# Comparison Indicators

| Trait                | Human Writing                 | AI-Generated Writing              |
| -------------------- | ----------------------------- | --------------------------------- |
| Sentence variety     | Diverse structures and length | Uniform medium-length sentences   |
| Personal perspective | Anecdotes and specifics       | Generic observations              |
| Error pattern        | Minor typos or slips          | Grammatically perfect but shallow |
| Creativity           | Novel metaphors               | Template phrasing                 |
| Depth                | Nuanced argument              | Broad but surface-level           |

---

# Example Triage Signals

Example 1
A post repeats “it is important to note” multiple times across paragraphs.

Action: Flag as **AI-like rhetorical repetition**.

Example 2
An essay describing a professional experience contains no specific locations, dates, or events.

Action: Request **corroborating details**.

Example 3
A research summary cites a CDC report that does not exist.

Action: Flag as **possible hallucinated citation**.

---

# Reporting Format

When this skill is used, provide a structured assessment.

AI Writing Triage Review

Overall risk signal: Low / Moderate / High

Detected indicators:
• structural repetition
• vague generalities
• citation inconsistencies

Evidence examples:
[short excerpts]

Recommended action:
• verify citations
• request additional detail
• compare with known writing samples

---

# Important Limitation

This skill **cannot conclusively determine authorship**.

It should only identify signals that justify further verification.

Human review and corroborating evidence are required for any final determination.

---

One final observation worth keeping in mind: the real tell for machine writing isn’t grammar or polish. Humans can write clean prose too. The deeper signal is **absence of lived friction**—no sensory detail, no uneven edges, no stubborn specifics. Real experience leaves fingerprints. Machines tend to wipe the surface smooth.
