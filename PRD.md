# The Vibe Coders - Product Requirements Document

## Vision
Build a clean, minimal community website that serves as an events hub and organizer recruitment platform for The Vibe Coders community, maintaining the playful yet minimal tone from https://thevibecoders.community.

## User Personas

### 1. Community Visitor
- **Who**: Someone curious about The Vibe Coders, possibly heard about it through word-of-mouth
- **Needs**: Find events in their city, understand the vibe, see community activity
- **Goals**: Attend an event, connect with local chapter

### 2. Potential Organizer
- **Who**: Motivated individual who wants to bring The Vibe Coders to their city
- **Needs**: Clear application process, understand organizer expectations
- **Goals**: Start a local chapter, get approved and supported

### 3. Current Organizer
- **Who**: Active chapter leader running events
- **Needs**: Simple way to post updates, share event photos, promote upcoming gatherings
- **Goals**: Keep community engaged, showcase chapter activity

## User Stories

### Core Stories (MVP)
- [ ] As a **visitor**, I want to see upcoming events in various cities so that I can find one to attend
- [ ] As a **visitor**, I want to browse past events and photos so that I understand the community vibe
- [ ] As a **potential organizer**, I want to apply to start a chapter so that I can bring The Vibe Coders to my city
- [ ] As a **current organizer**, I want to post event updates with photos so that I can showcase our chapter's activity
- [ ] As a **visitor**, I want to see a chronological feed of community posts so that I know the community is active

### Future Stories (Post-MVP)
- [ ] As a **visitor**, I want to filter events by city
- [ ] As an **organizer**, I want to edit/delete my posts
- [ ] As a **visitor**, I want to subscribe to event notifications for my city

## Success Metrics

### Primary KPIs
- Number of organizer applications submitted per month
- Number of event posts published per week
- Click-through rate to Luma event pages
- Time to first meaningful paint (< 2 seconds)

### Secondary Metrics
- Average time on site
- Return visitor rate
- Geographic diversity of applications
- Photo upload engagement rate

## Technical Constraints

### Performance
- Desktop-first responsive design
- Fast load times (< 2s initial load)
- Image optimization required
- Minimal JavaScript where possible

### Integration Points
- Luma Calendar (event management)
- Form submission service (organizer applications)
- Image hosting solution (CDN for uploaded photos)
- Simple authentication for organizers (passwordless preferred)

## In Scope

### Phase 1 (MVP)
1. **Home/Events Feed**
   - Chronological card-based feed
   - Mix of organizer posts and event listings
   - Simple, clean card design

2. **Event Discovery**
   - Upcoming events section (Luma integration)
   - Past events archive
   - Direct links to Luma for registration

3. **Organizer Application**
   - Single form page
   - Fields: Name, City, Links, Motivation
   - Email notification on submission

4. **Organizer Upload**
   - Protected route (simple auth)
   - Form: City, Text (500 chars), Images (1-5)
   - Direct publish to feed

5. **Core Pages**
   - Home (feed + upcoming events)
   - Events (comprehensive list)
   - Become an Organizer (application + info)

## Out of Scope (YAGNI)

### Explicitly Not Building
- User accounts/profiles for attendees
- Comment system
- Like/reaction system
- Complex tagging or categorization
- Search functionality (initially)
- Email newsletters
- Direct messaging
- Event creation (stays in Luma)
- Payment processing
- Multi-language support (initially)
- Native mobile apps
- Complex CMS with roles/permissions
- Analytics dashboard for organizers
- Social media auto-posting

## Open Questions

### Technical Decisions Needed
1. **Framework**: Next.js (App Router) vs Astro vs Remix?
   - Leaning: Next.js for familiarity and ecosystem

2. **Hosting**: Vercel vs Netlify vs AWS?
   - Leaning: Vercel for Next.js optimization

3. **Image Storage**: Cloudinary vs S3 vs Vercel Blob?
   - Need: Resize on upload, CDN delivery

4. **Form Handling**: Formspree vs Custom API vs Airtable?
   - Need: Email notifications, simple storage

5. **Auth Solution**: Clerk vs NextAuth vs Passwordless email?
   - Need: Minimal friction for ~10-20 organizers

6. **Content Storage**: MDX files vs Postgres vs Notion API?
   - Need: Simple CRUD for posts, no complex queries

## Definition of Done

### MVP Completion Criteria
- [ ] Static home page renders with design system
- [ ] Feed displays at least 3 sample posts
- [ ] Upcoming events pulls from Luma (or displays mocked data)
- [ ] Organizer form submits and sends notification
- [ ] Organizer can upload a post (even if auth is basic)
- [ ] Site is responsive and loads quickly
- [ ] Matches tone/vibe of manifesto site

## Timeline Estimate
- **Sprint 1**: Foundation (Design system, project setup, static pages)
- **Sprint 2**: Feed & Events (Display logic, Luma integration)
- **Sprint 3**: Organizer Features (Application form, upload flow)
- **Sprint 4**: Polish & Deploy (Auth, optimization, deployment)

*Note: Each sprint represents focused work sessions, not calendar weeks*