#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

// Directories
const outputDir = path.join(__dirname, '..', 'cypress', 'preview', 'output');
const screenshotsDir = path.join(__dirname, '..', 'cypress', 'screenshots');

// Check if directories exist
if (!fs.existsSync(outputDir)) {
  console.log('⚠️  No preview data found. Run "npm run preview:capture" first.');
  process.exit(1);
}

// Read all captured data
const routes = ['home', 'events', 'about'];
const previewData = {};

routes.forEach(route => {
  const domPath = path.join(outputDir, `${route}-dom.json`);
  const metricsPath = path.join(outputDir, `${route}-metrics.json`);

  if (fs.existsSync(domPath)) {
    try {
      previewData[route] = {
        dom: JSON.parse(fs.readFileSync(domPath, 'utf8')),
        metrics: fs.existsSync(metricsPath) ?
          JSON.parse(fs.readFileSync(metricsPath, 'utf8')) : null
      };

      // Check for screenshots
      const fullScreenshot = path.join(screenshotsDir, `${route}-full.png`);
      const mobileScreenshot = path.join(screenshotsDir, `${route}-mobile.png`);

      if (fs.existsSync(fullScreenshot)) {
        previewData[route].screenshots = {
          full: fs.readFileSync(fullScreenshot).toString('base64'),
          mobile: fs.existsSync(mobileScreenshot) ?
            fs.readFileSync(mobileScreenshot).toString('base64') : null
        };
      }
    } catch (error) {
      console.error(`Error reading data for ${route}:`, error.message);
    }
  }
});

// Generate HTML viewer
const html = `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Vibe Coders Preview - ${new Date().toLocaleString()}</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }

    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      background: #0a0a0a;
      color: #e0e0e0;
      line-height: 1.6;
    }

    .header {
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
      padding: 2rem;
      text-align: center;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }

    .header h1 {
      font-size: 2rem;
      margin-bottom: 0.5rem;
    }

    .header .timestamp {
      opacity: 0.9;
      font-size: 0.9rem;
    }

    .tabs {
      display: flex;
      background: #1a1a1a;
      border-bottom: 1px solid #333;
      position: sticky;
      top: 0;
      z-index: 100;
    }

    .tab {
      padding: 1rem 2rem;
      cursor: pointer;
      border: none;
      background: none;
      color: #999;
      font-size: 1rem;
      transition: all 0.3s;
    }

    .tab:hover {
      background: #222;
    }

    .tab.active {
      color: #fff;
      background: #2a2a2a;
      border-bottom: 2px solid #667eea;
    }

    .content {
      display: none;
      animation: fadeIn 0.3s;
    }

    .content.active {
      display: block;
    }

    @keyframes fadeIn {
      from { opacity: 0; }
      to { opacity: 1; }
    }

    .preview-container {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 2rem;
      padding: 2rem;
      max-width: 1600px;
      margin: 0 auto;
    }

    .panel {
      background: #1a1a1a;
      border-radius: 8px;
      overflow: hidden;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
    }

    .panel-header {
      background: #2a2a2a;
      padding: 1rem;
      font-weight: bold;
      border-bottom: 1px solid #333;
    }

    .panel-content {
      padding: 1rem;
      max-height: 70vh;
      overflow: auto;
    }

    .dom-tree {
      font-family: "SF Mono", Monaco, "Cascadia Code", monospace;
      font-size: 0.85rem;
      line-height: 1.4;
    }

    .dom-tree pre {
      white-space: pre-wrap;
      word-wrap: break-word;
    }

    .screenshot {
      width: 100%;
      border: 1px solid #333;
      border-radius: 4px;
    }

    .metrics {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
      gap: 1rem;
      margin-top: 1rem;
    }

    .metric {
      background: #2a2a2a;
      padding: 1rem;
      border-radius: 4px;
      text-align: center;
    }

    .metric-value {
      font-size: 1.5rem;
      font-weight: bold;
      color: #667eea;
    }

    .metric-label {
      font-size: 0.85rem;
      color: #999;
      margin-top: 0.25rem;
    }

    .view-toggle {
      display: flex;
      gap: 1rem;
      margin-bottom: 1rem;
    }

    .view-btn {
      padding: 0.5rem 1rem;
      background: #2a2a2a;
      border: 1px solid #333;
      color: #e0e0e0;
      border-radius: 4px;
      cursor: pointer;
      transition: all 0.2s;
    }

    .view-btn:hover {
      background: #333;
    }

    .view-btn.active {
      background: #667eea;
      border-color: #667eea;
    }

    .error {
      background: #ff4444;
      color: white;
      padding: 1rem;
      border-radius: 4px;
      margin: 1rem 0;
    }

    ::-webkit-scrollbar {
      width: 8px;
      height: 8px;
    }

    ::-webkit-scrollbar-track {
      background: #1a1a1a;
    }

    ::-webkit-scrollbar-thumb {
      background: #444;
      border-radius: 4px;
    }

    ::-webkit-scrollbar-thumb:hover {
      background: #555;
    }
  </style>
</head>
<body>
  <div class="header">
    <h1>🎨 Vibe Coders Preview</h1>
    <div class="timestamp">Generated: ${new Date().toLocaleString()}</div>
  </div>

  <div class="tabs">
    ${Object.keys(previewData).map((route, index) => `
      <button class="tab ${index === 0 ? 'active' : ''}" data-route="${route}">
        ${route.charAt(0).toUpperCase() + route.slice(1)}
      </button>
    `).join('')}
  </div>

  ${Object.entries(previewData).map(([route, data], index) => `
    <div class="content ${index === 0 ? 'active' : ''}" id="${route}">
      <div class="preview-container">
        <div class="panel">
          <div class="panel-header">📄 DOM Structure & Metrics</div>
          <div class="panel-content">
            ${data.dom ? `
              <div class="metrics">
                <div class="metric">
                  <div class="metric-value">${data.dom.nodeCount || 0}</div>
                  <div class="metric-label">DOM Nodes</div>
                </div>
                <div class="metric">
                  <div class="metric-value">${data.dom.astroIslands || 0}</div>
                  <div class="metric-label">Astro Islands</div>
                </div>
                <div class="metric">
                  <div class="metric-value">${data.dom.images || 0}</div>
                  <div class="metric-label">Images</div>
                </div>
                <div class="metric">
                  <div class="metric-value">${data.dom.links || 0}</div>
                  <div class="metric-label">Links</div>
                </div>
                ${data.metrics ? `
                  <div class="metric">
                    <div class="metric-value">${data.metrics.loadTime || 0}ms</div>
                    <div class="metric-label">Load Time</div>
                  </div>
                  <div class="metric">
                    <div class="metric-value">${data.metrics.domReady || 0}ms</div>
                    <div class="metric-label">DOM Ready</div>
                  </div>
                ` : ''}
              </div>

              <h3 style="margin: 2rem 0 1rem; color: #667eea;">HTML Structure</h3>
              <div class="dom-tree">
                <pre>${escapeHtml(formatHtml(data.dom.html || ''))}</pre>
              </div>
            ` : '<div class="error">No DOM data available</div>'}
          </div>
        </div>

        <div class="panel">
          <div class="panel-header">🖼️ Visual Preview</div>
          <div class="panel-content">
            ${data.screenshots ? `
              <div class="view-toggle">
                <button class="view-btn active" data-view="full">Desktop</button>
                ${data.screenshots.mobile ? `
                  <button class="view-btn" data-view="mobile">Mobile</button>
                ` : ''}
              </div>
              <img class="screenshot"
                   id="${route}-screenshot"
                   src="data:image/png;base64,${data.screenshots.full}"
                   alt="${route} preview">
            ` : '<div class="error">No screenshot available</div>'}
          </div>
        </div>
      </div>
    </div>
  `).join('')}

  <script>
    // Tab switching
    document.querySelectorAll('.tab').forEach(tab => {
      tab.addEventListener('click', () => {
        const route = tab.dataset.route;

        // Update active tab
        document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
        tab.classList.add('active');

        // Update active content
        document.querySelectorAll('.content').forEach(c => c.classList.remove('active'));
        document.getElementById(route).classList.add('active');
      });
    });

    // View toggle (desktop/mobile)
    document.querySelectorAll('.view-toggle').forEach(toggle => {
      toggle.querySelectorAll('.view-btn').forEach(btn => {
        btn.addEventListener('click', () => {
          const view = btn.dataset.view;
          const content = btn.closest('.content');
          const route = content.id;
          const data = ${JSON.stringify(previewData)};

          // Update active button
          toggle.querySelectorAll('.view-btn').forEach(b => b.classList.remove('active'));
          btn.classList.add('active');

          // Update screenshot
          const img = content.querySelector('.screenshot');
          if (img && data[route].screenshots) {
            const screenshot = view === 'mobile' ?
              data[route].screenshots.mobile :
              data[route].screenshots.full;
            if (screenshot) {
              img.src = 'data:image/png;base64,' + screenshot;
            }
          }
        });
      });
    });

    function escapeHtml(str) {
      return str.replace(/[&<>"']/g, (match) => ({
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#39;'
      })[match]);
    }

    function formatHtml(html) {
      // Simple HTML formatting for readability
      return html
        .replace(/></g, '>\\n<')
        .replace(/<(script|style)[^>]*>.*?<\\/\\1>/gs, '') // Remove scripts and styles
        .substring(0, 10000); // Limit to first 10000 chars for performance
    }
  </script>
</body>
</html>`;

// Helper functions for the template
function escapeHtml(str) {
  if (!str) return '';
  return str.replace(/[&<>"']/g, (match) => ({
    '&': '&amp;',
    '<': '&lt;',
    '>': '&gt;',
    '"': '&quot;',
    "'": '&#39;'
  })[match]);
}

function formatHtml(html) {
  if (!html) return '';
  return html
    .replace(/></g, '>\\n<')
    .replace(/<(script|style)[^>]*>.*?<\\/\\1>/gs, '')
    .substring(0, 10000);
}

// Save the viewer
const viewerPath = path.join(__dirname, '..', 'preview.html');
fs.writeFileSync(viewerPath, html);

console.log('✅ Preview generated successfully!');
console.log(`📁 View file: ${viewerPath}`);
console.log('🌐 Opening in browser...');

// Open in browser
const { exec } = require('child_process');
exec(`open ${viewerPath}`);