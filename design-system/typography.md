# Typography System

> "The universe is the limit" - Our type should feel as bold as our ambitions

## Font Families

### Primary: Inter
Our workhorse font. Clean, modern, highly legible.
```css
font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
```

### Code: JetBrains Mono
For code blocks, technical content, and when we want that "coder vibe."
```css
font-family: 'JetBrains Mono', 'Fira Code', 'Courier New', monospace;
```

## Type Scale

Desktop-first approach (because we code on desktops).

### Display Sizes
```css
--font-size-5xl: 3.75rem;  /* 60px - "The universe is the limit" */
--font-size-4xl: 3rem;     /* 48px - Main hero headlines */
--font-size-3xl: 2.25rem;  /* 36px - Section headers */
```

### Heading Sizes
```css
--font-size-2xl: 1.875rem; /* 30px - H1 */
--font-size-xl: 1.5rem;    /* 24px - H2 */
--font-size-lg: 1.25rem;   /* 20px - H3 */
```

### Body Sizes
```css
--font-size-md: 1.125rem;  /* 18px - Large body text */
--font-size-base: 1rem;    /* 16px - Default body */
--font-size-sm: 0.875rem;  /* 14px - Secondary text */
--font-size-xs: 0.75rem;   /* 12px - Captions, labels */
```

## Font Weights

Keep it simple. We don't need every weight.

```css
--font-weight-normal: 400;    /* Body text */
--font-weight-medium: 500;    /* Subtle emphasis */
--font-weight-semibold: 600;  /* Subheadings */
--font-weight-bold: 700;      /* Headlines, CTAs */
--font-weight-extrabold: 800; /* Big statements */
```

## Line Heights

```css
--line-height-tight: 1.25;    /* Headlines */
--line-height-base: 1.5;      /* Body text */
--line-height-relaxed: 1.75;  /* Long-form content */
--line-height-loose: 2;        /* Very relaxed reading */
```

## Letter Spacing

```css
--letter-spacing-tight: -0.025em;  /* Headlines */
--letter-spacing-normal: 0;        /* Body */
--letter-spacing-wide: 0.025em;    /* Uppercase labels */
--letter-spacing-wider: 0.05em;    /* Special emphasis */
```

## Text Styles

### Headlines

#### Hero Title
```css
.hero-title {
  font-size: var(--font-size-5xl);
  font-weight: var(--font-weight-extrabold);
  line-height: var(--line-height-tight);
  letter-spacing: var(--letter-spacing-tight);
  color: var(--color-text-primary);
}
```

#### Section Header
```css
.section-header {
  font-size: var(--font-size-3xl);
  font-weight: var(--font-weight-bold);
  line-height: var(--line-height-tight);
  color: var(--color-text-primary);
  margin-bottom: var(--space-md);
}
```

### Body Text

#### Default Paragraph
```css
p {
  font-size: var(--font-size-base);
  font-weight: var(--font-weight-normal);
  line-height: var(--line-height-relaxed);
  color: var(--color-text-primary);
  max-width: var(--content-width); /* ~65ch for readability */
}
```

#### Lead Paragraph
```css
.lead {
  font-size: var(--font-size-md);
  font-weight: var(--font-weight-medium);
  color: var(--color-text-secondary);
  margin-bottom: var(--space-lg);
}
```

### Special Styles

#### Code Inline
```css
code {
  font-family: var(--font-family-mono);
  font-size: 0.9em;
  padding: 0.125em 0.25em;
  background: var(--color-surface);
  border-radius: var(--radius-sm);
  color: var(--color-vibe-teal);
}
```

#### Manifesto Style
```css
.manifesto-item {
  font-size: var(--font-size-lg);
  font-weight: var(--font-weight-semibold);
  font-family: var(--font-family-mono);
  color: var(--color-vibe-teal);
  /* VS Code comment style */
}
```

#### Label/Caption
```css
.label {
  font-size: var(--font-size-xs);
  font-weight: var(--font-weight-semibold);
  letter-spacing: var(--letter-spacing-wider);
  text-transform: uppercase;
  color: var(--color-text-tertiary);
}
```

## Responsive Adjustments

Mobile gets slightly smaller display sizes:

```css
@media (max-width: 768px) {
  .hero-title {
    font-size: var(--font-size-4xl); /* Down from 5xl */
  }

  .section-header {
    font-size: var(--font-size-2xl); /* Down from 3xl */
  }
}
```

## Usage Examples

### Event Card
```css
.event-card {
  .event-date {
    font-size: var(--font-size-sm);
    font-weight: var(--font-weight-semibold);
    color: var(--color-vibe-teal);
    text-transform: uppercase;
    letter-spacing: var(--letter-spacing-wide);
  }

  .event-title {
    font-size: var(--font-size-xl);
    font-weight: var(--font-weight-bold);
    margin: var(--space-sm) 0;
  }

  .event-location {
    font-size: var(--font-size-base);
    color: var(--color-text-secondary);
  }
}
```

### Call-to-Action Button
```css
.cta-button {
  font-size: var(--font-size-base);
  font-weight: var(--font-weight-bold);
  letter-spacing: var(--letter-spacing-wide);
  text-transform: uppercase;
  padding: var(--space-md) var(--space-lg);
}
```

## Typography Don'ts

- ❌ Don't use system-ui (stick to Inter for consistency)
- ❌ Don't go below 14px for body text (accessibility)
- ❌ Don't use light weights on dark backgrounds (poor contrast)
- ❌ Don't forget max-width on paragraphs (readability)
- ❌ Don't mix too many sizes (keep hierarchy clear)

## Special Characters & Emoji

We embrace emoji as part of our language:
- City flags for locations (🇬🇧 🇺🇸 🇵🇹)
- Sparkles for excitement (✨)
- Celebration for achievements (🎉)
- Tools for technical content (🛠️)

Use them in headings, body text, wherever they add personality without cluttering.

## Philosophy
"We're pioneers" - Our typography should feel confident and clear. No apologizing, no hedging. Say it like you mean it.