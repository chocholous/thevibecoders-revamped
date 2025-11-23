# Color System

> "Different roles, experiences, backgrounds—and we... we vibe"

## Brand Palette

Our colors reflect our dual nature: technical depth with human warmth.

### Primary Colors

#### Vibe Purple
- **Base**: `#4A1D7F` - Our signature deep purple background
- **Dark**: `#3A1060` - For depth and shadows
- **Light**: `#5A2D8F` - For surfaces and cards

Used for: Main backgrounds, hero sections, primary brand moments

#### Vibe Teal
- **Base**: `#00D4D4` - Electric teal for energy
- **Dark**: `#00A8A8` - Hover states
- **Light**: `#40E4E4` - Highlights

Used for: Links, highlights, secondary CTAs, success states

#### Vibe Orange
- **Base**: `#FF6B35` - Bold action color
- **Dark**: `#E55525` - Hover states
- **Light**: `#FF8555` - Subtle highlights

Used for: Primary CTAs, important actions, excitement

## Semantic Colors

### Text Colors
```css
--color-text-primary: #FFFFFF;    /* Main text on dark backgrounds */
--color-text-secondary: #D4C4E8;  /* Muted/secondary information */
--color-text-tertiary: #A890C8;   /* Timestamps, metadata */
```

### Surface Colors
```css
--color-background: #4A1D7F;      /* Page background */
--color-surface: #5A2D8F;          /* Cards, sections */
--color-surface-elevated: #6A3D9F; /* Modals, dropdowns */
```

### State Colors
```css
--color-success: #00D97E;  /* "We made it!" */
--color-warning: #FFB547;  /* "Heads up" */
--color-error: #FF5757;    /* "We suffer—but we learn" */
```

### Code Editor Colors
```css
--color-code-bg: #1E1E1E;      /* VS Code dark theme */
--color-code-comment: #6A9955;  /* Comments in green */
--color-code-keyword: #569CD6;  /* Keywords in blue */
--color-code-string: #CE9178;   /* Strings in orange */
```

## Usage Guidelines

### Do's
- ✅ Use high contrast (WCAG AAA where possible)
- ✅ Maintain the purple background as primary
- ✅ Use teal for interactive elements
- ✅ Reserve orange for primary actions
- ✅ Test all color combinations for accessibility

### Don'ts
- ❌ Use low contrast text (we're inclusive)
- ❌ Mix too many colors (keep it minimal)
- ❌ Use pure black (#000000) - too harsh
- ❌ Forget about dark mode (we ARE dark mode)

## Color Combinations

### Recommended Pairings
1. **Purple + White**: Primary text on backgrounds
2. **Purple + Teal**: Brand signature combo
3. **Purple + Orange**: High-impact CTAs
4. **Surface + Teal**: Interactive elements on cards

### Accessibility Notes
- All text on purple backgrounds must be white or very light
- Teal on purple needs careful testing (use for accents, not text)
- Orange works best as a button/CTA color, not for text

## Implementation Examples

### Hero Section
```css
.hero {
  background: var(--color-vibe-purple);
  color: var(--color-text-primary);
}

.hero-cta {
  background: var(--color-vibe-orange);
  color: white;
}
```

### Event Card
```css
.event-card {
  background: var(--color-surface);
  border: 2px solid var(--color-vibe-teal);
  color: var(--color-text-primary);
}
```

### Code Block
```css
.code-showcase {
  background: var(--color-code-bg);
  padding: var(--space-lg);
  border-radius: var(--radius-md);
  font-family: var(--font-family-mono);
}
```

## Special Effects

### Glow Effects
For special moments (hover states, featured content):
```css
.glow-teal {
  box-shadow: 0 0 20px rgba(0, 212, 212, 0.3);
}

.glow-orange {
  box-shadow: 0 0 20px rgba(255, 107, 53, 0.3);
}
```

### Gradients (Use Sparingly)
```css
.vibe-gradient {
  background: linear-gradient(135deg,
    var(--color-vibe-purple) 0%,
    var(--color-vibe-purple-dark) 100%
  );
}
```

## Philosophy
"Last month is sooo history" - Our colors might evolve, but the vibe stays: bold, inclusive, and unmistakably us.