# The Great Soup Feast — App Design Spec

> A standalone web app for organizing, voting on, and celebrating an annual soup competition for ~100 guests and ~25 soups.

---

## 1. Core Concepts

| Concept | Description |
|---|---|
| **Event** | A single Soup Feast (annual). The app supports one active event at a time with an archive of past events. |
| **Soup** | A competition entry — has a name, cook, description, dietary tags (vegan, vegetarian, GF, etc.), and a table/crockpot number. |
| **Guest** | An attendee. May or may not also be a Cook. Identified by a short code or phone number — no account creation friction. |
| **Cook** | A guest who registered a soup. One soup per cook (or team). |
| **Vote** | A ranked-choice ballot. Each guest ranks their top N soups (recommended: top 5 of 25). |
| **Campaign** | A timed drip of messages (email/SMS) leading up to the event. |

---

## 2. User Roles

| Role | Can Do |
|---|---|
| **Admin (you)** | Everything — create event, manage soups, send campaigns, view all data, trigger results reveal |
| **Cook** | Sign up a soup, edit their entry, view the leaderboard |
| **Guest** | RSVP, vote, view leaderboard, optionally leave tasting notes |

No login walls. Guests get a unique link (via invite or QR code at the event). Cooks get a slightly different link when they register a soup.

---

## 3. App Sections

### 3.1 Planning Dashboard (Admin Only)

The command center for running the event. Only you see this.

**Features:**
- **Event Setup**: Set event name, date, location, capacity (~100), number of soups expected (~25)
- **Timeline Builder**: Key milestones with status indicators
  - Save the Date sent
  - Soup sign-up opens / closes
  - Formal invite sent
  - Voting opens / closes
  - Results revealed
- **Soup Roster**: Table of all registered soups — name, cook, dietary tags, crockpot number assignment, status (confirmed / tentative / withdrawn)
- **Guest List**: RSVP tracker — invited, confirmed, declined, no response. Supports manual adds.
- **Budget Tracker**: Simple line items — postcards, supplies, ingredients, venue — with running total
- **Checklist Generator**: Auto-generates day-of checklist based on soup count and guest count (table layout, labels, napkins, voting station setup, etc.)
- **Campaign Manager**: Create, schedule, and track drip messages (see Section 3.3)

---

### 3.2 Soup Sign-Up & Idea Generator

**Sign-Up Flow:**
1. Cook lands on sign-up page (linked from invite or shared URL)
2. Enters: name, soup name, short description (2-3 sentences), dietary tags (multi-select: vegan, vegetarian, gluten-free, dairy-free, contains nuts, spicy)
3. Optional: "surprise me" flag — hides soup name from leaderboard until reveal
4. Receives a confirmation with their unique cook link

**Idea Generator** ("What Should I Make?"):
A standalone page anyone can hit for inspiration. Two modes:

- **Spin the Wheel**: Random soup idea from a curated list. Tap to spin again. Categories: Classic Comfort, Around the World, Vegan/Plant-Based, Weird & Wonderful, Crowd Pleasers.
- **Prompt Mode**: Answer 3 quick questions → get 3 tailored suggestions
  1. Vegan or anything goes?
  2. Adventurous or crowd-pleaser?
  3. How much effort? (crockpot-and-forget / some love / showstopper)

  Returns 3 soup ideas with a one-liner description each. Sourced from a static curated list (no AI generation needed — just a good JSON file of ~100 soups with tags).

---

### 3.3 Invitations & Drip Campaign

**Dual-Channel Invites:**
- **Snail Mail**: App generates a printable postcard PDF (or card layout) with:
  - Event name, date, location
  - QR code linking to the RSVP page (unique per guest or a single shared link — your call)
  - Tagline / teaser
- **Electronic**: Same content delivered via email or SMS with a direct link

**Drip Campaign Timeline** (suggested, fully customizable):

| Timing | Message | Channel |
|---|---|---|
| 6 weeks out | **Save the Date** — "The Great Soup Feast returns. Mark your calendar." | Email + Postcard |
| 4 weeks out | **Soup Sign-Up Opens** — "Think you've got what it takes? Register your soup." | Email/SMS |
| 2 weeks out | **The Lineup Teaser** — "25 soups. Here's a sneak peek at what's brewing." | Email/SMS |
| 1 week out | **Final Call** — "RSVP now. Voting will be live at the event." | Email/SMS |
| Day of | **Game Day** — "It's here. Your voting link is ready." | SMS |
| Day after | **Results Are In** — "And the winner is... [link to reveal page]" | Email/SMS |

**Campaign Manager** (admin):
- Each message is a template with merge fields (guest name, event date, RSVP link)
- Status per message: draft → scheduled → sent
- Send manually or schedule auto-send
- Track: sent count, opened (email only), clicked

---

### 3.4 Day-of Voting

**How It Works:**
1. Guest scans a QR code at the event (or opens their link from the SMS)
2. Lands on a mobile-first voting page — no app install, no login
3. Sees all 25 soups listed with: number, name, cook name, dietary tags
4. Drags or taps to rank their **top 5** (configurable by admin)
5. Submits ballot — gets a fun confirmation ("Your taste buds have spoken!")
6. One ballot per guest link. Can update until voting closes.

**Ranked Choice Voting (RCV) Algorithm:**
- Instant-runoff style
- Round 1: Count all #1 votes. If a soup has >50% of first-place votes, it wins.
- Round 2+: Eliminate the soup with the fewest #1 votes. Redistribute those ballots to each voter's next-ranked soup. Repeat until a winner emerges.
- Also compute: "People's Runner-Up" (2nd place), "Sleeper Hit" (biggest jump from round 1 to final), "Most Polarizing" (highest variance in ranking)

**Voting UX Details:**
- Big, tappable soup cards on mobile
- Drag-to-rank or tap-to-add-to-ranking
- Clear "your current ranking" sidebar/footer
- Dietary filter toggles (show only vegan, etc.)
- "I haven't tried this one" indicator (optional — helps you understand coverage)

---

### 3.5 Digital Tasting Notes (Experimental)

Low-friction, optional. Test it this year and see if people engage.

**Per-Soup Mini Review:**
- Star rating (1-5 ladles instead of stars)
- One-tap flavor tags: Savory, Sweet, Spicy, Creamy, Hearty, Light, Umami, Smoky
- Optional free-text note (max 140 chars — keep it tweet-length)

**Where It Lives:**
- Accessible from the voting page — small "add notes" link on each soup card
- Notes are private to the guest unless they opt to share
- Admin can see aggregate ratings and tag clouds per soup

**Why Test It:**
- Gives cooks actual feedback beyond "you won / you didn't"
- Flavor tag data makes cool post-event visualizations
- If nobody uses it, kill it next year — zero harm

---

### 3.6 Live Leaderboard

The heartbeat of the event. Displayed on a big screen at the venue AND accessible on phones.

**What's On It — A Rotating Feed:**

The leaderboard is NOT just a ranked list. It's a living display that cycles through content blocks every 10-15 seconds:

| Block Type | Content | Example |
|---|---|---|
| **Vote Pulse** | Current vote count + animated progress bar per soup | "78 of ~100 ballots cast!" |
| **Soup Spotlight** | Random soup highlight — name, cook, fun description | "Soup #14: Thai Coconut Chaos by Maria — 'It's like a hug from a coconut'" |
| **Soup Fact** | Random soup trivia | "Americans eat over 10 billion bowls of soup per year" |
| **Leaderboard Snapshot** | Top 5 soups by current first-place votes (no final results — just a teaser) | Updated live as votes come in |
| **Weird Stat** | Fun computed stat from the vote data | "Soup #7 has been ranked #1 or #5 — nothing in between. Polarizing!" |
| **Dietary Breakdown** | Visual showing the vegan/veggie/GF breakdown of entries | Pie or icon chart |
| **Voter Milestone** | Celebration when vote count milestones hit | "50 votes in! Halfway there!" |
| **Countdown** | Time remaining until voting closes | Ticking clock |

**Presentation Mode:**
- Full-screen, auto-rotating, designed for a TV/projector
- Dark background, large type, animated transitions
- No interaction needed — just cast it to a screen

**Phone Mode:**
- Same content blocks but scrollable
- Tap a soup to see its details / leave tasting notes

---

### 3.7 Results Reveal

Not shown until admin triggers the reveal. This is the ceremony.

**Reveal Page Flow:**
1. Admin clicks "Reveal Results" — page goes live
2. **Sankey Diagram**: Animated visualization showing how votes flowed through each RCV round
   - Left side: all 25 soups with their Round 1 vote counts
   - Each elimination round shows votes redistributing
   - Right side: final winner highlighted
   - Color-coded by soup — eliminated soups fade out
3. **Final Rankings**: Full ordered list — 1st through 25th
4. **Awards Section**:
   - **Champion**: The winner
   - **Runner-Up**: 2nd place
   - **Sleeper Hit**: Biggest mover from first round to final ranking
   - **Most Polarizing**: Highest variance in rankings
   - **Crowd Comfort**: Most "hearty" + "savory" tasting note tags (if tasting notes are used)
   - **Boldest Bowl**: Most "spicy" + "adventurous" tags
5. **Soup Stories** (if tasting notes are active): Per-soup card with aggregate star rating, top flavor tags, and a few highlighted guest notes
6. **Fun Stats Recap**:
   - Total votes cast
   - Average soups tasted per guest
   - Most-ranked soup (appeared on the most ballots)
   - Least-ranked soup (fewest ballots — "the hidden gem")
   - Voting time distribution (when did people vote — early vs. last minute)

**Shareable:**
- Each guest gets a "your ballot vs. the results" comparison
- Shareable result card (image) for social media — "I voted for the winner!" or "My #1 pick was the Sleeper Hit!"

---

## 4. Data Model

```
Event
  ├── id
  ├── name ("The Great Soup Feast 2026")
  ├── date
  ├── location
  ├── capacity
  ├── voting_open (boolean)
  ├── results_revealed (boolean)
  ├── config
  │     ├── max_soups (25)
  │     ├── ranking_depth (5)  // how many soups each guest ranks
  │     └── tasting_notes_enabled (boolean)
  │
  ├── Soups[]
  │     ├── id
  │     ├── number (table/crockpot number)
  │     ├── name
  │     ├── cook_name
  │     ├── description
  │     ├── dietary_tags[] (vegan, vegetarian, gf, df, nuts, spicy)
  │     ├── surprise_entry (boolean)
  │     └── status (confirmed / tentative / withdrawn)
  │
  ├── Guests[]
  │     ├── id
  │     ├── name
  │     ├── contact (email or phone)
  │     ├── invite_channel (mail / email / sms / both)
  │     ├── rsvp_status (invited / confirmed / declined / no_response)
  │     ├── unique_link_token
  │     └── is_cook (boolean → links to Soup)
  │
  ├── Ballots[]
  │     ├── id
  │     ├── guest_id
  │     ├── rankings[] (ordered list of soup_ids, position = rank)
  │     ├── submitted_at
  │     └── updated_at
  │
  ├── TastingNotes[]
  │     ├── id
  │     ├── guest_id
  │     ├── soup_id
  │     ├── rating (1-5)
  │     ├── flavor_tags[]
  │     ├── note_text (max 140 chars)
  │     └── shareable (boolean)
  │
  ├── Campaigns[]
  │     ├── id
  │     ├── name
  │     ├── send_date
  │     ├── channel (email / sms / both)
  │     ├── template_body
  │     ├── status (draft / scheduled / sent)
  │     └── stats { sent, opened, clicked }
  │
  └── Budget[]
        ├── id
        ├── item
        ├── estimated_cost
        ├── actual_cost
        └── category (supplies / printing / food / venue / other)
```

---

## 5. Suggested Tech Stack

| Layer | Choice | Why |
|---|---|---|
| **Framework** | Next.js (App Router) | Full-stack in one project. SSR for the reveal page, API routes for voting, static for the leaderboard. |
| **Database** | PostgreSQL (via Supabase or Neon) | Relational data with easy joins. Free tier covers this scale easily. |
| **ORM** | Drizzle or Prisma | Type-safe queries. Drizzle is lighter, Prisma has better DX. |
| **Auth** | None for guests (token-based links). Simple password or magic link for admin. | No friction for 100 guests. |
| **Real-time** | Supabase Realtime or Server-Sent Events | Live leaderboard updates as votes come in. |
| **Email/SMS** | Resend (email) + Twilio (SMS) | Both have generous free tiers. Resend is dead simple. |
| **PDF Generation** | @react-pdf/renderer | For printable postcard/invite layouts. |
| **Sankey Diagram** | D3.js or Recharts with custom Sankey | D3 gives full control over the animation. |
| **Hosting** | Vercel | Free tier. Auto-deploys from GitHub. Perfect for Next.js. |
| **Styling** | Tailwind CSS | Fast to build, easy to theme (soup-themed color palette). |

---

## 6. Soup Idea Generator — Data Structure

A static JSON file with ~100 soup ideas, tagged for the generator:

```json
{
  "soups": [
    {
      "name": "Roasted Red Pepper & Gouda",
      "category": "crowd_pleaser",
      "vegan": false,
      "effort": "some_love",
      "description": "Smoky roasted peppers with melty gouda. Dangerously good."
    },
    {
      "name": "West African Peanut Stew",
      "category": "around_the_world",
      "vegan": true,
      "effort": "some_love",
      "description": "Rich, spicy, peanutty. Sweet potato and greens. A showstopper."
    }
  ]
}
```

Categories: `classic_comfort`, `around_the_world`, `vegan_plant_based`, `weird_wonderful`, `crowd_pleaser`

Effort levels: `crockpot_and_forget`, `some_love`, `showstopper`

---

## 7. Page Map

```
/                          → Public landing page (event info, countdown, RSVP link)
/rsvp/:token               → Guest RSVP page
/signup                     → Cook soup registration
/ideas                      → Soup idea generator
/vote/:token                → Voting page (mobile-first)
/vote/:token/notes/:soupId  → Tasting notes for a specific soup
/leaderboard                → Live leaderboard (public, auto-rotating)
/leaderboard?mode=tv        → Full-screen presentation mode
/results                    → Results reveal (hidden until admin triggers)
/results/my/:token          → "Your ballot vs. results" personal view
/admin                      → Planning dashboard (password protected)
/admin/soups                → Soup roster management
/admin/guests               → Guest list & RSVP tracking
/admin/campaigns            → Campaign manager
/admin/budget               → Budget tracker
/admin/reveal               → Trigger results reveal
```

---

## 8. RCV Algorithm — Pseudocode

```
function runRCV(ballots, soups):
    rounds = []
    remaining = [...soups]
    activeBallots = [...ballots]

    while remaining.length > 1:
        // Count first-place votes among remaining soups
        counts = {}
        for ballot in activeBallots:
            topPick = ballot.rankings.find(s => remaining.includes(s))
            if topPick:
                counts[topPick] += 1

        round = { counts, eliminated: null }

        // Check for majority
        total = sum(counts.values())
        for soup, count in counts:
            if count > total / 2:
                rounds.push(round)
                return { winner: soup, rounds }

        // Eliminate lowest
        lowest = min(counts, by: value)
        round.eliminated = lowest
        remaining.remove(lowest)
        rounds.push(round)

    return { winner: remaining[0], rounds }
```

Each `round` object feeds directly into the Sankey diagram — showing where eliminated votes went.

---

## 9. Open Questions

1. **Guest identification**: Unique links per guest (more tracking, more setup) vs. shared link + name entry (less setup, risk of duplicates)?
2. **Postcard design**: Do you want to design the postcard yourself, or should the app generate a templated one?
3. **Historical data**: Is this year one, or do you have past results to seed an "archive" section?
4. **SMS provider**: Twilio is solid but costs per-message. Are you okay with that, or do you want email-only for the drip campaign?
5. **Tasting notes privacy**: Should notes default to private (guest opts in to share) or public (guest opts out)?
6. **Leaderboard spoilers**: Show real-time top 5 during voting, or keep it fully hidden until reveal?

---

## 10. What's Next

This spec is ready to become a repo. Recommended order of build:

1. **Data model + admin dashboard** — get the planning tools working first
2. **Soup sign-up + idea generator** — open registration
3. **Invite system + campaign manager** — send save-the-dates
4. **Voting system + RCV engine** — the core game-day feature
5. **Leaderboard** — the live display
6. **Results reveal + Sankey** — the grand finale
7. **Tasting notes** — experimental, build last
