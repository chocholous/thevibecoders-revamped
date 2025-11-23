# Cypress Preview System

A automated preview system that captures both DOM structure and visual screenshots of your Astro application, with zero flaky waits or sleeps.

## Quick Start

```bash
# Make sure your Astro dev server is running (port 4321)
npm run dev

# In another terminal, run the preview
npm run preview
```

This will:
1. Capture DOM structure and screenshots of all pages
2. Generate a beautiful split-view HTML report
3. Open the report in your browser

## What It Captures

For each page (`/`, `/events`, `/about`):
- **Full HTML DOM** structure
- **Desktop screenshot** (1280x720)
- **Mobile screenshot** (iPhone X viewport)
- **Performance metrics** (load time, DOM ready time)
- **Page statistics** (node count, images, links, Astro islands)

## Commands

```bash
# Full preview (capture + view)
npm run preview

# Just capture (headless)
npm run preview:capture

# Just view existing results
npm run preview:view

# Interactive mode (see tests running)
npm run cypress:open
```

## Output Files

```
cypress/
├── preview/
│   ├── capture.cy.js        # The test script
│   └── output/              # JSON data files
│       ├── home-dom.json
│       ├── home-metrics.json
│       └── ...
├── screenshots/             # PNG screenshots
│   ├── home-full.png
│   ├── home-mobile.png
│   └── ...
└── README.md               # This file

preview.html                # Generated viewer (root dir)
```

## How It Works

1. **No sleeps or arbitrary waits** - Cypress automatically waits for:
   - Page to load
   - DOM to be ready
   - Astro islands to hydrate
   - Network requests to complete

2. **Smart waiting strategies**:
   ```javascript
   // Waits for body to be visible
   cy.get('body').should('be.visible');

   // Checks for Astro islands if they exist
   cy.get('body').then($body => {
     if ($body.find('astro-island').length > 0) {
       cy.get('astro-island').should('have.attr', 'hydrated');
     }
   });
   ```

3. **Parallel capture** of DOM and screenshots for efficiency

## Customizing

### Add More Routes

Edit `cypress/preview/capture.cy.js`:

```javascript
const routes = [
  { path: '/', name: 'home' },
  { path: '/events', name: 'events' },
  { path: '/about', name: 'about' },
  // Add more routes here
  { path: '/contact', name: 'contact' },
];
```

### Change Viewports

```javascript
// Desktop size
cy.viewport(1920, 1080);

// Tablet
cy.viewport('ipad-2');

// Custom size
cy.viewport(1440, 900);
```

### Capture Additional Metrics

```javascript
// Add to the capture script
cy.window().then(win => {
  const customMetrics = {
    // Your metrics here
    memoryUsage: win.performance.memory?.usedJSHeapSize,
    networkRequests: win.performance.getEntriesByType('resource').length,
  };

  cy.writeFile(`output/${route.name}-custom.json`, customMetrics);
});
```

## Troubleshooting

### "No preview data found"
Make sure you run `npm run preview:capture` first.

### Screenshots not showing
Check that the Astro dev server is running on port 4321.

### Tests failing
1. Ensure Astro dev server is running
2. Check console for specific error messages
3. Run `npm run cypress:open` to debug interactively

## Benefits Over Traditional Tools

- ✅ **No flaky waits** - Cypress handles timing automatically
- ✅ **Real browser testing** - Uses Chromium under the hood
- ✅ **DOM + Visual together** - See structure and appearance side-by-side
- ✅ **Mobile + Desktop** - Multiple viewport captures
- ✅ **Performance metrics** - Load times included
- ✅ **Zero config** - Works out of the box
- ✅ **Astro-aware** - Waits for islands to hydrate

## Integration with CI/CD

```yaml
# Example GitHub Actions
- name: Start Astro
  run: npm run build && npm run preview &

- name: Wait for server
  run: npx wait-on http://localhost:4321

- name: Run preview
  run: npm run preview:capture

- name: Upload artifacts
  uses: actions/upload-artifact@v2
  with:
    name: preview-results
    path: |
      cypress/screenshots/
      cypress/preview/output/
      preview.html
```