# The Vibe Coders Design System

## Design Philosophy
**"Playful but Minimal"** - Combining Stripe's clarity with Notion's warmth. Clean interfaces that feel approachable, not sterile. Professional without being corporate.

## Design Tokens

### Colors

```css
/* Primary Palette - Based on actual website */
--color-vibe-purple: #4A1D7F;    /* Deep Purple - Main background */
--color-vibe-teal: #00D4D4;      /* Teal/Cyan - Accents & highlights */
--color-vibe-orange: #FF6B35;    /* Orange - Primary CTAs */
--color-primary: #4A1D7F;        /* Deep Purple - Main brand color */
--color-primary-dark: #3A1560;   /* Darker purple for hover states */
--color-primary-light: #5A2D9F;  /* Lighter purple for accents */

/* Neutral Scale */
--color-black: #0A0A0A;          /* Pure black for text */
--color-gray-900: #1A1A1A;       /* Dark backgrounds */
--color-gray-800: #2D2D2D;       /* Secondary text */
--color-gray-700: #404040;       /* Borders dark mode */
--color-gray-600: #525252;       /* Muted text */
--color-gray-500: #737373;       /* Placeholder text */
--color-gray-400: #A3A3A3;       /* Disabled states */
--color-gray-300: #D4D4D4;       /* Borders light mode */
--color-gray-200: #E5E5E5;       /* Subtle backgrounds */
--color-gray-100: #F5F5F5;       /* Light backgrounds */
--color-white: #FFFFFF;          /* Pure white */

/* Semantic Colors */
--color-success: #10B981;        /* Emerald - Success states */
--color-warning: #F59E0B;        /* Amber - Warnings */
--color-error: #EF4444;          /* Red - Errors */
--color-info: #3B82F6;           /* Blue - Information */

/* Accent Colors */
--color-accent-pink: #EC4899;    /* Playful pink for CTAs */
--color-accent-purple: #8B5CF6;  /* Secondary purple */
--color-accent-blue: #06B6D4;    /* Cyan for highlights */
```

### Typography

```css
/* Font Families */
--font-sans: 'Inter', system-ui, -apple-system, sans-serif;
--font-mono: 'JetBrains Mono', 'Courier New', monospace;

/* Font Sizes */
--text-xs: 0.75rem;      /* 12px */
--text-sm: 0.875rem;     /* 14px */
--text-base: 1rem;       /* 16px */
--text-lg: 1.125rem;     /* 18px */
--text-xl: 1.25rem;      /* 20px */
--text-2xl: 1.5rem;      /* 24px */
--text-3xl: 1.875rem;    /* 30px */
--text-4xl: 2.25rem;     /* 36px */
--text-5xl: 3rem;        /* 48px */

/* Line Heights */
--leading-none: 1;
--leading-tight: 1.25;
--leading-snug: 1.375;
--leading-normal: 1.5;
--leading-relaxed: 1.625;
--leading-loose: 2;

/* Font Weights */
--font-normal: 400;
--font-medium: 500;
--font-semibold: 600;
--font-bold: 700;
```

### Spacing Scale

```css
/* Consistent spacing based on 4px grid */
--space-0: 0;
--space-1: 0.25rem;     /* 4px */
--space-2: 0.5rem;      /* 8px */
--space-3: 0.75rem;     /* 12px */
--space-4: 1rem;        /* 16px */
--space-5: 1.25rem;     /* 20px */
--space-6: 1.5rem;      /* 24px */
--space-8: 2rem;        /* 32px */
--space-10: 2.5rem;     /* 40px */
--space-12: 3rem;       /* 48px */
--space-16: 4rem;       /* 64px */
--space-20: 5rem;       /* 80px */
--space-24: 6rem;       /* 96px */
--space-32: 8rem;       /* 128px */
```

### Border Radius

```css
--radius-none: 0;
--radius-sm: 0.125rem;   /* 2px - Subtle rounding */
--radius-base: 0.25rem;  /* 4px - Default */
--radius-md: 0.375rem;   /* 6px - Cards */
--radius-lg: 0.5rem;     /* 8px - Buttons */
--radius-xl: 0.75rem;    /* 12px - Modals */
--radius-2xl: 1rem;      /* 16px - Large cards */
--radius-full: 9999px;   /* Pills */
```

### Shadows

```css
--shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);
--shadow-base: 0 1px 3px 0 rgb(0 0 0 / 0.1), 0 1px 2px -1px rgb(0 0 0 / 0.1);
--shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
--shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
--shadow-xl: 0 20px 25px -5px rgb(0 0 0 / 0.1), 0 8px 10px -6px rgb(0 0 0 / 0.1);
--shadow-2xl: 0 25px 50px -12px rgb(0 0 0 / 0.25);
```

### Animation

```css
/* Transitions */
--transition-fast: 150ms ease;
--transition-base: 200ms ease;
--transition-slow: 300ms ease;

/* Easing */
--ease-in: cubic-bezier(0.4, 0, 1, 1);
--ease-out: cubic-bezier(0, 0, 0.2, 1);
--ease-in-out: cubic-bezier(0.4, 0, 0.2, 1);
```

## Responsive Breakpoints

```css
/* Mobile First Approach (but designed desktop-first) */
--screen-sm: 640px;   /* Small devices */
--screen-md: 768px;   /* Tablets */
--screen-lg: 1024px;  /* Desktop */
--screen-xl: 1280px;  /* Large screens */
--screen-2xl: 1536px; /* Extra large screens */
```

## Layout Principles

### Container Widths
- Max content width: 1280px
- Reading width (prose): 65ch
- Card grid: 3 columns desktop, 2 tablet, 1 mobile
- Consistent padding: 16px mobile, 24px tablet, 32px desktop

### Grid System
- 12-column grid on desktop
- 8-column grid on tablet
- 4-column grid on mobile
- Gap: 16px (mobile), 24px (desktop)

## Component Patterns

### Cards
- Background: white (light mode) / gray-900 (dark mode)
- Border: 1px solid gray-300 (light) / gray-700 (dark)
- Border radius: radius-md (6px)
- Padding: space-4 (16px) to space-6 (24px)
- Shadow: shadow-sm on hover
- Transition: all properties 200ms ease

### Buttons

**Primary Button**
- Background: color-primary
- Text: white
- Padding: space-2 (8px) space-4 (16px)
- Border radius: radius-lg (8px)
- Hover: color-primary-dark
- Active: scale(0.98)

**Secondary Button**
- Background: transparent
- Border: 1px solid color-gray-300
- Text: color-gray-900
- Hover: background color-gray-100

**Ghost Button**
- Background: transparent
- Text: color-gray-600
- Hover: background color-gray-100
- Minimal padding

### Forms
- Input height: 40px (base), 48px (large)
- Border: 1px solid gray-300
- Focus: border-primary, shadow ring
- Label: text-sm, font-medium, margin-bottom space-2
- Error state: border-error, text-error below

### Typography Hierarchy

**H1 - Page Title**
- Size: text-4xl (36px) mobile, text-5xl (48px) desktop
- Weight: font-bold
- Line height: leading-tight

**H2 - Section Title**
- Size: text-2xl (24px) mobile, text-3xl (30px) desktop
- Weight: font-semibold
- Line height: leading-snug

**H3 - Card Title**
- Size: text-xl (20px)
- Weight: font-semibold
- Line height: leading-snug

**Body Text**
- Size: text-base (16px)
- Weight: font-normal
- Line height: leading-relaxed
- Color: color-gray-800 (light) / color-gray-200 (dark)

**Small Text**
- Size: text-sm (14px)
- Weight: font-normal
- Color: color-gray-600

## Interaction States

### Hover Effects
- Lift: translateY(-2px) + shadow-md
- Glow: subtle primary color shadow
- Fade: opacity 0.8 to 1
- Background shift: subtle gray background

### Focus States
- Ring: 2px offset, primary color
- Outline: 2px solid primary
- High contrast for accessibility

### Loading States
- Skeleton screens with pulse animation
- Spinner: 20px default, primary color
- Progress bars: 4px height, rounded

## Image Handling

### Aspect Ratios
- Event cards: 16:9
- Organizer posts: 4:3 or 1:1
- Hero images: 21:9
- Thumbnails: 1:1

### Optimization
- Lazy loading for below-fold images
- WebP with JPG fallback
- Responsive srcset
- Blur-up placeholders

## Accessibility

### Color Contrast
- WCAG AA minimum (4.5:1 for normal text)
- WCAG AAA for important elements (7:1)
- Test all color combinations

### Keyboard Navigation
- Visible focus indicators
- Logical tab order
- Skip links for navigation
- Escape key closes modals

### Screen Readers
- Semantic HTML structure
- ARIA labels where needed
- Alt text for all images
- Descriptive link text

## Motion & Animation

### Principles
- Purposeful: Every animation has a reason
- Quick: Nothing over 300ms
- Smooth: Use ease-out for most transitions
- Subtle: Small movements, not dramatic

### Common Animations
- Fade in: opacity 0 to 1, 200ms
- Slide up: translateY(10px) to 0, 200ms
- Scale: scale(0.95) to 1, 150ms
- Skeleton pulse: 2s infinite

## Dark Mode Considerations

### Automatic Detection
- Respect system preferences
- Smooth transition between modes
- Persistent user choice

### Color Adjustments
- Invert gray scale
- Slightly desaturate bright colors
- Increase contrast for readability
- Soften pure white to gray-100

## Tailwind Configuration

```javascript
// Extend Tailwind with our design tokens
module.exports = {
  theme: {
    extend: {
      colors: {
        primary: {
          DEFAULT: '#5B4FE5',
          dark: '#4A3FD4',
          light: '#7B6FF5',
        },
        accent: {
          pink: '#EC4899',
          purple: '#8B5CF6',
          blue: '#06B6D4',
        }
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', '-apple-system', 'sans-serif'],
        mono: ['JetBrains Mono', 'Courier New', 'monospace'],
      },
      animation: {
        'pulse-slow': 'pulse 2s ease-in-out infinite',
        'slide-up': 'slideUp 200ms ease-out',
        'fade-in': 'fadeIn 200ms ease-out',
      }
    }
  }
}
```

## Implementation Notes

1. Start with shadcn/ui base components
2. Customize with our color tokens
3. Keep animations subtle and fast
4. Test on real devices, not just browser
5. Prioritize readability over aesthetics
6. When in doubt, choose simpler option