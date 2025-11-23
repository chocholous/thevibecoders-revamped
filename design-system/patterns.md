# Layout Patterns

> "Vibe coding happens IRL" - Layouts that bring the community together

## Page Structure

### Base Layout
```html
<body class="vibe-app">
  <header class="site-header">
    <!-- Navigation -->
  </header>

  <main class="site-main">
    <!-- Page content -->
  </main>

  <footer class="site-footer">
    <!-- Footer content -->
  </footer>
</body>
```

```css
.vibe-app {
  min-height: 100vh;
  background: var(--color-vibe-purple);
  color: var(--color-text-primary);
  font-family: var(--font-family-base);
  display: flex;
  flex-direction: column;
}

.site-main {
  flex: 1;
  width: 100%;
}

.site-header {
  position: sticky;
  top: 0;
  z-index: var(--z-sticky);
  backdrop-filter: blur(10px);
  background: rgba(74, 29, 127, 0.9);
}
```

### Container System
```css
.container {
  width: 100%;
  max-width: var(--container-xl);
  margin: 0 auto;
  padding: 0 var(--space-4);
}

@media (min-width: 768px) {
  .container {
    padding: 0 var(--space-8);
  }
}

/* Variants */
.container--sm { max-width: var(--container-sm); }
.container--md { max-width: var(--container-md); }
.container--lg { max-width: var(--container-lg); }
.container--full { max-width: 100%; }
```

## Hero Patterns

### Classic Hero
```html
<section class="hero">
  <div class="container">
    <h1 class="hero-title">The universe is the limit</h1>
    <p class="hero-lead">
      Different roles, experiences, backgrounds—and we vibe.
    </p>
    <div class="hero-actions">
      <button class="btn-primary">Join the Vibe</button>
      <button class="btn-secondary">Explore Events</button>
    </div>
  </div>
</section>
```

```css
.hero {
  padding: var(--space-32) 0;
  text-align: center;
  position: relative;
  overflow: hidden;
}

.hero-title {
  font-size: var(--font-size-5xl);
  font-weight: var(--font-weight-extrabold);
  margin-bottom: var(--space-6);
  background: linear-gradient(135deg, white, var(--color-vibe-teal));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.hero-lead {
  font-size: var(--font-size-lg);
  color: var(--color-text-secondary);
  max-width: 600px;
  margin: 0 auto var(--space-8);
}

.hero-actions {
  display: flex;
  gap: var(--space-4);
  justify-content: center;
  flex-wrap: wrap;
}
```

### Split Hero
```html
<section class="hero-split">
  <div class="hero-split__content">
    <h1>We're pioneers</h1>
    <p>The tools we use don't have docs yet. We figure it out.</p>
    <button class="btn-primary">Start Exploring</button>
  </div>
  <div class="hero-split__visual">
    <!-- Code editor mockup or illustration -->
  </div>
</section>
```

```css
.hero-split {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: var(--space-12);
  align-items: center;
  padding: var(--space-20) var(--space-8);
}

@media (max-width: 768px) {
  .hero-split {
    grid-template-columns: 1fr;
  }
}
```

## Content Layouts

### Event Grid
```html
<section class="events-section">
  <div class="container">
    <header class="section-header">
      <h2>Upcoming Vibes</h2>
      <p>IRL events where magic happens</p>
    </header>
    <div class="events-grid">
      <!-- Event cards -->
    </div>
  </div>
</section>
```

```css
.events-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: var(--space-6);
  margin-top: var(--space-8);
}

.section-header {
  text-align: center;
  margin-bottom: var(--space-10);
}

.section-header h2 {
  font-size: var(--font-size-3xl);
  margin-bottom: var(--space-4);
}

.section-header p {
  color: var(--color-text-secondary);
  font-size: var(--font-size-lg);
}
```

### Activity Feed
```html
<section class="feed-layout">
  <aside class="feed-sidebar">
    <!-- Filters, tags -->
  </aside>
  <main class="feed-content">
    <!-- Activity items -->
  </main>
</section>
```

```css
.feed-layout {
  display: grid;
  grid-template-columns: 280px 1fr;
  gap: var(--space-8);
  max-width: var(--container-xl);
  margin: 0 auto;
  padding: var(--space-8);
}

@media (max-width: 768px) {
  .feed-layout {
    grid-template-columns: 1fr;
  }

  .feed-sidebar {
    order: 2;
  }
}

.feed-content {
  background: var(--color-surface);
  border-radius: var(--radius-lg);
  overflow: hidden;
}
```

### City Showcase
```html
<section class="cities-section">
  <div class="container">
    <h2>Where We Vibe</h2>
    <div class="cities-grid">
      <div class="city-card">
        <span class="city-flag">🇬🇧</span>
        <h3>London</h3>
        <p>23 members</p>
      </div>
      <!-- More cities -->
    </div>
  </div>
</section>
```

```css
.cities-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: var(--space-4);
}

.city-card {
  background: var(--color-surface);
  padding: var(--space-6);
  border-radius: var(--radius-lg);
  text-align: center;
  transition: all var(--duration-base) var(--ease-out);
  cursor: pointer;
}

.city-card:hover {
  transform: translateY(-4px);
  border: 2px solid var(--color-vibe-teal);
}

.city-flag {
  font-size: 3rem;
  display: block;
  margin-bottom: var(--space-4);
}
```

## Form Layouts

### Application Form
```html
<form class="application-form">
  <div class="form-section">
    <h3>About You</h3>
    <div class="form-grid">
      <div class="form-field">
        <!-- Name input -->
      </div>
      <div class="form-field">
        <!-- Email input -->
      </div>
    </div>
  </div>

  <div class="form-section">
    <h3>Your Vibe</h3>
    <!-- Text areas, selects -->
  </div>

  <div class="form-actions">
    <button type="submit" class="btn-primary">Submit Application</button>
  </div>
</form>
```

```css
.application-form {
  max-width: var(--container-md);
  margin: 0 auto;
  background: var(--color-surface);
  padding: var(--space-8);
  border-radius: var(--radius-lg);
}

.form-section {
  margin-bottom: var(--space-8);
}

.form-section h3 {
  margin-bottom: var(--space-5);
  color: var(--color-vibe-teal);
}

.form-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: var(--space-5);
}

.form-actions {
  padding-top: var(--space-6);
  border-top: 1px solid var(--color-surface-elevated);
  display: flex;
  justify-content: flex-end;
  gap: var(--space-4);
}
```

## Special Patterns

### Manifesto Display
```html
<section class="manifesto">
  <div class="container container--md">
    <div class="manifesto-window">
      <div class="window-controls">
        <span class="dot dot--red"></span>
        <span class="dot dot--yellow"></span>
        <span class="dot dot--green"></span>
      </div>
      <div class="manifesto-content">
        <!-- Manifesto items as code comments -->
      </div>
    </div>
  </div>
</section>
```

```css
.manifesto-window {
  background: var(--color-code-bg);
  border-radius: var(--radius-lg);
  overflow: hidden;
  box-shadow: var(--shadow-xl);
}

.window-controls {
  padding: var(--space-3) var(--space-4);
  background: #2D2D30;
  display: flex;
  gap: var(--space-2);
}

.dot {
  width: 12px;
  height: 12px;
  border-radius: 50%;
}

.dot--red { background: #FF5F57; }
.dot--yellow { background: #FFBD2E; }
.dot--green { background: #28CA42; }
```

### Stats Dashboard
```html
<section class="stats">
  <div class="container">
    <div class="stats-grid">
      <div class="stat-card">
        <span class="stat-value">9</span>
        <span class="stat-label">Active Cities</span>
      </div>
      <div class="stat-card">
        <span class="stat-value">100+</span>
        <span class="stat-label">Vibing Members</span>
      </div>
      <div class="stat-card">
        <span class="stat-value">∞</span>
        <span class="stat-label">Ideas Explored</span>
      </div>
    </div>
  </div>
</section>
```

```css
.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: var(--space-6);
  text-align: center;
}

.stat-card {
  padding: var(--space-8) var(--space-6);
}

.stat-value {
  display: block;
  font-size: var(--font-size-4xl);
  font-weight: var(--font-weight-extrabold);
  color: var(--color-vibe-teal);
  margin-bottom: var(--space-2);
}

.stat-label {
  font-size: var(--font-size-sm);
  text-transform: uppercase;
  letter-spacing: var(--letter-spacing-wider);
  color: var(--color-text-secondary);
}
```

## Footer Pattern
```html
<footer class="site-footer">
  <div class="container">
    <div class="footer-top">
      <div class="footer-brand">
        <h3>The Vibe Coders</h3>
        <p>The universe is the limit</p>
      </div>
      <nav class="footer-nav">
        <div class="footer-column">
          <h4>Community</h4>
          <ul>
            <li><a href="#">Events</a></li>
            <li><a href="#">Cities</a></li>
            <li><a href="#">Manifesto</a></li>
          </ul>
        </div>
        <!-- More columns -->
      </nav>
    </div>
    <div class="footer-bottom">
      <p>© 2024 The Vibe Coders. We don't sell our souls.</p>
      <div class="footer-social">
        <!-- Social links -->
      </div>
    </div>
  </div>
</footer>
```

```css
.site-footer {
  margin-top: var(--space-20);
  padding: var(--space-12) 0 var(--space-8);
  background: var(--color-vibe-purple-dark);
  border-top: 1px solid var(--color-surface);
}

.footer-top {
  display: grid;
  grid-template-columns: 1fr 2fr;
  gap: var(--space-12);
  margin-bottom: var(--space-8);
}

.footer-nav {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: var(--space-8);
}

.footer-bottom {
  padding-top: var(--space-6);
  border-top: 1px solid var(--color-surface);
  display: flex;
  justify-content: space-between;
  align-items: center;
}

@media (max-width: 768px) {
  .footer-top {
    grid-template-columns: 1fr;
  }

  .footer-bottom {
    flex-direction: column;
    text-align: center;
    gap: var(--space-4);
  }
}
```

## Responsive Patterns

### Mobile Navigation
```css
@media (max-width: 768px) {
  .nav-menu {
    position: fixed;
    top: 0;
    left: -100%;
    width: 80%;
    height: 100vh;
    background: var(--color-surface);
    flex-direction: column;
    padding: var(--space-8) var(--space-6);
    transition: left var(--duration-base) var(--ease-out);
  }

  .nav-menu.active {
    left: 0;
  }

  .nav-overlay {
    position: fixed;
    inset: 0;
    background: rgba(0, 0, 0, 0.5);
    display: none;
  }

  .nav-overlay.active {
    display: block;
  }
}
```

### Responsive Tables
```css
@media (max-width: 768px) {
  .responsive-table {
    display: block;
  }

  .responsive-table thead {
    display: none;
  }

  .responsive-table tr {
    display: block;
    margin-bottom: var(--space-4);
    background: var(--color-surface);
    padding: var(--space-4);
    border-radius: var(--radius-md);
  }

  .responsive-table td {
    display: block;
    text-align: right;
    padding: var(--space-2);
  }

  .responsive-table td:before {
    content: attr(data-label);
    float: left;
    font-weight: var(--font-weight-semibold);
    color: var(--color-text-secondary);
  }
}
```

## Pattern Philosophy

1. **Desktop-first**: We code on desktops, optimize there first
2. **Content-driven**: Layout serves content, not vice versa
3. **Flexible grids**: Use CSS Grid and auto-fit for responsive magic
4. **Consistent spacing**: Stick to the spacing system religiously
5. **Performance**: Minimize layout shifts, optimize reflows

## Layout Don'ts

- ❌ Don't use floats (it's not 2010)
- ❌ Don't forget container max-widths (readability matters)
- ❌ Don't use fixed heights (content should flow)
- ❌ Don't forget touch targets on mobile (44px minimum)
- ❌ Don't overcomplicate (KISS principle always)

## Philosophy
"Different roles, experiences, backgrounds—and we vibe" - Our layouts bring diverse content together in harmony. Flexible, inclusive, and always ready for what's next.