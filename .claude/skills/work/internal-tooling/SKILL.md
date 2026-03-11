---
name: internal-tooling
description: "Building internal tools — HTML/React single-page apps, interactive prototypes, and visual artifacts for internal use. Use this skill when creating working software that demonstrates concepts or operationalizes frameworks."
---

# Internal Tooling

## Overview

This skill covers building working software for internal use — interactive tools, dashboards, assessment interfaces, and visual demos. These are not throwaway prototypes; they're production-quality artifacts that encode expertise and operationalize frameworks. A self-running demo is worth more than a slide explaining the concept.

This is where the vocabulary terms **Working Demo**, **Self-Running Artifact**, **Encode Expertise**, and **Operationalize** come to life. See `knowledge/vocabulary.md` for definitions.

## When to Use This Skill

- Building an HTML/React single-page app for internal use
- Creating an interactive assessment or scoring tool
- Building a dashboard or visualization
- Creating a working demo to communicate a concept
- Turning a framework into an interactive tool (e.g., a maturity assessment into a scored web app)
- Building a prototype to validate an approach before requesting engineering resources

## When NOT to Use This Skill

- **Production backend services** — if it needs a server, database, or deployment pipeline from the start, it's an engineering project, not an internal tool.
- **External-facing products** — tools built with this skill are for internal use. Customer-facing software has different quality, accessibility, and compliance requirements.
- **Engineering handoff from day one** — if the plan is to hand the codebase to an engineering team immediately, start with their stack and conventions, not this skill's conventions.
- **Content or document creation** — if the output is a document, deck, or assessment narrative, use the relevant content skill instead.

## Quality Bar

- **Works standalone** — the tool runs without a backend or complex setup. Single HTML file or simple React app, self-contained.
- **Visually clean** — internal doesn't mean ugly. Consistent spacing, readable typography, intentional color use. Tailwind CSS or equivalent utility-first styling.
- **Immediately usable** — a new user can understand what the tool does and start using it without instructions. The UI is the documentation.
- **Encodes expertise** — the tool embodies a framework, rubric, or assessment methodology. It's not just a form — it applies logic, scores, and surfaces insights.
- **Responsive** — works on desktop and tablet at minimum. Phone is a bonus but not required for internal tools.

## Process

### Step 1: Define the Tool's Job
- What decision does this tool support?
- What manual process does it replace or augment?
- What framework or rubric does it operationalize?
- Who uses it, and in what context? (Workshop? Individual assessment? Team review?)

### Step 2: Design the Interaction
- What are the inputs? (Selections, scores, text, configuration)
- What are the outputs? (Scores, visualizations, recommendations, exports)
- What's the flow? (Linear form? Dashboard? Multi-step wizard?)
- Where does expertise get encoded? (Scoring logic, weightings, thresholds, conditional guidance)

### Step 3: Choose the Stack
For most internal tools:
- **Single-file HTML** — for simple tools, assessments, calculators. No build step. Open in a browser.
- **React SPA** — for more complex tools with state management, multiple views, or data persistence. Vite.
- **Tailwind CSS** — utility-first styling for consistent, clean interfaces.
- **Local storage** — for persistence when a backend isn't justified.
- **CSV/JSON export** — for tools that produce data others need to use elsewhere.

### Step 4: Build Iteratively
1. **Skeleton first** — layout, navigation, empty states. Validate the flow before adding logic.
2. **Core logic second** — scoring, calculations, framework application. The brain of the tool.
3. **Polish third** — visual refinement, edge cases, empty states, loading states.
4. **Export/share last** — CSV export, shareable links, print styling if needed.

### Step 5: Validate
- Can someone who didn't build it use it without explanation?
- Does the scoring/logic match the intended framework?
- Does it handle edge cases (no input, extreme values, incomplete data)?
- Is it visually presentable in a stakeholder meeting?

## Technical Conventions

### HTML Single-File Apps
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[Tool Name]</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <!-- Additional CDN dependencies as needed -->
</head>
<body class="bg-gray-50 min-h-screen">
  <div id="app" class="max-w-4xl mx-auto p-6">
    <!-- Tool content -->
  </div>
  <script>
    // Application logic
  </script>
</body>
</html>
```

### React SPAs
- Use functional components and hooks
- Organize by feature, not by file type
- Keep state as local as possible
- Use Tailwind for styling — no custom CSS unless necessary
- Include a clear README with setup instructions

## Output Formats

The output of this skill is working code — an HTML file or React app that can be opened/run immediately. Always include:
- The complete, runnable code
- A brief description of what the tool does
- Instructions for running it (usually "open in a browser")

## Anti-Patterns

- **Prototype theater** — building something that looks functional but has no real logic. Every interactive element should do something meaningful.
- **Over-engineering** — reaching for a database, authentication, or deployment pipeline when localStorage and a single HTML file would work.
- **Invisible expertise** — building a tool that collects data but doesn't apply the framework. The tool should score, assess, recommend — not just record.
- **Ugly internals** — treating "internal" as permission to skip visual quality. Internal tools need to earn adoption through craftsmanship.

## Downstream Repos

Tools built from this skill live in their own repositories, not in jay-i-skills. Each tool repo gets a `CLAUDE.md` that points back to this skills repo for persona and skill context. See the "Downstream Repo Pattern" section of the root `CLAUDE.md` for the required format.
