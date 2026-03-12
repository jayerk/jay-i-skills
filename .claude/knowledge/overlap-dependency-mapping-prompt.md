# Overlap Dependency Mapping Prompt

One Copilot prompt that takes the completed summary tables from all four
research prompt sets and generates a Mermaid diagram showing where product
standards overlap with SDLC, SPM, and I2I processes.

**When to run:** After you've completed at least some of the research prompts
from each set and filled in the summary tables. The more complete the tables,
the more useful the diagram.

**Purpose:** Create a visual dependency map for stakeholder conversations —
showing which standards are covered by which processes, where there's
duplication, and where gaps exist. This becomes the conversation artifact
for aligning with SDLC, SPM, and I2I owners.

---

## The Prompt

> I need you to generate a Mermaid diagram that maps the relationships between
> our **39 product management standards** and three enterprise processes:
> **SDLC**, **SPM (Strategic Portfolio Management)**, and **I2I (Idea to
> Implementation)**.
>
> Use the research results below to build the diagram. Each result tells you
> whether a product standard is covered (Embedded, Partial, Gap, or Conflict)
> by each process.
>
> ### Input Data
>
> **Paste your completed summary table rows here.** Use this format for each
> standard — one line per standard:
>
> ```
> Standard: [name]
> SDLC: [Embedded / Partial / Gap / Conflict]
> SPM: [Embedded / Partial / Gap / Conflict]
> I2I: [Embedded / Partial / Gap / Conflict]
> ```
>
> *(Example:)*
> ```
> Standard: Regular customer research cadence
> SDLC: Gap
> SPM: Gap
> I2I: Partial
>
> Standard: Risk register at checkpoints
> SDLC: Embedded
> SPM: Partial
> I2I: Embedded
> ```
>
> ### Diagram Requirements
>
> Generate a **Mermaid flowchart** with these specifications:
>
> **1. Four swim lanes (top to bottom):**
> - Product Standards (grouped by sub-practice)
> - SDLC
> - SPM
> - I2I
>
> **2. Node styling by coverage:**
> - `:::embedded` (green) — standard is fully covered by this process
> - `:::partial` (yellow) — standard is partially covered
> - `:::gap` (red) — standard is not addressed
> - `:::conflict` (orange) — standard conflicts with this process
>
> **3. Connections:**
> - Draw a solid line from each product standard to each process that covers
>   it (Embedded or Partial)
> - Use a dashed line for Conflict
> - No line for Gap
> - Label connections with the coverage level
>
> **4. Grouping:**
> - Group product standards by sub-practice (1-10)
> - Within each process lane, group by phase/stage where the standard is
>   addressed
>
> **5. Summary section:**
> - Below the diagram, add a table summarizing:
>
> | Coverage | SDLC Count | SPM Count | I2I Count |
> |----------|-----------|----------|----------|
> | Embedded | | | |
> | Partial  | | | |
> | Gap      | | | |
> | Conflict | | | |
>
> **6. Key insights to call out:**
> - Standards covered by ALL three processes (potential duplication —
>   opportunity to consolidate)
> - Standards covered by NONE of the three processes (true gaps —
>   product standards fill unmet need)
> - Standards where processes conflict (alignment conversations needed)
> - Standards covered by only ONE process (single point of accountability)
>
> ### Output Format
>
> Return:
>
> 1. The complete Mermaid diagram code (ready to paste into a Mermaid renderer)
> 2. The summary table
> 3. A "conversation guide" section with 3-5 bullet points I can use when
>    meeting with SDLC, SPM, and I2I owners to discuss the overlap
>
> The conversation guide should frame the overlap positively — we're not
> creating competing standards, we're looking for where product management
> practices can strengthen existing processes. Use language like:
> - "Your process already covers X — we'd like to formalize that alignment"
> - "Neither of us addresses Y — here's how we could embed it in your gate"
> - "We're both doing Z slightly differently — let's pick one approach"

---

## How to Use the Output

1. **Render the Mermaid diagram** — paste into any Mermaid-compatible tool
   (VS Code extension, Mermaid Live Editor, Confluence Mermaid macro)
2. **Share the summary table** — quick reference for which group owns what
3. **Use the conversation guide** — when meeting with SDLC, SPM, and I2I
   process owners

### Stakeholder Talking Points

The diagram answers three questions stakeholders will ask:

| Question | Where to Look |
|----------|--------------|
| "Are you duplicating our work?" | Green nodes in their lane — show alignment, not duplication |
| "What do you add that we don't have?" | Red nodes in their lane — standards that fill gaps |
| "Where do we disagree?" | Orange nodes — discuss and pick one approach |
