# The Vibe Coders - Project Plan

## Current Sprint: Foundation (Sprint 1)

### In Progress
- [ ] **TASK-001**: Define design system tokens and create design-system.md

### Ready
- [ ] **TASK-002**: Initialize Astro project with minimal template
- [ ] **TASK-003**: Configure Tailwind CSS with custom tokens
- [ ] **TASK-004**: Add React integration for interactive islands
- [ ] **TASK-005**: Create base Astro layout component
- [ ] **TASK-006**: Build responsive navigation (Astro component)
- [ ] **TASK-007**: Create hero section for home page
- [ ] **TASK-008**: Set up Airtable connection and schema

### Completed
✅ Project structure created
✅ PRD.md documented
✅ Initial planning setup

---

## Sprint 2: Airtable Integration & Feed

### Backlog
- [ ] **TASK-009**: Create Airtable base with Posts, Applications, Organizers tables
- [ ] **TASK-010**: Build Airtable data fetching utilities
- [ ] **TASK-011**: Create post card component (Astro)
- [ ] **TASK-012**: Build feed layout with card grid
- [ ] **TASK-013**: Add Luma Calendar embed widgets
- [ ] **TASK-014**: Create events listing page with Luma embeds
- [ ] **TASK-015**: Connect Airtable posts to feed display
- [ ] **TASK-016**: Implement image display from Airtable attachments

---

## Sprint 3: Auth0 & Organizer Features

### Backlog
- [ ] **TASK-017**: Set up Auth0 application (Google + GitHub providers)
- [ ] **TASK-018**: Implement Auth0 authentication in Astro
- [ ] **TASK-019**: Create organizer application form (submit to Airtable)
- [ ] **TASK-020**: Build protected organizer upload page
- [ ] **TASK-021**: Create upload form (text + images to Airtable)
- [ ] **TASK-022**: Connect organizer posts to main feed
- [ ] **TASK-023**: Add form validation and error handling
- [ ] **TASK-024**: Test full organizer flow (apply → approve → upload)

---

## Sprint 4: Polish & Deploy

### Backlog
- [ ] **TASK-025**: Performance optimization audit
- [ ] **TASK-026**: Implement lazy loading for images
- [ ] **TASK-027**: Add loading states and skeletons
- [ ] **TASK-028**: SEO optimization and meta tags
- [ ] **TASK-029**: Set up error boundaries
- [ ] **TASK-030**: Configure production deployment
- [ ] **TASK-031**: Set up monitoring and analytics
- [ ] **TASK-032**: Final design polish and animations

---

## Technical Decisions Log

### Decided ✅
- **Framework**: Astro (less code heavy, easy to maintain)
- **CMS/Database**: Airtable (all content and forms)
- **Styling**: Tailwind CSS
- **authentication**: Auth0 (Google + GitHub login)
- **Events**: Luma Calendar (embed widgets)
- **Project management**: PLAN.md + MADRs for major decisions

### Pending
- [ ] Hosting platform (Vercel vs Netlify - both work great with Astro)
- [ ] Image optimization (Cloudinary vs Airtable attachments)

---

## Validation Gates

### Gate 1: Static Site Working ⏳
- [ ] Design system implemented
- [ ] Navigation functional
- [ ] Home page renders with proper styling
- **Target**: End of Sprint 1

### Gate 2: Feed Rendering ⏳
- [ ] Event cards display
- [ ] Post cards display
- [ ] Grid layout responsive
- **Target**: Mid Sprint 2

### Gate 3: Form Submission ⏳
- [ ] Application form works
- [ ] Data persists somewhere
- [ ] Email notification sent
- **Target**: Mid Sprint 3

### Gate 4: Full Loop Complete ⏳
- [ ] Organizer can upload
- [ ] Post appears in feed
- [ ] Events display from Luma
- **Target**: End of Sprint 3

---

## Notes & Blockers

### Current Blockers
- None yet

### Decisions Needed
1. Confirm Next.js as framework choice
2. Select image hosting solution
3. Choose form handling approach

### Resources & Links
- Manifesto site: https://thevibecoders.community
- Luma Calendar: [TBD - need account access]
- Design inspiration: Stripe (clarity) + Notion (warmth)

---

## Definition of Ready
Before starting a task:
- [ ] Requirements are clear
- [ ] Dependencies identified
- [ ] Acceptance criteria defined
- [ ] Technical approach agreed

## Definition of Done
Task completion requires:
- [ ] Code implemented and working
- [ ] Responsive design verified
- [ ] No console errors
- [ ] Follows design system
- [ ] Accessibility checked (keyboard nav, contrast)
- [ ] Committed to repository