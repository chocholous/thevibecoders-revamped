# Component Patterns

> "We're pioneers" - Components that work today, ready to evolve tomorrow

## Design Principles

1. **Minimal by default** - Start simple, add complexity only when needed
2. **Dark-first** - Designed for our purple universe
3. **Accessible always** - Everyone can vibe
4. **Responsive naturally** - Desktop-first, mobile-ready

## Core Components

### Buttons

#### Primary CTA
```css
.btn-primary {
  background: var(--color-vibe-orange);
  color: white;
  padding: var(--space-3) var(--space-6);
  border: none;
  border-radius: var(--radius-md);
  font-weight: var(--font-weight-bold);
  font-size: var(--font-size-base);
  letter-spacing: var(--letter-spacing-wide);
  text-transform: uppercase;
  cursor: pointer;
  transition: all var(--duration-base) var(--ease-out);
}

.btn-primary:hover {
  background: var(--color-vibe-orange-dark);
  transform: translateY(-2px);
  box-shadow: var(--shadow-glow-orange);
}
```

#### Secondary Button
```css
.btn-secondary {
  background: transparent;
  color: var(--color-vibe-teal);
  padding: var(--space-3) var(--space-6);
  border: 2px solid var(--color-vibe-teal);
  border-radius: var(--radius-md);
  font-weight: var(--font-weight-semibold);
  transition: all var(--duration-base) var(--ease-out);
}

.btn-secondary:hover {
  background: var(--color-vibe-teal);
  color: var(--color-vibe-purple);
  box-shadow: var(--shadow-glow-teal);
}
```

#### Ghost Button
```css
.btn-ghost {
  background: transparent;
  color: var(--color-text-primary);
  padding: var(--space-3) var(--space-4);
  border: none;
  font-weight: var(--font-weight-medium);
  opacity: 0.8;
  transition: opacity var(--duration-fast) var(--ease-out);
}

.btn-ghost:hover {
  opacity: 1;
  text-decoration: underline;
}
```

### Cards

#### Event Card
```html
<article class="event-card">
  <span class="event-date">Nov 23 • 6PM PT</span>
  <h3 class="event-title">AI Tools Showcase 🚀</h3>
  <p class="event-description">
    Show off your latest experiments. We suffer—but we learn!
  </p>
  <div class="event-location">
    📍 Portland, OR
  </div>
  <div class="event-actions">
    <button class="btn-primary">RSVP</button>
    <button class="btn-ghost">Learn More</button>
  </div>
</article>
```

```css
.event-card {
  background: var(--color-surface);
  padding: var(--space-6);
  border-radius: var(--radius-lg);
  border: 2px solid transparent;
  transition: all var(--duration-base) var(--ease-out);
}

.event-card:hover {
  border-color: var(--color-vibe-teal);
  transform: translateY(-4px);
  box-shadow: var(--shadow-lg);
}

.event-date {
  color: var(--color-vibe-teal);
  font-size: var(--font-size-sm);
  font-weight: var(--font-weight-semibold);
  text-transform: uppercase;
  letter-spacing: var(--letter-spacing-wide);
}

.event-title {
  margin: var(--space-3) 0;
  font-size: var(--font-size-xl);
  color: var(--color-text-primary);
}

.event-location {
  color: var(--color-text-secondary);
  margin-top: var(--space-4);
}

.event-actions {
  display: flex;
  gap: var(--space-3);
  margin-top: var(--space-5);
}
```

#### Organizer Card
```html
<article class="organizer-card">
  <div class="organizer-avatar">JD</div>
  <h3 class="organizer-name">Jane Doe</h3>
  <p class="organizer-role">Portland Chapter Lead</p>
  <p class="organizer-bio">
    Building AI tools by day, vibing by night.
  </p>
</article>
```

```css
.organizer-card {
  background: var(--color-surface-elevated);
  padding: var(--space-6);
  border-radius: var(--radius-lg);
  text-align: center;
}

.organizer-avatar {
  width: 80px;
  height: 80px;
  margin: 0 auto var(--space-4);
  background: linear-gradient(135deg, var(--color-vibe-teal), var(--color-vibe-orange));
  border-radius: var(--radius-full);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: var(--font-size-2xl);
  font-weight: var(--font-weight-bold);
  color: white;
}
```

### Forms

#### Input Field
```html
<div class="form-field">
  <label class="form-label">Your Email</label>
  <input type="email" class="input" placeholder="pioneer@vibecoders.com">
  <span class="form-help">We don't spam. We vibe.</span>
</div>
```

```css
.input {
  width: 100%;
  padding: var(--space-3) var(--space-4);
  background: var(--color-surface);
  border: 2px solid var(--color-surface-elevated);
  border-radius: var(--radius-md);
  color: var(--color-text-primary);
  font-size: var(--font-size-base);
  transition: all var(--duration-fast) var(--ease-out);
}

.input:focus {
  outline: none;
  border-color: var(--color-vibe-teal);
  box-shadow: var(--shadow-glow-teal);
}

.input::placeholder {
  color: var(--color-text-tertiary);
}

.form-label {
  display: block;
  margin-bottom: var(--space-2);
  font-weight: var(--font-weight-semibold);
  color: var(--color-text-primary);
}

.form-help {
  display: block;
  margin-top: var(--space-2);
  font-size: var(--font-size-sm);
  color: var(--color-text-secondary);
}
```

#### Select Dropdown
```css
.select {
  width: 100%;
  padding: var(--space-3) var(--space-4);
  background: var(--color-surface);
  border: 2px solid var(--color-surface-elevated);
  border-radius: var(--radius-md);
  color: var(--color-text-primary);
  appearance: none;
  background-image: url("data:image/svg+xml,..."); /* Chevron down */
  background-repeat: no-repeat;
  background-position: right var(--space-3) center;
}
```

### Navigation

#### Header Nav
```html
<nav class="nav-header">
  <div class="nav-brand">
    <span class="nav-logo">The Vibe Coders</span>
  </div>
  <ul class="nav-menu">
    <li><a href="#events" class="nav-link">Events</a></li>
    <li><a href="#about" class="nav-link">About</a></li>
    <li><a href="#join" class="nav-link nav-link--cta">Join Us</a></li>
  </ul>
</nav>
```

```css
.nav-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: var(--space-4) var(--space-8);
  background: var(--color-background);
}

.nav-menu {
  display: flex;
  gap: var(--space-6);
  list-style: none;
  margin: 0;
  padding: 0;
}

.nav-link {
  color: var(--color-text-primary);
  text-decoration: none;
  font-weight: var(--font-weight-medium);
  transition: color var(--duration-fast) var(--ease-out);
}

.nav-link:hover {
  color: var(--color-vibe-teal);
}

.nav-link--cta {
  padding: var(--space-2) var(--space-4);
  background: var(--color-vibe-orange);
  border-radius: var(--radius-md);
  color: white;
}

.nav-link--cta:hover {
  background: var(--color-vibe-orange-dark);
  color: white;
}
```

### Badges & Tags

#### City Badge
```html
<span class="badge badge--city">🇬🇧 London</span>
```

```css
.badge {
  display: inline-block;
  padding: var(--space-1) var(--space-3);
  border-radius: var(--radius-full);
  font-size: var(--font-size-sm);
  font-weight: var(--font-weight-semibold);
  background: var(--color-surface);
  color: var(--color-text-primary);
}

.badge--city {
  background: var(--color-surface-elevated);
  border: 1px solid var(--color-vibe-teal);
}
```

#### Status Tag
```css
.tag {
  display: inline-block;
  padding: var(--space-1) var(--space-2);
  border-radius: var(--radius-sm);
  font-size: var(--font-size-xs);
  font-weight: var(--font-weight-medium);
  text-transform: uppercase;
  letter-spacing: var(--letter-spacing-wide);
}

.tag--new {
  background: var(--color-vibe-teal);
  color: var(--color-vibe-purple);
}

.tag--soon {
  background: var(--color-vibe-orange);
  color: white;
}
```

### Special Components

#### Manifesto Block (VS Code Style)
```html
<div class="manifesto-block">
  <div class="manifesto-header">
    <span class="file-name">.vibe-manifesto</span>
    <span class="file-lang">gitignore</span>
  </div>
  <pre class="manifesto-content">
    <code>
# The Vibe Coders Manifesto

# 1. The universe is the limit
# Not just the sky. We think bigger.

# 2. We suffer—a lot—but we learn
# Every bug is a lesson.
    </code>
  </pre>
</div>
```

```css
.manifesto-block {
  background: var(--color-code-bg);
  border-radius: var(--radius-md);
  overflow: hidden;
  font-family: var(--font-family-mono);
}

.manifesto-header {
  display: flex;
  justify-content: space-between;
  padding: var(--space-2) var(--space-4);
  background: #2D2D30;
  border-bottom: 1px solid #3E3E42;
  font-size: var(--font-size-sm);
}

.manifesto-content {
  padding: var(--space-4);
  margin: 0;
  color: var(--color-code-comment);
  line-height: var(--line-height-relaxed);
}
```

#### Activity Feed Item
```html
<article class="activity-item">
  <div class="activity-meta">
    <span class="activity-author">Sarah Chen</span>
    <span class="activity-date">2 hours ago</span>
  </div>
  <p class="activity-content">
    Just shipped a new AI agent that writes its own documentation.
    It's terrible at it, but it's learning! 😅
  </p>
  <div class="activity-reactions">
    <button class="reaction">🚀 12</button>
    <button class="reaction">❤️ 8</button>
  </div>
</article>
```

```css
.activity-item {
  padding: var(--space-5);
  border-bottom: 1px solid var(--color-surface);
}

.activity-meta {
  display: flex;
  justify-content: space-between;
  margin-bottom: var(--space-3);
  font-size: var(--font-size-sm);
}

.activity-author {
  color: var(--color-vibe-teal);
  font-weight: var(--font-weight-semibold);
}

.activity-date {
  color: var(--color-text-tertiary);
}

.reaction {
  background: var(--color-surface);
  border: none;
  padding: var(--space-1) var(--space-3);
  border-radius: var(--radius-full);
  margin-right: var(--space-2);
  cursor: pointer;
  transition: all var(--duration-fast) var(--ease-out);
}

.reaction:hover {
  background: var(--color-surface-elevated);
  transform: scale(1.05);
}
```

## Animation Guidelines

Keep animations subtle and purposeful:

```css
/* Standard transitions */
.interactive-element {
  transition: all var(--duration-base) var(--ease-out);
}

/* Hover lift */
.card:hover {
  transform: translateY(-4px);
}

/* Glow effects */
.glow-on-hover:hover {
  box-shadow: var(--shadow-glow-teal);
}

/* Micro-interactions */
@keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.7; }
}

.pulse {
  animation: pulse 2s infinite;
}
```

## Component Don'ts

- ❌ Don't over-animate (subtle > flashy)
- ❌ Don't forget focus states (accessibility)
- ❌ Don't use pure white on purple (use --color-text-primary)
- ❌ Don't make components too complex (KISS)
- ❌ Don't forget mobile touch targets (min 44px)

## Philosophy
"We don't sell our souls" - Every component should feel authentic to our vibe. No corporate polish, no fake enthusiasm. Real connections, real design.