# Implementation Guide

> "We're pioneers" - Let's build something that vibes

## Quick Start with Next.js & Tailwind

### 1. Install Dependencies
```bash
npm install -D tailwindcss @tailwindcss/forms @tailwindcss/typography
npm install next react react-dom
npm install lucide-react  # For icons
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

### Button Component
**components/Button.jsx**
```jsx
export function Button({ variant = 'primary', children, ...props }) {
  const variants = {
    primary: 'btn-primary',
    secondary: 'btn-secondary',
    ghost: 'bg-transparent text-white font-medium opacity-80 hover:opacity-100 hover:underline'
  }

  return (
    <button
      className={`px-6 py-3 rounded-lg transition-all ${variants[variant]}`}
      {...props}
    >
      {children}
    </button>
  )
}
```

### Event Card Component
**components/EventCard.jsx**
```jsx
export function EventCard({ date, title, description, location, emoji = '🚀' }) {
  return (
    <article className="card">
      <span className="text-vibe-teal text-sm font-semibold uppercase tracking-wider">
        {date}
      </span>
      <h3 className="text-xl my-3">
        {title} {emoji}
      </h3>
      <p className="text-text-secondary mb-4">
        {description}
      </p>
      <div className="text-text-secondary mb-5">
        📍 {location}
      </div>
      <div className="flex gap-3">
        <Button variant="primary">RSVP</Button>
        <Button variant="ghost">Learn More</Button>
      </div>
    </article>
  )
}
```

### Layout Component
**components/Layout.jsx**
```jsx
export function Layout({ children }) {
  return (
    <div className="min-h-screen flex flex-col">
      <Navigation />
      <main className="flex-1">
        {children}
      </main>
      <Footer />
    </div>
  )
}
```

## Page Templates

### Homepage
**pages/index.jsx**
```jsx
import { Layout } from '../components/Layout'
import { Button } from '../components/Button'
import { EventCard } from '../components/EventCard'

export default function Home() {
  return (
    <Layout>
      {/* Hero Section */}
      <section className="py-32 text-center">
        <div className="container mx-auto px-4">
          <h1 className="mb-6 bg-gradient-to-r from-white to-vibe-teal
                         bg-clip-text text-transparent">
            The universe is the limit
          </h1>
          <p className="text-lg text-text-secondary max-w-2xl mx-auto mb-8">
            Different roles, experiences, backgrounds—and we vibe.
          </p>
          <div className="flex gap-4 justify-center flex-wrap">
            <Button variant="primary">Join the Vibe</Button>
            <Button variant="secondary">Explore Events</Button>
          </div>
        </div>
      </section>

      {/* Events Grid */}
      <section className="py-20">
        <div className="container mx-auto px-4">
          <h2 className="text-center mb-10">Upcoming Vibes</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {events.map(event => (
              <EventCard key={event.id} {...event} />
            ))}
          </div>
        </div>
      </section>
    </Layout>
  )
}
```

## Using with shadcn/ui

### Install shadcn/ui
```bash
npx shadcn-ui@latest init
```

### Customize shadcn Components
Update `components.json` to use our colors:
```json
{
  "style": "default",
  "tailwind": {
    "baseColor": "vibe-purple",
    "cssVariables": true
  }
}
```

### Override shadcn Styles
```css
/* Override shadcn button */
.ui-button {
  @apply font-semibold tracking-wide transition-all duration-250;
}

.ui-button-primary {
  @apply bg-vibe-orange hover:bg-vibe-orange-dark hover:shadow-glow-orange;
}

.ui-button-secondary {
  @apply border-vibe-teal text-vibe-teal hover:bg-vibe-teal hover:text-vibe-purple;
}
```

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