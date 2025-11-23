# Frontend Design & Development Skill

You are building the frontend for The Vibe Coders website using Astro. This skill ensures you write production-grade, performant, and maintainable code.

## Astro Development Principles

### Core Philosophy
- **Zero JS by default** - Only add JavaScript where absolutely necessary
- **Build-time over runtime** - Compute everything possible at build time
- **HTML-first** - Semantic, accessible HTML before any framework
- **Progressive enhancement** - Site works without JS, enhanced with it

### File Structure & Naming
```
src/
├── pages/              # Routes (.astro files)
│   ├── index.astro    # Homepage
│   ├── events.astro   # Events listing
│   └── about.astro    # About page
├── components/         # Reusable components
│   ├── EventCard.astro
│   ├── Header.astro
│   └── islands/       # Interactive components
│       └── ApplicationForm.tsx
├── layouts/           # Page templates
│   └── BaseLayout.astro
├── styles/            # Global styles
│   └── global.css
└── lib/               # Utilities
    └── airtable.ts    # Data fetching
```

### Component Guidelines

#### Static Astro Components (.astro)
```astro
---
// Props interface
export interface Props {
  title: string;
  description?: string;
  image: string;
}

// Destructure props with defaults
const {
  title,
  description = '',
  image
} = Astro.props;

// Build-time data fetching
const data = await fetch('...').then(r => r.json());
---

<article class="event-card">
  <img src={image} alt="" loading="lazy">
  <h3>{title}</h3>
  {description && <p>{description}</p>}
</article>

<style>
  .event-card {
    /* Scoped styles - only affect this component */
    background: var(--color-surface);
    border-radius: 8px;
  }
</style>
```

#### Interactive Islands (React/Preact)
```tsx
// Only for truly interactive features
import { useState } from 'react';

export default function ApplicationForm() {
  const [email, setEmail] = useState('');

  // Minimal, focused interactivity
  return (
    <form>
      {/* Form logic here */}
    </form>
  );
}
```

Use in Astro:
```astro
---
import ApplicationForm from '../components/islands/ApplicationForm.tsx';
---

<!-- Only loads JS when visible -->
<ApplicationForm client:visible />
```

### Styling Approach

#### Global Styles (Tailwind + Custom Properties)
```css
/* src/styles/global.css */
:root {
  /* Vibe Coders brand colors */
  --color-vibe-purple: #6B46C1;
  --color-vibe-teal: #14B8A6;
  --color-vibe-orange: #FB923C;

  /* Semantic colors */
  --color-background: #0A0A0A;
  --color-surface: #1A1A1A;
  --color-text: #E5E5E5;

  /* Typography */
  --font-display: 'Inter', system-ui, sans-serif;
  --font-body: 'Inter', system-ui, sans-serif;
}
```

#### Component Styles
- Use Tailwind classes for utilities
- Use CSS custom properties for theming
- Scope complex styles to components
- Never use CSS-in-JS

### Data Fetching Patterns

#### Build-Time (Preferred)
```astro
---
// In .astro component or page
import { getEvents } from '../lib/airtable';

// Runs once at build time
const events = await getEvents();
---

<!-- Use the data -->
{events.map(event => <EventCard {...event} />)}
```

#### Dynamic Routes
```astro
---
// src/pages/city/[city].astro
export async function getStaticPaths() {
  const cities = await getCities();

  return cities.map(city => ({
    params: { city: city.slug },
    props: { city }
  }));
}

const { city } = Astro.props;
---

<h1>Events in {city.name}</h1>
```

### Performance Checklist

#### Images
- [ ] Use Astro's Image component
- [ ] Set explicit width/height
- [ ] Use lazy loading for below-fold
- [ ] Optimize with `format` and `quality`
- [ ] Serve WebP with fallbacks

```astro
---
import { Image } from 'astro:assets';
import eventPhoto from '../images/event.jpg';
---

<Image
  src={eventPhoto}
  alt="Community event"
  width={800}
  height={450}
  format="webp"
  loading="lazy"
/>
```

#### Fonts
- [ ] Use `font-display: swap`
- [ ] Preload critical fonts
- [ ] Subset fonts for needed characters
- [ ] Use system fonts as fallbacks

```html
<!-- In BaseLayout.astro -->
<link
  rel="preload"
  href="/fonts/inter.woff2"
  as="font"
  type="font/woff2"
  crossorigin
>
```

#### Critical CSS
- [ ] Inline critical CSS in <head>
- [ ] Defer non-critical styles
- [ ] Minimize CSS size (< 14KB inline)

### Accessibility Requirements

#### Semantic HTML
```astro
<!-- Good -->
<nav aria-label="Main">
  <ul>
    <li><a href="/">Home</a></li>
  </ul>
</nav>

<!-- Bad -->
<div class="nav">
  <div class="nav-item">Home</div>
</div>
```

#### ARIA When Needed
```astro
<button
  aria-expanded={isOpen}
  aria-controls="menu"
  aria-label="Toggle menu"
>
  <svg><!-- Icon --></svg>
</button>
```

#### Focus Management
```css
/* Always visible focus indicators */
:focus-visible {
  outline: 2px solid var(--color-vibe-teal);
  outline-offset: 2px;
}
```

### Mobile-First Responsive

```astro
<!-- Use Tailwind's responsive utilities -->
<div class="
  grid
  grid-cols-1
  md:grid-cols-2
  lg:grid-cols-3
  gap-4
  md:gap-6
">
  <!-- Content -->
</div>
```

### Testing & Preview

#### Development Workflow
```bash
# Start dev server
npm run dev

# Preview production build
npm run build && npm run preview

# Capture DOM + screenshots for review
npm run preview:capture
npm run preview:view
```

#### Visual Testing with Cypress
- Captures are configured in `cypress/preview/capture.cy.js`
- Screenshots saved to `cypress/screenshots/`
- DOM analysis in `cypress/preview/output/`
- View results in generated `preview.html`

### Common Patterns

#### Event Card
```astro
---
export interface Props {
  title: string;
  date: Date;
  city: string;
  image: string;
  lumaUrl: string;
}

const { title, date, city, image, lumaUrl } = Astro.props;

const formattedDate = new Intl.DateTimeFormat('en-US', {
  month: 'short',
  day: 'numeric'
}).format(date);

const isNew = Date.now() - date.getTime() < 3 * 24 * 60 * 60 * 1000;
---

<article class="event-card group">
  <a href={lumaUrl} target="_blank" rel="noopener">
    <div class="relative overflow-hidden rounded-lg">
      <img
        src={image}
        alt=""
        class="w-full h-48 object-cover transition-transform group-hover:scale-105"
        loading="lazy"
      >
      {isNew && (
        <span class="absolute top-2 right-2 bg-vibe-orange text-white px-2 py-1 text-sm rounded">
          New
        </span>
      )}
    </div>
    <div class="mt-3">
      <div class="flex items-center gap-2 text-sm text-gray-400">
        <span>{city}</span>
        <span>•</span>
        <span>{formattedDate}</span>
      </div>
      <h3 class="mt-1 font-semibold text-white">
        {title}
      </h3>
    </div>
  </a>
</article>
```

#### Loading States (Islands Only)
```tsx
// For interactive components
import { useState, useEffect } from 'react';

export default function DynamicContent() {
  const [loading, setLoading] = useState(true);
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch('/api/data')
      .then(r => r.json())
      .then(d => {
        setData(d);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <div className="animate-pulse">Loading...</div>;
  }

  return <div>{/* Content */}</div>;
}
```

### Animation Guidelines

#### CSS Transitions (Preferred)
```css
.card {
  transition: transform 200ms ease-out;
}

.card:hover {
  transform: translateY(-2px);
}
```

#### Framer Motion (Only for complex animations)
```tsx
// Only in islands, only when necessary
import { motion } from 'framer-motion';

<motion.div
  initial={{ opacity: 0 }}
  animate={{ opacity: 1 }}
  transition={{ duration: 0.2 }}
>
  {/* Content */}
</motion.div>
```

### Form Handling

#### Airtable Form Submission
```astro
---
// In API route: src/pages/api/apply.ts
export async function post({ request }) {
  const data = await request.formData();

  // Submit to Airtable
  const response = await fetch(`https://api.airtable.com/v0/${BASE_ID}/Applications`, {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${AIRTABLE_TOKEN}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      fields: {
        Name: data.get('name'),
        City: data.get('city'),
        // ...
      }
    })
  });

  return new Response(JSON.stringify({ success: true }));
}
---
```

### Error Boundaries

```astro
---
// Graceful error handling
let events = [];
let error = null;

try {
  events = await getEvents();
} catch (e) {
  error = e.message;
  console.error('Failed to load events:', e);
}
---

{error ? (
  <div class="error-message">
    Unable to load events. Please try again later.
  </div>
) : (
  <div>{/* Show events */}</div>
)}
```

### Build & Deploy

#### Environment Variables
```env
# .env.local
AIRTABLE_API_KEY=your_key_here
AIRTABLE_BASE_ID=your_base_id
AUTH0_DOMAIN=your_domain
AUTH0_CLIENT_ID=your_client_id
```

#### Deployment Checklist
- [ ] Run `npm run build` locally
- [ ] Check build output size (< 500KB JS)
- [ ] Test all routes with `npm run preview`
- [ ] Verify environment variables in hosting
- [ ] Set up proper caching headers
- [ ] Enable CDN/edge caching

### Performance Targets
- **First Contentful Paint**: < 1.5s
- **Largest Contentful Paint**: < 2.5s
- **Time to Interactive**: < 3.5s
- **Cumulative Layout Shift**: < 0.1
- **JavaScript bundle**: < 50KB (gzipped)

### Anti-Patterns to Avoid
- ❌ Using React for static content
- ❌ Client-side data fetching for initial load
- ❌ Importing entire icon libraries
- ❌ Using CSS-in-JS libraries
- ❌ Complex state management (Redux, MobX)
- ❌ Building custom form validation
- ❌ Creating unnecessary abstractions
- ❌ Over-optimizing before measuring

### Quick Reference

#### When to use what:
- **Astro components**: Everything by default
- **React islands**: Forms, real-time features only
- **API routes**: Form submissions, auth callbacks
- **Static assets**: Images, fonts, downloads
- **CDN**: All static assets and built pages

#### Component Decision Tree:
1. Is it interactive? → No → Use .astro
2. Is interaction simple? → Yes → Use .astro with vanilla JS
3. Does it need state? → Yes → Use React island with client:visible
4. Is it critical? → Yes → Use client:load instead

Remember: Ship HTML, enhance with JS. The best JavaScript is often no JavaScript.