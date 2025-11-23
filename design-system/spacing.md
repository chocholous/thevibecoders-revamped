# Spacing System

> "We suffer—a lot—but we learn" - Good spacing reduces the suffering

## 8px Grid System

Everything aligns to an 8px grid. It's predictable, scalable, and developers love it.

## Space Scale

```css
--space-0: 0;          /* When things need to touch */
--space-1: 0.25rem;    /* 4px - Tiny gaps */
--space-2: 0.5rem;     /* 8px - Tight spacing */
--space-3: 0.75rem;    /* 12px - Compact */
--space-4: 1rem;       /* 16px - Default spacing */
--space-5: 1.25rem;    /* 20px - Comfortable */
--space-6: 1.5rem;     /* 24px - Spacious */
--space-8: 2rem;       /* 32px - Breathing room */
--space-10: 2.5rem;    /* 40px - Section gaps */
--space-12: 3rem;      /* 48px - Major sections */
--space-16: 4rem;      /* 64px - Hero spacing */
--space-20: 5rem;      /* 80px - Large sections */
--space-24: 6rem;      /* 96px - Extra large */
--space-32: 8rem;      /* 128px - Maximum space */
```

## Semantic Aliases

For consistency across the codebase:

```css
--space-xs: var(--space-2);   /* Extra small */
--space-sm: var(--space-3);   /* Small */
--space-md: var(--space-4);   /* Medium (default) */
--space-lg: var(--space-6);   /* Large */
--space-xl: var(--space-8);   /* Extra large */
--space-2xl: var(--space-12); /* 2x Extra large */
--space-3xl: var(--space-16); /* 3x Extra large */
```

## Component Spacing

### Buttons
```css
.button {
  padding: var(--space-3) var(--space-6);  /* 12px 24px */
}

.button-sm {
  padding: var(--space-2) var(--space-4);  /* 8px 16px */
}

.button-lg {
  padding: var(--space-4) var(--space-8);  /* 16px 32px */
}
```

### Cards
```css
.card {
  padding: var(--space-6);      /* 24px all around */
  margin-bottom: var(--space-4); /* 16px between cards */
  gap: var(--space-4);          /* 16px between card elements */
}

.card-compact {
  padding: var(--space-4);      /* 16px for tighter cards */
}
```

### Forms
```css
.form-field {
  margin-bottom: var(--space-5); /* 20px between fields */
}

.form-label {
  margin-bottom: var(--space-2); /* 8px before input */
}

.form-help {
  margin-top: var(--space-2);    /* 8px after input */
}

.input {
  padding: var(--space-3) var(--space-4); /* 12px 16px */
}
```

### Text Content
```css
/* Paragraph spacing */
p + p {
  margin-top: var(--space-4);    /* 16px between paragraphs */
}

/* Heading spacing */
h1 {
  margin-top: var(--space-12);   /* 48px before h1 */
  margin-bottom: var(--space-6); /* 24px after h1 */
}

h2 {
  margin-top: var(--space-10);   /* 40px before h2 */
  margin-bottom: var(--space-5); /* 20px after h2 */
}

h3 {
  margin-top: var(--space-8);    /* 32px before h3 */
  margin-bottom: var(--space-4); /* 16px after h3 */
}

/* List spacing */
ul, ol {
  margin: var(--space-4) 0;
  padding-left: var(--space-6);
}

li + li {
  margin-top: var(--space-2);    /* 8px between list items */
}
```

## Page Sections

### Hero Section
```css
.hero {
  padding: var(--space-20) var(--space-4); /* 80px 16px */
}

@media (min-width: 768px) {
  .hero {
    padding: var(--space-32) var(--space-8); /* 128px 32px on desktop */
  }
}
```

### Content Sections
```css
.section {
  padding: var(--space-16) var(--space-4); /* 64px 16px */
}

.section + .section {
  border-top: 1px solid var(--color-surface);
}
```

### Container Padding
```css
.container {
  padding-left: var(--space-4);  /* 16px on mobile */
  padding-right: var(--space-4);
}

@media (min-width: 768px) {
  .container {
    padding-left: var(--space-8);  /* 32px on desktop */
    padding-right: var(--space-8);
  }
}
```

## Layout Patterns

### Stack (Vertical spacing)
```css
.stack-sm > * + * {
  margin-top: var(--space-2);   /* 8px */
}

.stack-md > * + * {
  margin-top: var(--space-4);   /* 16px */
}

.stack-lg > * + * {
  margin-top: var(--space-8);   /* 32px */
}
```

### Cluster (Horizontal spacing with wrap)
```css
.cluster {
  display: flex;
  flex-wrap: wrap;
  gap: var(--space-4);          /* 16px gap */
}

.cluster-tight {
  gap: var(--space-2);          /* 8px gap */
}

.cluster-loose {
  gap: var(--space-6);          /* 24px gap */
}
```

### Grid
```css
.grid {
  display: grid;
  gap: var(--space-6);          /* 24px gap */
}

.grid-tight {
  gap: var(--space-3);          /* 12px gap */
}

.grid-loose {
  gap: var(--space-8);          /* 32px gap */
}
```

## Special Cases

### Event Cards Grid
```css
.events-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: var(--space-6);          /* 24px between cards */
  margin: var(--space-8) 0;     /* 32px top/bottom margin */
}
```

### Navigation
```css
.nav {
  padding: var(--space-4) var(--space-6);
  gap: var(--space-6);          /* Between nav items */
}

.nav-item {
  padding: var(--space-2) var(--space-3);
}
```

### Footer
```css
.footer {
  padding: var(--space-12) var(--space-6);
  margin-top: var(--space-20);
}

.footer-columns {
  gap: var(--space-10);
}
```

## Responsive Spacing

Mobile devices get tighter spacing:

```css
@media (max-width: 768px) {
  :root {
    --space-16: 3rem;   /* 48px instead of 64px */
    --space-20: 4rem;   /* 64px instead of 80px */
    --space-24: 5rem;   /* 80px instead of 96px */
    --space-32: 6rem;   /* 96px instead of 128px */
  }
}
```

## Common Patterns

### Card with Content
```css
.event-card {
  padding: var(--space-6);

  .event-header {
    margin-bottom: var(--space-4);
  }

  .event-body {
    margin-bottom: var(--space-5);
  }

  .event-footer {
    padding-top: var(--space-4);
    border-top: 1px solid var(--color-surface);
  }
}
```

### Modal
```css
.modal {
  padding: var(--space-8);

  .modal-header {
    margin-bottom: var(--space-6);
  }

  .modal-body {
    margin-bottom: var(--space-8);
  }

  .modal-footer {
    display: flex;
    gap: var(--space-4);
    justify-content: flex-end;
  }
}
```

## Spacing Don'ts

- ❌ Don't use arbitrary pixel values
- ❌ Don't mix spacing scales (stick to the system)
- ❌ Don't forget responsive adjustments
- ❌ Don't use margins for component internal spacing (use padding/gap)
- ❌ Don't double up spacing (margin + padding fighting)

## Quick Reference

| Use Case | Value | Pixels |
|----------|-------|--------|
| Between icons | `space-2` | 8px |
| Form field gap | `space-5` | 20px |
| Card padding | `space-6` | 24px |
| Section gap | `space-16` | 64px |
| Hero padding | `space-32` | 128px |

## Philosophy
"Last month is sooo history" - But good spacing is timeless. Keep it consistent, keep it on the grid, and the design will vibe.