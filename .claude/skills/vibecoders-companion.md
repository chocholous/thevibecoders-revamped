# The Vibe Coders Companion

You are building a community website for The Vibe Coders. This skill ensures you maintain the project's unique character and make decisions aligned with its philosophy.

## The Actual Manifesto

**Core Statement:** "The universe is the limit. We command various AIs to craft apps, agents, webs, assets, toys—even businesses."

### The Seven Principles

1. **We push boundaries** - "The universe is the limit" (not just the sky)
2. **We learn through suffering** - "Yes, we suffer—a lot—but we learn from it"
3. **We're pioneers** - "Our tools often lack documentation, making us feel like pioneers. Because we are."
4. **We're diverse and we vibe** - "Different roles, experiences, ages, genders, backgrounds, and tech"
5. **We move fast** - "Last month is sooo history. We move fast, picking up and dropping new tools constantly"
6. **We keep it real** - "We don't sell our souls—or our contacts. Want to connect? Attend an event."
7. **We meet IRL** - "Vibe coding happens IRL" (but open to virtual future)

## The Actual Vibe

Key phrases from the real website:
- "We're pioneers. We're diverse. We vibe."
- "The universe is the limit"
- "We command various AIs"
- "We suffer—a lot—but we learn from it"
- "Last month is sooo history"
- "We don't sell our souls"
- "Vibe coding happens IRL"

## Current Community Status
- **9 Active Cities**: London 🇬🇧, Portland 🇺🇸, Porto 🇵🇹, Prague 🇨🇿, Stockholm 🇸🇪, Toronto 🇨🇦, Brno 🇨🇿, Pilsen 🇨🇿, San Francisco 🇺🇸
- **100+ Members** across all chapters
- **3+ Events** documented
- Growing but intimate - perfect size for personal connections

## Voice & Tone Guide

### Say This, Not That
- ✅ "Start a chapter in your city" → ❌ "Apply to be a leader"
- ✅ "Join the vibe" → ❌ "Register now"
- ✅ "We're building something together" → ❌ "Our platform enables"
- ✅ "Happening soon" → ❌ "Upcoming events"
- ✅ "Stories from the community" → ❌ "User-generated content"
- ✅ "Get involved" → ❌ "Sign up"

### Writing Principles
1. **Warmth over corporate** - Write like a friend, not a company
2. **Show, don't tell** - Photos and stories over descriptions
3. **Active voice** - "Organizers share..." not "Posts are shared..."
4. **Present tense** - Creates immediacy and energy
5. **Short sentences** - Punchy, clear, scannable

## YAGNI Defense Shield

When someone suggests these features, the answer is NO:
- "Should we add comments?" → NO. Keep it one-way broadcast.
- "What about user profiles?" → NO. This isn't LinkedIn.
- "Can we add likes/reactions?" → NO. Not a social network.
- "Should we build our own event system?" → NO. Luma exists.
- "What about a mobile app?" → NO. Web is enough.
- "Should we add categories/tags?" → NO. Chronological is fine.
- "Can organizers customize their pages?" → NO. Consistency matters.
- "Should we add analytics for organizers?" → NO. Keep it simple.
- "What about email notifications?" → NO. (except organizer applications)
- "Can we integrate with social media?" → NO. We ARE the community.

## Decision Shortcuts

### When choosing between options:
1. **Boring > Clever** - Choose proven technology
2. **Simple > Flexible** - Hardcode before abstracting
3. **Fast > Perfect** - Ship something that works
4. **Visible > Hidden** - Show activity, not metrics
5. **Direct > Indirect** - Link to Luma, don't wrap it

### Visual Identity (From Original Site):
- **Primary Color** - Deep purple background (#vibe-purple)
- **Accent Color** - Teal/cyan for highlights (#vibe-teal)
- **CTA Color** - Orange for primary actions (#vibe-orange)
- **Typography** - Bold modern sans-serif, white on dark
- **Layout** - Generous spacing, grid-based, card architecture
- **Personality** - Emoji integration (city flags, sparkles)
- **Code aesthetic** - Manifesto styled as VS Code editor

### Component Decisions:
- **Card layouts** - Always. Lists are too dense.
- **Images** - Required. Text-only is lifeless.
- **Animations** - Subtle only. 200ms max.
- **Colors** - Deep purple primary, teal accents, orange CTAs
- **Fonts** - Bold modern sans-serif (like original)

### Technical Choices (Decided):
- **Framework** - Astro (less code, minimal JS)
- **CMS/Database** - Airtable (everything in one place)
- **Forms** - Airtable Forms API (no custom backend)
- **Images** - Airtable attachments or Cloudinary
- **Auth** - Auth0 (Google + GitHub only)
- **Events** - Luma embeds (not API)
- **Hosting** - Vercel or Netlify (both work great)

## The Feeling We Want

Visitors should feel:
- **Curious** - "What's happening here?"
- **Welcomed** - "I could belong here"
- **Energized** - "Things are actually happening"
- **Confident** - "I could start this in my city"

Organizers should feel:
- **Supported** - "The tools just work"
- **Proud** - "My events look great here"
- **Connected** - "I'm part of something bigger"

## Component Personality

### Event Cards
- Photo-first (16:9 ratio)
- City badge (pride of place)
- Date as "Happening [soon/date]"
- One-line description max
- Link out to Luma (no internal pages)

### Organizer Posts
- Instagram-style cards
- Photo + short caption
- Organizer name and city
- Posted "2 days ago" style
- No engagement metrics

### Application Form
- Conversational labels ("What's your name?")
- Placeholder text with examples
- One question per screen on mobile
- Success message: "We'll be in touch soon!"
- No progress bars or steps

### Navigation
- Three items max initially
- No dropdowns
- Active state: purple underline
- Mobile: full-screen overlay, not hamburger

## Astro-Specific Guidance

### Component Strategy
- **Default to .astro files** - HTML-like, no JS overhead
- **React islands only for**:
  - Forms with complex validation
  - Real-time features (if any)
  - Rich interactions (image galleries, etc.)
- **Never use React for**:
  - Navigation
  - Static cards
  - Simple layouts

### Airtable Integration
- **Fetch at build time** - Use getStaticPaths()
- **Simple schema**:
  ```
  Posts: City, Text, Images[], Date, AuthorEmail
  Applications: Name, City, Links, Why, Status
  Organizers: Email, City, Auth0ID
  ```
- **No complex queries** - Airtable isn't a database
- **Rate limits** - Cache aggressively

## Red Flags to Avoid

Stop immediately if you find yourself:
- Creating user models/schemas (Airtable handles this)
- Building an admin panel (Airtable IS the admin)
- Writing custom backend code
- Making API endpoints (except for form submission)
- Creating more than 10 components
- Adding "just in case" fields to Airtable
- Building abstractions for single-use cases
- Using React when Astro components would work

## Validation Questions

Before implementing anything, ask:
1. Does this help someone find an event?
2. Does this help someone become an organizer?
3. Does this show community activity?

If no to all three → DON'T BUILD IT.

## UI Patterns from Manifesto Site

The original site likely has:
- Bold hero statements
- Plenty of whitespace
- High contrast text
- Geometric shapes or patterns
- Community photos (not stock)
- Clear CTAs without being pushy

Emulate the confidence without copying directly.

## Quick Wins (Do These)

- Animated purple gradient on hover
- Staggered fade-in for card grids
- City names in small caps
- "New" badge for events < 3 days old
- Lazy load images with blur-up
- Keyboard shortcuts (J/K for navigation)

## Time Wasters (Skip These)

- Perfect responsive breakpoints
- Cross-browser testing beyond Chrome/Safari/Firefox
- SEO optimization beyond basics
- Performance optimization before measuring
- Accessibility beyond WCAG AA
- i18n/l10n preparation

## The One Rule

**If you're unsure, choose the option that ships faster.**

The Vibe Coders is about momentum and energy. A simple site that exists beats a perfect site in planning. Build something people can see, feel, and join. Everything else is noise.

## Mantras for Tough Decisions

- "Is this Instagram or is this a tool?"
- "Would a busy organizer thank me for this?"
- "Am I building Twitter again?"
- "What would Stripe do? Now do half of that."
- "YAGNI until it hurts, then YAGNI some more."

Remember: You're building a megaphone for organizers, not a social network. Keep it simple, keep it moving, keep the vibe.