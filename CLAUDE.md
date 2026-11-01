# Rose Care Navigation website — working rules

Live site: https://rosecarenavigation.com (Netlify team "Rose care", project `rosecarenavigation`).
Source of truth on Yehuda's Mac: `~/RoseCare Website/website/` — this repo mirrors that folder.

## Deploying (credits cost money)

- Netlify Personal plan: 1,000 credits/month. **Each production deploy costs 15 credits**; drafts are free.
- While iterating, preview locally or with `netlify deploy --dir=website` (draft URL, free).
- Run `netlify deploy --prod --dir=website` **once per batch of changes, and only after Yehuda approves in chat.**
- Builds from Git are stopped on Netlify; deploys are manual from the local folder.
- Oct 2026 lesson: 20+ back-to-back production deploys in one night used the whole free tier and took the site offline.

## Media budget

- Homepage first load should stay under ~1.5 MB. Bandwidth costs 20 credits/GB.
- Videos: H.264, no audio track, ≤ 960px wide, `-crf 29 -preset slow -movflags +faststart`; target < 1.5 MB.
- `/images/*` is cached for a year (`_headers`, immutable). **Never overwrite an image/video in place — save it under a new name** (e.g. `hero-v3.mp4`) and update the reference.
- Bump `?v=` on the stylesheet link when `css/style.css` changes.
- Unused drafts live in `~/RoseCare Website/site-extras (not deployed)/`, never in `website/`.

## Brand

- Palette: peach `#FBE9DD`, dark sage `#3F4736`. Fonts: Cormorant (headings) + Outfit (body), Parisienne/Italiana accents.
- Name: "Rose Care Navigation" (legal: Rose Care Navigation LLC). Tagline: "It begins with care."
- Phone (561) 299-0526. Based in Boca Raton; serves Palm Beach County / South Florida.
- Non-medical advocacy — never claim medical, legal or financial advice. Don't claim Medicare covers the service.

## SEO plumbing — keep in sync when adding a page

1. Add the URL to `sitemap.xml` with a `lastmod` date.
2. Add a line to `llms.txt`.
3. Link it from the footer / related guides.
4. Unique `<title>`, meta description, one `<h1>`, canonical to `https://rosecarenavigation.com/...`.

`_redirects` sends `rosecarenavigation.netlify.app/*` to the real domain (301).
