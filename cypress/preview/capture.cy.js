describe('App Preview Capture', () => {
  // Routes to preview
  const routes = [
    { path: '/', name: 'home' },
    { path: '/events', name: 'events' },
    { path: '/about', name: 'about' }
  ];

  routes.forEach(route => {
    it(`captures ${route.name} page`, () => {
      // Visit the page
      cy.visit(route.path);

      // Wait for Astro to be fully loaded
      cy.get('body').should('be.visible');

      // Wait for any Astro islands to hydrate (if they exist)
      cy.get('body').then($body => {
        if ($body.find('astro-island').length > 0) {
          cy.get('astro-island').should('have.attr', 'hydrated');
        }
      });

      // Capture the DOM structure
      cy.document().then(doc => {
        const domData = {
          html: doc.documentElement.outerHTML,
          title: doc.title,
          nodeCount: doc.querySelectorAll('*').length,
          astroIslands: doc.querySelectorAll('astro-island').length,
          images: doc.images.length,
          links: doc.links.length,
          forms: doc.forms.length
        };

        // Save DOM data
        cy.writeFile(`cypress/preview/output/${route.name}-dom.json`, domData);

        // Save clean HTML separately
        cy.writeFile(`cypress/preview/output/${route.name}.html`, domData.html);
      });

      // Take full page screenshot
      cy.screenshot(`${route.name}-full`, {
        capture: 'fullPage',
        overwrite: true
      });

      // Mobile viewport screenshot
      cy.viewport('iphone-x');
      cy.screenshot(`${route.name}-mobile`, {
        capture: 'viewport',
        overwrite: true
      });

      // Reset to desktop
      cy.viewport(1280, 720);

      // Capture performance metrics
      cy.window().then(win => {
        const metrics = win.performance.timing;
        const loadTime = metrics.loadEventEnd - metrics.navigationStart;
        const domReady = metrics.domContentLoadedEventEnd - metrics.navigationStart;

        cy.writeFile(`cypress/preview/output/${route.name}-metrics.json`, {
          loadTime,
          domReady,
          timestamp: new Date().toISOString()
        });
      });
    });
  });

});