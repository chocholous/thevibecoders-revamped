# The Vibe Coders - Project Plan

## Current Sprint: Foundation (Sprint 1)

### In Progress
- [ ] **TASK-001**: Define design system tokens and create design-system.md

### Ready
- [ ] **TASK-002**: Initialize Next.js project with TypeScript
- [ ] **TASK-003**: Configure Tailwind CSS with custom tokens
- [ ] **TASK-004**: Set up shadcn/ui components
- [ ] **TASK-005**: Create base layout component
- [ ] **TASK-006**: Build responsive navigation component
- [ ] **TASK-007**: Create hero section for home page
- [ ] **TASK-008**: Document component hierarchy in components.md

### Completed
✅ Project structure created
✅ PRD.md documented
✅ Initial planning setup

---

## Sprint 2: Feed & Events

### Backlog
- [ ] **TASK-009**: Design event card component
- [ ] **TASK-010**: Create organizer post card component
- [ ] **TASK-011**: Build feed layout with card grid
- [ ] **TASK-012**: Research Luma API/embed options
- [ ] **TASK-013**: Create events listing page
- [ ] **TASK-014**: Implement upcoming events section
- [ ] **TASK-015**: Add past events archive
- [ ] **TASK-016**: Set up image optimization pipeline

---

## Sprint 3: Organizer Features

### Backlog
- [ ] **TASK-017**: Design organizer application form
- [ ] **TASK-018**: Set up form submission handling
- [ ] **TASK-019**: Create organizer upload interface
- [ ] **TASK-020**: Implement basic auth for organizers
- [ ] **TASK-021**: Build image upload functionality
- [ ] **TASK-022**: Connect upload to feed display
- [ ] **TASK-023**: Add form validation and error handling
- [ ] **TASK-024**: Set up email notifications

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

### Decided
- Project structure: Next.js App Router approach
- Styling: Tailwind CSS + shadcn/ui
- Project management: PLAN.md + MADRs for major decisions

### Pending
- [ ] Image hosting solution (Cloudinary vs S3 vs Vercel Blob)
- [ ] Form backend (Formspree vs custom vs Airtable)
- [ ] Auth provider (Clerk vs NextAuth vs passwordless)
- [ ] Hosting platform (Vercel vs Netlify)
- [ ] Luma integration approach (embed vs API)

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