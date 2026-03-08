# The Great Soup Feast — Process Flow

> Every step from planning through post-event, who does what, and what the app handles.

---

## Phase 1: Event Setup (8-10 weeks before)

```
┌─────────────────────────────────────────────────────────────────────┐
│ ADMIN                                                               │
│                                                                     │
│  1. Log into /admin                                                 │
│  2. Create new event:                                               │
│     → Name, date, location, capacity, max soups                     │
│     → Set ranking depth (top 5)                                     │
│     → Toggle tasting notes on/off                                   │
│  3. Backfill archive (years 1 & 2) if not done yet                  │
│     → /admin/archive: winner, runner-up, soup list, photos          │
│                                                                     │
│  APP AUTO-GENERATES:                                                │
│  → Shared RSVP QR code (for postcards)                              │
│  → Event landing page at /                                          │
│  → Countdown timer on landing page                                  │
│  → /signup page (soup registration — not yet linked publicly)       │
│  → /ideas page (idea generator — always available)                  │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Phase 2: Guest List & Invites (6-8 weeks before)

```
┌─────────────────────────────────────────────────────────────────────┐
│ ADMIN                                                               │
│                                                                     │
│  1. Build guest list in /admin/guests                               │
│     → Add guests one-by-one or CSV import                           │
│     → For each guest: name, email, phone, invite channel preference │
│     → App auto-generates unique token per guest                     │
│                                                                     │
│  2. Prepare postcard content                                        │
│     → /admin exports: event details + shared QR code                │
│     → Jay drops content into Canva postcard design                  │
│     → Print & mail postcards                                        │
│                                                                     │
│  3. Set up drip campaign in /admin/campaigns                        │
│     → 6 messages pre-loaded as templates                            │
│     → Edit copy, set dates, assign channels (email/SMS/both)        │
│     → Test send to yourself                                         │
└─────────────────────────────────────────────────────────────────────┘

                              │
                    6 WEEKS BEFORE EVENT
                              │
                              ▼

┌─────────────────────────────────────────────────────────────────────┐
│ CAMPAIGN: SAVE THE DATE                                             │
│                                                                     │
│  Channel: Email + Postcard (mailed separately)                      │
│  Content: "The Great Soup Feast returns. Mark your calendar."       │
│  Link: → / (landing page with countdown + RSVP button)             │
│                                                                     │
│  ┌──────────────────────────────────────────────────────┐           │
│  │ GUEST EXPERIENCE                                     │           │
│  │                                                      │           │
│  │  Option A — Gets email:                              │           │
│  │    → Clicks unique link → /rsvp/:token               │           │
│  │    → Sees event details                              │           │
│  │    → Taps "I'm in!" or "Can't make it"               │           │
│  │    → App records RSVP status                         │           │
│  │                                                      │           │
│  │  Option B — Gets postcard:                           │           │
│  │    → Scans shared QR code → /rsvp                    │           │
│  │    → Enters their name                               │           │
│  │    → App matches to guest list OR creates new entry   │           │
│  │    → Taps "I'm in!" or "Can't make it"               │           │
│  │    → App records RSVP status                         │           │
│  └──────────────────────────────────────────────────────┘           │
│                                                                     │
│  APP TRACKS: sent count, opened, clicked, RSVP conversions          │
└─────────────────────────────────────────────────────────────────────┘

                              │
                    ADMIN MONITORS
                              │
                              ▼

┌─────────────────────────────────────────────────────────────────────┐
│ ADMIN: RSVP DASHBOARD                                               │
│                                                                     │
│  /admin/guests shows:                                               │
│  → Confirmed: 42  |  Declined: 8  |  No Response: 50               │
│  → Can manually update status for walk-ups or verbal RSVPs          │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Phase 3: Soup Registration (4-6 weeks before)

```
┌─────────────────────────────────────────────────────────────────────┐
│ CAMPAIGN: SOUP SIGN-UP OPENS (4 weeks out)                          │
│                                                                     │
│  Channel: Email + SMS                                               │
│  Content: "Think you've got what it takes? Register your soup."     │
│  Link: → /signup                                                    │
└─────────────────────────────────────────────────────────────────────┘

                              │
                              ▼

┌─────────────────────────────────────────────────────────────────────┐
│ COOK EXPERIENCE                                                     │
│                                                                     │
│  1. Lands on /signup                                                │
│  2. Enters:                                                         │
│     → Name                                                          │
│     → Soup name                                                     │
│     → Short description (2-3 sentences)                             │
│     → Dietary tags (multi-select: vegan, vegetarian, GF, DF, nuts,  │
│       spicy)                                                        │
│     → Optional: "surprise entry" flag (hide name until reveal)      │
│  3. Submits                                                         │
│  4. Gets confirmation page + unique cook link (to edit later)       │
│                                                                     │
│  ALSO AVAILABLE: /ideas ("What Should I Make?")                     │
│  → Spin the Wheel: random soup idea by category                     │
│  → Prompt Mode: 3 questions → 3 tailored suggestions               │
│  → Browseable anytime — no sign-up required                         │
└─────────────────────────────────────────────────────────────────────┘

                              │
                              ▼

┌─────────────────────────────────────────────────────────────────────┐
│ ADMIN: SOUP ROSTER                                                  │
│                                                                     │
│  /admin/soups shows new registrations immediately                   │
│  → Review, confirm, or mark tentative                               │
│  → Assign crockpot numbers (closer to event day)                    │
│  → Contact cooks if questions about dietary tags or descriptions    │
│  → Track: 25 target — currently at X/25                             │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Phase 4: Build-Up & Hype (2-4 weeks before)

```
┌─────────────────────────────────────────────────────────────────────┐
│ CAMPAIGN: LINEUP TEASER (2 weeks out)                               │
│                                                                     │
│  Channel: Email + SMS                                               │
│  Content: "25 soups confirmed. Here's a sneak peek at what's        │
│  brewing."                                                          │
│  → Shows 3-5 teaser soups (not all — build curiosity)               │
│  → Dietary breakdown: "8 vegan options this year!"                  │
│  → Link to /ideas for undecided cooks still thinking about entering │
└─────────────────────────────────────────────────────────────────────┘

                              │
                    1 WEEK BEFORE
                              │
                              ▼

┌─────────────────────────────────────────────────────────────────────┐
│ CAMPAIGN: FINAL CALL (1 week out)                                   │
│                                                                     │
│  Channel: Email + SMS                                               │
│  Content: "RSVP now. Voting goes live at the event."                │
│  → Final push for RSVPs                                             │
│  → Reminds cooks to finalize their entry                            │
│  → Teases the leaderboard and voting experience                     │
└─────────────────────────────────────────────────────────────────────┘

                              │
                              ▼

┌─────────────────────────────────────────────────────────────────────┐
│ ADMIN: PRE-EVENT PREP                                               │
│                                                                     │
│  1. Finalize soup roster                                            │
│     → Assign all crockpot numbers                                   │
│     → Confirm all entries (withdraw no-shows)                       │
│     → Export roster for table labels                                │
│                                                                     │
│  2. Review budget (/admin/budget)                                   │
│     → Update actual costs as purchases are made                     │
│                                                                     │
│  3. Generate day-of checklist (/admin/checklist)                    │
│     → Based on soup count + guest count                             │
│     → Tables, labels, crockpots, bowls, spoons, napkins            │
│     → QR code signs for voting stations                             │
│     → Projector/TV for leaderboard                                  │
│     → Extension cords, power strips                                 │
│                                                                     │
│  4. Print QR code signs for the venue                               │
│     → Large format: "SCAN TO VOTE" → links to /vote                │
│     → One per table or a few around the room                        │
│                                                                     │
│  5. Test everything                                                 │
│     → Cast /leaderboard?mode=tv to a screen                        │
│     → Submit a test ballot, verify it shows on leaderboard          │
│     → Delete test ballot                                            │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Phase 5: Event Day

```
┌─────────────────────────────────────────────────────────────────────┐
│ CAMPAIGN: GAME DAY (morning of)                                     │
│                                                                     │
│  Channel: SMS                                                       │
│  Content: "It's here. Scan, taste, vote."                           │
│  → Includes direct voting link for each guest                       │
└─────────────────────────────────────────────────────────────────────┘

                              │
                              ▼

┌─────────────────────────────────────────────────────────────────────┐
│ ADMIN: VENUE SETUP                                                  │
│                                                                     │
│  1. Set up soup tables with crockpot labels (number + name + tags)  │
│  2. Post QR code signs around the venue                             │
│  3. Cast /leaderboard?mode=tv to projector/TV                       │
│  4. Open voting: /admin → toggle "Voting Open"                      │
│  5. Monitor from phone throughout the event                         │
└─────────────────────────────────────────────────────────────────────┘

                              │
                              ▼

┌─────────────────────────────────────────────────────────────────────┐
│ GUEST EXPERIENCE: TASTING & VOTING                                  │
│                                                                     │
│  1. Arrive → grab a bowl                                            │
│  2. Walk the soup tables, taste soups                               │
│  3. Scan QR code or open link from SMS                              │
│     → Lands on /vote/:token (mobile-first)                         │
│                                                                     │
│  4. Browse soup list:                                               │
│     → Each soup: number, name, cook, dietary tags                   │
│     → Filter by dietary preference                                  │
│     → "I haven't tried this" toggle per soup                        │
│                                                                     │
│  5. Rank top 5 soups:                                               │
│     → Drag-to-rank or tap-to-add                                    │
│     → Sticky footer shows current ranking                           │
│     → Review before submitting                                      │
│                                                                     │
│  6. Submit ballot → "Your taste buds have spoken!"                  │
│     → Can revise until voting closes                                │
│                                                                     │
│  ┌──────────────────────────────────────────────────────┐           │
│  │ DISCOVERY NUDGE (post-submit)                        │           │
│  │                                                      │           │
│  │ "Before you go — these soups could use some love:"   │           │
│  │                                                      │           │
│  │  → "Under the Radar" — soups with fewer votes so far │           │
│  │    that match your dietary filters                    │           │
│  │  → "People who ranked [your #1] also tried..."       │           │
│  │  → "Only 3 people have voted for Soup #19 —          │           │
│  │     be the one who discovers it"                     │           │
│  │                                                      │           │
│  │  Guest can go taste more and update their ballot.    │           │
│  └──────────────────────────────────────────────────────┘           │
│                                                                     │
│  7. Optional: Leave tasting notes                                   │
│     → "Add notes" link on each soup card                            │
│     → Rate 1-5 ladles                                               │
│     → Tap flavor tags (savory, spicy, creamy, etc.)                 │
│     → Optional 140-char comment                                     │
│     → Notes are private (cook gets anonymized summary later)        │
└─────────────────────────────────────────────────────────────────────┘

                              │
                     MEANWHILE, ON THE BIG SCREEN
                              │
                              ▼

┌─────────────────────────────────────────────────────────────────────┐
│ LIVE LEADERBOARD (auto-rotating on TV)                              │
│                                                                     │
│  Cycles every 10-15 seconds through:                                │
│                                                                     │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐     │
│  │   VOTE PULSE    │  │     TOP 5       │  │ SOUP SPOTLIGHT  │     │
│  │                 │  │                 │  │                 │     │
│  │ "78 of ~100     │  │ 1. Soup #12     │  │ Soup #14:       │     │
│  │  ballots cast!" │  │ 2. Soup #3      │  │ Thai Coconut    │     │
│  │                 │  │ 3. Soup #21     │  │ Chaos by Maria  │     │
│  │ ████████░░ 78%  │  │ 4. Soup #7      │  │ "It's like a    │     │
│  │                 │  │ 5. Soup #19     │  │  hug from a     │     │
│  │                 │  │                 │  │  coconut"       │     │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘     │
│                                                                     │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐     │
│  │   SOUP FACT     │  │   WEIRD STAT    │  │   COUNTDOWN     │     │
│  │                 │  │                 │  │                 │     │
│  │ "The world's    │  │ "Soup #7 has    │  │  VOTING CLOSES  │     │
│  │  oldest soup    │  │  been ranked    │  │   IN 00:42:15   │     │
│  │  recipe is from │  │  #1 or dead     │  │                 │     │
│  │  6000 BC"       │  │  last. Nothing  │  │                 │     │
│  │                 │  │  in between."   │  │                 │     │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘     │
│                                                                     │
│  Also: Dietary Breakdown, Voter Milestones                          │
└─────────────────────────────────────────────────────────────────────┘

                              │
                    ADMIN CLOSES VOTING
                              │
                              ▼

┌─────────────────────────────────────────────────────────────────────┐
│ ADMIN: CLOSE VOTING                                                 │
│                                                                     │
│  /admin → toggle "Voting Closed"                                    │
│  → Voting page shows "Voting has ended — results coming soon!"     │
│  → Leaderboard switches to "Results coming..." holding screen       │
│  → RCV algorithm runs automatically in the background               │
│  → Admin can preview results at /admin/reveal before going live     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Phase 6: Results Reveal (event day, after voting closes)

```
┌─────────────────────────────────────────────────────────────────────┐
│ ADMIN: TRIGGER REVEAL                                               │
│                                                                     │
│  1. Go to /admin/reveal                                             │
│  2. Preview: see full results, Sankey, awards before anyone else    │
│  3. Click "Reveal Results" → /results goes live                     │
│  4. Announce to the room: "Results are in! Check your phones!"     │
│  5. Optionally walk through the Sankey on the big screen            │
└─────────────────────────────────────────────────────────────────────┘

                              │
                              ▼

┌─────────────────────────────────────────────────────────────────────┐
│ GUEST EXPERIENCE: RESULTS                                           │
│                                                                     │
│  /results (public — on the big screen and phones)                   │
│                                                                     │
│  1. SANKEY DIAGRAM (animated)                                       │
│     → All 25 soups on the left with Round 1 votes                   │
│     → Watch votes redistribute as soups get eliminated              │
│     → Winner emerges on the right with celebration animation        │
│                                                                     │
│  2. FINAL RANKINGS: 1st through 25th                                │
│                                                                     │
│  3. AWARDS:                                                         │
│     🏆 Champion — RCV winner                                        │
│     🥈 Runner-Up — 2nd place                                        │
│     🌟 Sleeper Hit — biggest mover from R1 to final                 │
│     🔥 Most Polarizing — highest ranking variance                   │
│     🫕 Crowd Comfort — most "hearty" + "savory" tags                │
│     🌶️ Boldest Bowl — most "spicy" + "smoky" + "umami" tags        │
│                                                                     │
│  4. FUN STATS:                                                      │
│     → Total votes, avg soups ranked per guest                       │
│     → Most-ranked soup (on the most ballots)                        │
│     → Hidden Gem (fewest ballots)                                   │
│     → Early birds vs. last-minute voters                            │
│                                                                     │
│  5. SOUP STORIES (if tasting notes active):                         │
│     → Per-soup card: ladle rating, flavor tags, guest comments      │
└─────────────────────────────────────────────────────────────────────┘

                              │
                              ▼

┌─────────────────────────────────────────────────────────────────────┐
│ PERSONAL RESULTS: /results/my/:token                                │
│                                                                     │
│  "Your ballot vs. the results"                                      │
│  → "You ranked Soup #12 first — it won!"                            │
│  → "Your #3 pick was the Sleeper Hit"                               │
│  → Shareable image card for social media                            │
│     "I voted for the champion!" / "I found the Hidden Gem!"        │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Phase 7: Post-Event (day after → 1 week after)

```
┌─────────────────────────────────────────────────────────────────────┐
│ CAMPAIGN: RESULTS ARE IN (day after)                                │
│                                                                     │
│  Channel: Email + SMS                                               │
│  Content: "And the winner is... [link to /results]"                 │
│  → For guests who left early or want to revisit                     │
│  → Includes link to personal results: /results/my/:token            │
└─────────────────────────────────────────────────────────────────────┘

                              │
                              ▼

┌─────────────────────────────────────────────────────────────────────┐
│ COOK FEEDBACK (auto-delivered after reveal)                         │
│                                                                     │
│  Each cook's unique link now shows their feedback page:             │
│                                                                     │
│  → Their soup's final ranking                                       │
│  → Aggregate ladle rating (avg + distribution chart)                │
│  → Flavor tag breakdown (bar chart)                                 │
│  → All anonymized guest comments                                    │
│  → Number of ballots their soup appeared on                         │
│  → "X people said your soup was [top flavor tag]"                   │
│                                                                     │
│  All notes anonymized — cooks see feedback, not who said it.        │
└─────────────────────────────────────────────────────────────────────┘

                              │
                              ▼

┌─────────────────────────────────────────────────────────────────────┐
│ ADMIN: POST-EVENT WRAP                                              │
│                                                                     │
│  1. Review tasting notes engagement                                 │
│     → How many guests left notes? Worth keeping the feature?        │
│                                                                     │
│  2. Finalize budget                                                 │
│     → Update actual costs, close out budget                         │
│                                                                     │
│  3. Archive auto-populates                                          │
│     → Year 3 data moves to /archive automatically                  │
│     → Upload event photos if desired                                │
│                                                                     │
│  4. Export data if needed                                            │
│     → Guest list, vote data, tasting notes for offline records      │
│                                                                     │
│  5. Collect informal feedback                                       │
│     → What worked? What didn't? Notes for next year.                │
│                                                                     │
│  6. Data cleanup (90 days post-event)                               │
│     → Guest contact info purged (or retained with consent)          │
│     → Archive data (winners, soup list, stats) kept permanently     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Full Timeline Summary

```
WEEK    ACTION                              WHO         APP FEATURE
─────   ──────────────────────────────────  ──────────  ─────────────────────
-10     Create event, build guest list      Admin       /admin
 -8     Design & mail postcards             Admin       QR code export
 -6     SEND: Save the Date                 Campaign    Email + postcard
 -6     RSVPs start coming in               Guests      /rsvp
 -4     SEND: Soup Sign-Up Opens            Campaign    Email + SMS
 -4     Cooks register soups                Cooks       /signup + /ideas
 -2     SEND: Lineup Teaser                 Campaign    Email + SMS
 -2     Finalize soup roster, assign #s     Admin       /admin/soups
 -1     SEND: Final Call                    Campaign    Email + SMS
 -1     Prep checklist, print QR signs      Admin       /admin/checklist
  0am   SEND: Game Day                      Campaign    SMS
  0     Set up venue, open voting           Admin       /admin
  0     Taste, vote, notes, leaderboard     Guests      /vote + /leaderboard
  0     Close voting, preview results       Admin       /admin/reveal
  0     REVEAL RESULTS                      Admin       /results
 +1     SEND: Results Are In                Campaign    Email + SMS
 +1     Cook feedback pages go live         Auto        Cook links
 +1     Personal results & sharing          Guests      /results/my/:token
 +7     Finalize budget, archive, cleanup   Admin       /admin
```
