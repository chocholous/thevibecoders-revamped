# Implementation Guide

> "We're pioneers" - Let's build something that vibes

## Quick Start with Astro & Tailwind

### 1. Install Dependencies
```bash
# Create Astro project
npm create astro@latest the-vibe-coders -- --template minimal --typescript --tailwind

# Add React for interactive islands only
npx astro add react

# Add Airtable for CMS
npm install airtable

# Icons (optional)
npm install lucide-react
```

### 2. Configure Tailwind with Our Tokens

**tailwind.config.js**
```javascript
module.exports = {
  content: [
    './pages/**/*.{js,ts,jsx,tsx}',
    './components/**/*.{js,ts,jsx,tsx}',
  ],
  theme: {
    extend: {
      colors: {
        'vibe-purple': '#4A1D7F',
        'vibe-purple-dark': '#3A1060',
        'vibe-purple-light': '#5A2D8F',
        'vibe-teal': '#00D4D4',
        'vibe-teal-dark': '#00A8A8',
        'vibe-teal-light': '#40E4E4',
        'vibe-orange': '#FF6B35',
        'vibe-orange-dark': '#E55525',
        'vibe-orange-light': '#FF8555',
        'surface': '#5A2D8F',
        'surface-elevated': '#6A3D9F',
        'text-primary': '#FFFFFF',
        'text-secondary': '#D4C4E8',
        'text-tertiary': '#A890C8',
      },
      fontFamily: {
        sans: ['Inter', '-apple-system', 'BlinkMacSystemFont', 'sans-serif'],
        mono: ['JetBrains Mono', 'Fira Code', 'monospace'],
      },
      fontSize: {
        '5xl': '3.75rem',
        '4xl': '3rem',
        '3xl': '2.25rem',
        '2xl': '1.875rem',
      },
      spacing: {
        '18': '4.5rem',
        '88': '22rem',
        '128': '32rem',
      },
      boxShadow: {
        'glow-teal': '0 0 20px rgba(0, 212, 212, 0.3)',
        'glow-orange': '0 0 20px rgba(255, 107, 53, 0.3)',
      },
    },
  },
  plugins: [],
}
```

### 3. Global Styles

**styles/globals.css**
```css
@import 'tailwindcss/base';
@import 'tailwindcss/components';
@import 'tailwindcss/utilities';

/* Import our design tokens */
@import '../design-system/tokens.css';

@layer base {
  body {
    @apply bg-vibe-purple text-text-primary;
  }

  h1 {
    @apply text-5xl font-extrabold;
  }

  h2 {
    @apply text-3xl font-bold;
  }

  h3 {
    @apply text-xl font-semibold;
  }
}

@layer components {
  .btn-primary {
    @apply px-6 py-3 bg-vibe-orange text-white font-bold uppercase
           tracking-wider rounded-lg transition-all duration-250
           hover:bg-vibe-orange-dark hover:-translate-y-0.5
           hover:shadow-glow-orange;
  }

  .btn-secondary {
    @apply px-6 py-3 bg-transparent text-vibe-teal border-2
           border-vibe-teal font-semibold rounded-lg transition-all
           duration-250 hover:bg-vibe-teal hover:text-vibe-purple
           hover:shadow-glow-teal;
  }

  .card {
    @apply bg-surface p-6 rounded-lg border-2 border-transparent
           transition-all duration-250 hover:border-vibe-teal
           hover:-translate-y-1 hover:shadow-lg;
  }
}
```

## Component Examples

### Button Component (Astro)
**components/Button.astro**
```astro
---
export interface Props {
  variant?: 'primary' | 'secondary' | 'ghost';
  href?: string;
}

const { variant = 'primary', href } = Astro.props;

const variants = {
  primary: 'btn-primary',
  secondary: 'btn-secondary',
  ghost: 'bg-transparent text-white font-medium opacity-80 hover:opacity-100 hover:underline'
};

const className = `px-6 py-3 rounded-lg transition-all ${variants[variant]}`;
---

{href ? (
  <a href={href} class={className}>
    <slot />
  </a>
) : (
  <button class={className}>
    <slot />
  </button>
)}
```

### Event Card Component (Astro)
**components/EventCard.astro**
```astro
---
export interface Props {
  date: string;
  title: string;
  description: string;
  location: string;
  lumaLink: string;
  emoji?: string;
}

const { date, title, description, location, lumaLink, emoji = '🚀' } = Astro.props;
---

<article class="card">
  <span class="text-vibe-teal text-sm font-semibold uppercase tracking-wider">
    {date}
  </span>
  <h3 class="text-xl my-3">
    {title} {emoji}
  </h3>
  <p class="text-text-secondary mb-4">
    {description}
  </p>
  <div class="text-text-secondary mb-5">
    📍 {location}
  </div>
  <div class="flex gap-3">
    <a href={lumaLink} class="btn-primary" target="_blank" rel="noopener">
      RSVP on Luma
    </a>
  </div>
</article>
```

### Layout Component (Astro)
**layouts/Layout.astro**
```astro
---
import Navigation from '../components/Navigation.astro';
import Footer from '../components/Footer.astro';

export interface Props {
  title: string;
}

const { title } = Astro.props;
---

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
    <title>{title} | The Vibe Coders</title>
  </head>
  <body class="bg-vibe-purple text-text-primary">
    <div class="min-h-screen flex flex-col">
      <Navigation />
      <main class="flex-1">
        <slot />
      </main>
      <Footer />
    </div>
  </body>
</html>
```

## Page Templates

### Homepage (Astro + Airtable)
**pages/index.astro**
```astro
---
import Layout from '../layouts/Layout.astro';
import Button from '../components/Button.astro';
import EventCard from '../components/EventCard.astro';
import PostCard from '../components/PostCard.astro';
import { getPosts } from '../lib/airtable';

// Fetch posts from Airtable at build time
const posts = await getPosts();
---

<Layout title="Home">
  <!-- Hero Section -->
  <section class="py-32 text-center">
    <div class="container mx-auto px-4">
      <h1 class="mb-6 bg-gradient-to-r from-white to-vibe-teal
                 bg-clip-text text-transparent">
        The universe is the limit
      </h1>
      <p class="text-lg text-text-secondary max-w-2xl mx-auto mb-8">
        We command various AIs to craft apps, agents, webs, assets, toys—even businesses.
      </p>
      <div class="flex gap-4 justify-center flex-wrap">
        <Button variant="primary" href="/become-organizer">
          Start a Chapter
        </Button>
        <Button variant="secondary" href="/events">
          Explore Events
        </Button>
      </div>
    </div>
  </section>

  <!-- Activity Feed -->
  <section class="py-20">
    <div class="container mx-auto px-4">
      <h2 class="text-center mb-10">Community Activity</h2>
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {posts.map(post => (
          <PostCard {...post} />
        ))}
      </div>
    </div>
  </section>

  <!-- Luma Events Embed -->
  <section class="py-20">
    <div class="container mx-auto px-4">
      <h2 class="text-center mb-10">Upcoming Events</h2>
      <div class="luma-embed">
        <!-- Luma calendar widget will go here -->
        <iframe
          src="https://lu.ma/embed/calendar/cal-xxx/events"
          class="w-full h-96 rounded-lg"
        />
      </div>
    </div>
  </section>
</Layout>
```

## React Islands (When Needed)

For interactive components that require React, use Astro's island architecture:

### Example: Upload Form (React Island)
**components/UploadForm.jsx**
```jsx
import { useState } from 'react';

export function UploadForm() {
  const [uploading, setUploading] = useState(false);

  // This runs only on the client
  const handleSubmit = async (e) => {
    e.preventDefault();
    setUploading(true);
    // Upload to Airtable
  };

  return (
    <form onSubmit={handleSubmit}>
      {/* Interactive form logic */}
    </form>
  );
}
```

**Usage in Astro page:**
```astro
---
import UploadForm from '../components/UploadForm.jsx';
---

<!-- Only this component ships JavaScript -->
<UploadForm client:load />
```

### When to Use React Islands:
- Complex forms with validation
- Real-time features
- Image galleries with interactions
- Auth0 login flows

### When NOT to Use React:
- Static content
- Simple navigation
- Basic cards and layouts
- Anything that doesn't need interactivity

## Best Practices

### 1. Maintain Consistency
- Always use design tokens (never hardcode colors/spacing)
- Follow the component patterns documented
- Keep animations subtle (250ms transitions)

### 2. Dark Mode is Default
- Design everything for purple backgrounds first
- Ensure high contrast for accessibility
- Test all text on dark surfaces

### 3. Performance
- Use CSS over JS animations
- Lazy load images and non-critical components
- Keep bundle size minimal (< 100KB CSS)

### 4. Responsive Design
- Desktop-first approach
- Test on common breakpoints (768px, 1024px, 1280px)
- Ensure touch targets are 44px minimum on mobile

### 5. Typography
- Use Inter for everything except code
- JetBrains Mono for code blocks only
- Maximum 65ch width for body text

## Common Patterns

### Form Validation States
```jsx
// Success
<input className="border-green-500 focus:shadow-green-500/20" />

// Error
<input className="border-red-500 focus:shadow-red-500/20" />
<span className="text-red-400 text-sm mt-1">Email is required</span>
```

### Loading States
```jsx
// Skeleton loader
<div className="animate-pulse bg-surface rounded-lg h-32"></div>

// Spinner
<div className="animate-spin w-6 h-6 border-2 border-vibe-teal
                border-t-transparent rounded-full"></div>
```

### Empty States
```jsx
<div className="text-center py-12">
  <p className="text-2xl mb-2">No events yet</p>
  <p className="text-text-secondary">Check back soon for upcoming vibes!</p>
</div>
```

## Accessibility Checklist

- [ ] All interactive elements have focus states
- [ ] Color contrast meets WCAG AAA (7:1 ratio)
- [ ] Keyboard navigation works throughout
- [ ] Screen readers can understand all content
- [ ] Forms have proper labels and error messages
- [ ] Images have alt text
- [ ] Animations respect prefers-reduced-motion

## Development Workflow

1. **Start with mobile layout** (even though we're desktop-first)
2. **Build with semantic HTML** first
3. **Apply utility classes** for styling
4. **Extract to components** when patterns emerge
5. **Test on real devices** before shipping

## Testing the Vibe

Ask yourself:
- Does it feel playful but minimal?
- Is the purple universe prominent?
- Are CTAs orange and attention-grabbing?
- Does teal highlight the right elements?
- Is the copy self-aware and authentic?
- Would a pioneer use this?

## Need Help?

- Review `/design-system/examples/sample-page.html` for implementation
- Check individual documentation files for detailed specs
- Remember: "Last month is sooo history" - iterate quickly
- When in doubt, keep it simple (KISS principle)

## Philosophy
"We suffer—a lot—but we learn" - Implementation won't be perfect the first time. Ship it, learn from it, make it better. That's the vibe.