# The Vibe Coders Community Website

## Project Context
Building a clean, minimal community website for The Vibe Coders. Maintain tone from https://thevibecoders.community - playful but minimal.

## Active Skills
- **vibecoders-companion** - Brand guardian and decision companion (ALWAYS USE)
- **frontend-design** - For production-grade UI generation
- **product-self-knowledge** - For Claude Code workflow guidance

## Core Principles
- KISS: Keep it simple, no over-engineering
- YAGNI: Don't build features "just in case"
- Use existing services (Luma for events)

## Primary Goals
1. **Events Hub**: Display upcoming/past events, organizer posts
2. **Organizer Recruitment**: Simple application form
3. **Activity Feed**: Chronological posts from organizers
4. **Simple Upload**: Basic form for organizer updates

## Technical Stack
- **Framework**: Astro (SSG with islands architecture)
- **CMS/Database**: Airtable (all content, forms, images)
- **Styling**: Tailwind CSS
- **Auth**: Auth0 (Google + GitHub login)
- **Events**: Luma Calendar (embedded widgets)
- **Hosting**: Vercel or Netlify (TBD)

## Design Philosophy
"Playful but minimal" - Stripe's clarity + Notion's warmth

## Development Notes
- **Astro-first**: Use .astro components, add React only for interactivity
- **Airtable as backend**: All data operations go through Airtable
- **Minimal JS**: Ship zero JavaScript by default
- Desktop-first responsive
- Page load < 2 seconds
- Use venv for Python (python3.13)
- Use gh for GitHub operations

## Architecture Principles
- **Static by default**: Build time rendering wherever possible
- **Islands architecture**: Interactive components only where needed
- **No custom backend**: Airtable handles everything
- **Embed over API**: Luma widgets instead of API calls
- **Less code heavy**: Choose simpler solutions always

## Quick Decision Reference
When uncertain, consult vibecoders-companion skill for:
- Voice and tone guidelines
- YAGNI defense (what NOT to build)
- Decision shortcuts
- Component patterns (now Astro-based)
- Red flags to avoid