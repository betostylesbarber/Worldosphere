// Worldosphere frame renderer: renders an HTML page (1080x1920) to PNG, or an animation to numbered PNG frames.
// Usage: node render.js page.html out.png
//        node render.js page.html outdir/ --frames 144 --fps 24     (page must define window.renderFrame(t_seconds))
// Requires Playwright with Chromium (set PLAYWRIGHT_BROWSERS_PATH if needed).
const path = require('path');
let pw; try { pw = require('playwright'); } catch (e) { pw = require('/opt/node22/lib/node_modules/playwright'); }
(async () => {
  const [page, out, ...rest] = process.argv.slice(2);
  const frames = rest.includes('--frames') ? parseInt(rest[rest.indexOf('--frames') + 1]) : 0;
  const fps = rest.includes('--fps') ? parseFloat(rest[rest.indexOf('--fps') + 1]) : 24;
  const browser = await pw.chromium.launch();
  const ctx = await browser.newContext({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
  const p = await ctx.newPage();
  await p.goto('file://' + path.resolve(page));
  await p.evaluate(() => document.fonts.ready);
  if (!frames) { await p.screenshot({ path: out }); }
  else {
    for (let i = 0; i < frames; i++) {
      await p.evaluate(t => window.renderFrame(t), i / fps);
      await p.screenshot({ path: path.join(out, String(i).padStart(4, '0') + '.png') });
    }
  }
  await browser.close();
})();
