# Component Hierarchy

## Page Components

### HomePage
- **Purpose**: Main landing and event feed
- **Children**: Hero, EventFeed, UpcomingEvents, OrganizerCTA
- **Data**: Recent posts, upcoming events from Luma

### EventsPage
- **Purpose**: Comprehensive event listings
- **Children**: EventsHeader, UpcomingEventsList, PastEventsList
- **Data**: All events from Luma, filtered by date

### BecomeOrganizerPage
- **Purpose**: Organizer application and info
- **Children**: OrganizerHero, WhyOrganize, ApplicationForm
- **Data**: Static content, form submission endpoint

### OrganizerDashboard (Protected)
- **Purpose**: Upload interface for organizers
- **Children**: UploadForm, RecentPosts
- **Data**: Organizer's posts, upload endpoint

## Core Components

### Navigation
```
Navigation
├── Logo (links to home)
├── NavLinks (max 3)
└── MobileMenuToggle
```
- **Variants**: Desktop, Mobile (fullscreen)
- **States**: Default, Active (purple underline)

### Hero
```
Hero
├── Headline (bold statement)
├── Subheadline (supporting text)
└── PrimaryCTA (one clear action)
```
- **Used on**: HomePage, BecomeOrganizerPage
- **Animation**: Fade in on load

## Feed Components

### EventFeed
```
EventFeed
├── FeedHeader
└── FeedGrid
    └── PostCard (multiple)
```
- **Layout**: 3 cols desktop, 2 tablet, 1 mobile
- **Order**: Chronological (newest first)

### PostCard
```
PostCard
├── PostImage (required)
├── PostContent
│   ├── CityBadge
│   ├── PostText (500 char max)
│   └── PostDate (relative)
└── OrganizerInfo
    └── OrganizerName
```
- **Size**: Fixed aspect ratio cards
- **Interaction**: Hover lift effect

### EventCard
```
EventCard
├── EventImage (16:9)
├── EventDetails
│   ├── EventTitle
│   ├── CityBadge
│   ├── EventDate
│   └── AttendeeCount (optional)
└── EventLink (to Luma)
```
- **Badge**: "New" if < 3 days old
- **Click**: Entire card links to Luma

## Form Components

### ApplicationForm
```
ApplicationForm
├── FormProgress (optional)
├── FormFields
│   ├── NameField
│   ├── CityField
│   ├── LinksField
│   └── MotivationField
├── FormActions
│   └── SubmitButton
└── FormFeedback
```
- **Validation**: Client-side first
- **Success**: Show confirmation message

### UploadForm
```
UploadForm
├── CitySelect
├── TextInput (500 chars)
├── ImageUpload
│   ├── DropZone
│   └── PreviewGrid (1-5 images)
└── PublishButton
```
- **States**: Uploading, Success, Error
- **Preview**: Show before publish

## UI Components

### Button
- **Variants**: Primary (purple), Secondary (bordered), Ghost (text)
- **Sizes**: Small, Medium, Large
- **States**: Default, Hover, Active, Disabled, Loading

### Badge
- **Variants**: City, New, Status
- **Colors**: Purple (default), Green (new), Gray (inactive)

### Card
- **Variants**: Post, Event, Simple
- **Shadows**: shadow-sm default, shadow-md on hover

### Input
- **Types**: Text, Textarea, Select
- **States**: Default, Focus (purple ring), Error (red border)

### LoadingStates
- **Skeleton**: Pulsing gray boxes
- **Spinner**: Purple, centered
- **ProgressBar**: For uploads

## Layout Components

### Container
- **Max-width**: 1280px
- **Padding**: Responsive (16px to 32px)

### Grid
- **Variants**: FeedGrid, EventGrid
- **Gaps**: 16px mobile, 24px desktop

### Section
- **Padding**: Consistent vertical rhythm
- **Variants**: Full-width, Contained

## Utility Components

### Image
- **Features**: Lazy load, blur placeholder
- **Optimization**: Next/Image or equivalent

### Link
- **Internal**: Next/Link or equivalent
- **External**: Opens new tab with rel="noopener"

### ErrorBoundary
- **Fallback**: Simple error message
- **Action**: Reload button

## Component Guidelines

### Composition Over Configuration
- Prefer multiple simple components over one configurable
- Example: `<EventCard>` and `<PostCard>` not `<Card type="event">`

### Data Flow
- Pages fetch data
- Components receive props
- No component-level data fetching

### Styling Approach
- Tailwind utilities first
- Component classes for complex states
- No inline styles

### Accessibility Checklist
- Keyboard navigable
- ARIA labels where needed
- Focus indicators visible
- Color contrast WCAG AA

### Performance Considerations
- Images always lazy loaded
- Animations GPU-accelerated
- Bundle splitting at route level
- No unnecessary re-renders

## Component Creation Order

### Phase 1 (Foundation)
1. Button
2. Input
3. Card
4. Navigation
5. Container/Grid

### Phase 2 (Features)
1. PostCard
2. EventCard
3. EventFeed
4. ApplicationForm

### Phase 3 (Polish)
1. LoadingStates
2. ErrorBoundary
3. Animations
4. Mobile optimizations

## Anti-Patterns to Avoid

❌ Deep component nesting (> 3 levels)
❌ Prop drilling (use context sparingly)
❌ Business logic in components
❌ Direct API calls from components
❌ Inline function definitions in renders
❌ Large component files (> 200 lines)
❌ Premature abstraction
❌ Over-engineering for reusability