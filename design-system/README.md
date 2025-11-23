# The Vibe Coders Design System

> "The universe is the limit" - A design system for pioneers who vibe

## Design Philosophy
**Playful but minimal** - We embrace the struggle, celebrate rapid change, and keep it real. Dark theme by default because we're coders. High contrast because accessibility matters. Personality through copy because we don't need decoration to vibe.

## The Vibe
- **Self-aware**: "We suffer—a lot—but we learn"
- **Bold**: "The universe is the limit" (not just the sky)
- **Current**: "Last month is sooo history"
- **Authentic**: "We don't sell our souls"
- **IRL-focused**: "Vibe coding happens IRL"

## Core Design Principles
1. **Dark Mode Native**: Deep purple backgrounds, high contrast
2. **Code Editor Aesthetic**: Mono fonts, VS Code vibes where appropriate
3. **Emoji-friendly**: City flags, sparkles - part of our language
4. **Performance First**: < 2 second loads, minimal dependencies
5. **KISS/YAGNI**: Build what we need, when we need it

## Quick Start
```css
/* Import all design tokens */
@import './tokens.css';

/* Use throughout your styles */
.vibe-component {
  background: var(--color-vibe-purple);
  color: var(--color-text-primary);
  padding: var(--space-md);
}
```

## File Structure
```
design-system/
├── README.md           # You are here
├── tokens.css          # All design tokens as CSS variables
├── colors.md           # Color documentation & usage
├── typography.md       # Type scale & guidelines
├── spacing.md          # Spacing system & rhythm
├── components.md       # Component patterns
├── patterns.md         # Layout patterns
└── examples/           # Implementation examples
```

## Design DNA
Inspired by:
- **Our Current Site**: Deep purple (#4A1D7F), teal accents, code editor aesthetic
- **freeCodeCamp**: Accessibility, functional clarity
- **Rewriting the Code**: Community warmth, inclusivity
- **Stripe/Linear**: Clean execution, thoughtful interactions

## Implementation Stack
- **Framework**: Next.js (likely)
- **Styling**: Tailwind CSS + custom tokens
- **Components**: shadcn/ui as base, customized for our vibe
- **Fonts**: Inter for UI, JetBrains Mono for code
- **Icons**: Lucide + emoji

## Community Scale
- 9 Active Cities
- 100+ Members
- Quality > Quantity
- IRL events are core