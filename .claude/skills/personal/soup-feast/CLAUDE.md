# CLAUDE.md — soup-feast

A standalone web app for organizing, voting on, and celebrating an annual soup
competition. Ranked-choice voting, campaign messaging, no-login guest experience.

---

## Skills & Persona (jay-i-skills)

- **Skills repo path**: `~/repos/jay-i-skills`
- **Context**: `personal` — read `.claude/skills/personal/_persona.md` before any skill work.
- **Design docs**:
  - `.claude/skills/personal/soup-feast/soup-feast-app-design.md` — PRD with core concepts, user roles, pages, data model, tech stack
  - `.claude/skills/personal/soup-feast/soup-feast-process-flow.md` — end-to-end process from event setup through post-event
- **Relevant skills**:
  - `.claude/skills/work/internal-tooling/SKILL.md` — HTML/React SPA patterns, dashboard conventions

Do NOT duplicate persona or skill content in this repo. Always reference the
skills repo.

---

## Repo-Specific Context

### Tech Stack

Per the app design doc:
- **Frontend**: React (Vite), Tailwind CSS, Framer Motion
- **Backend**: Supabase (Postgres, Auth, Realtime, Edge Functions)
- **Messaging**: Twilio (SMS + email campaigns)
- **Hosting**: Vercel
- **QR codes**: Generated server-side for RSVP postcards

### Key Design Decisions

- **No login walls.** Guests and cooks use unique link tokens. Admin uses a simple password.
- **Ranked-choice voting.** Each guest ranks top 5 soups. Instant-runoff tallying.
- **Campaign system.** Timed drip messages (email + SMS) with admin preview before send.
- **Mobile-first.** Voting happens on phones at the event.

### How to Use

1. Read the persona from the skills repo (`personal/_persona.md`)
2. Read both design docs before making architectural decisions
3. Reference `internal-tooling/SKILL.md` for SPA patterns and component conventions
4. Keep the voice casual and fun — this is a soup competition, not enterprise software
