# KeyboardsOnline — GitHub Pages

Free online keyboards for 100+ languages. This repository contains a static, SEO-optimized GitHub Pages version with **25 working keyboards** to start.

Original site: https://keyboardsonline.net/

## Live site (GitHub Pages)
https://onlinekeyboards.github.io/keyboardsonline/

Enable GitHub Pages in the repository: Settings → Pages → Deploy from a branch → `main` / `/ (root)`.

## What's inside
- `index.html` — homepage with search and all 25 keyboards
- `keyboards/` — index of all keyboards
- `<language>-keyboard/` — one page per keyboard, with a working on-screen keyboard, copy / clear / download, word & character counts, FAQ and structured data
- `assets/css/style.css`, `assets/js/keyboard.js` — shared styles and keyboard logic
- `sitemap.xml`, `robots.txt`, `.nojekyll`

## SEO
Every page has a unique title and meta description, canonical URL, Open Graph / Twitter tags, semantic HTML, fast static assets, and JSON-LD structured data (WebSite, WebApplication, BreadcrumbList, FAQPage).

## Add another keyboard
Copy an existing `<language>-keyboard/` page, update its title, description, layout rows in the `kb-data` JSON block, and FAQ, then add it to `index.html`, `keyboards/index.html` and `sitemap.xml`.
