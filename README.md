# RoseCare Advocacy — Website

Static site for RoseCare Advocacy LLC, a private patient advocacy practice in
Boca Raton / Palm Beach County, FL. Brand: Peach #FBE9DD + Dark Sage #3F4736,
Cormorant + Outfit. Tagline: "It begins with care."

## Structure
- `index.html` — homepage (LocalBusiness + FAQ schema)
- `/<slug>/index.html` — 8 AEO guide pages targeting problem-language searches, each with FAQ schema
- `css/style.css` — shared brand stylesheet
- `tools/build_pages.py` — generator for guide pages (edit content dict, run, commit)
- `AUDIT.md` — monthly online-presence audit playbook
- `/audits/` — dated audit reports (created as audits run)

## Update workflow
Edits are made in Claude sessions and pushed here; Netlify auto-deploys on push.

## Pending before launch
- [ ] Connect repo to Netlify (import repo, no build command, publish dir = root)
- [ ] Purchase + connect domain; then add canonical URLs, sitemap.xml, and set SITE_URL
- [ ] Replace `#schedule` CTA anchors with the real Healthie scheduling link
- [ ] Add real phone/email to contact section + footer
- [ ] Final image selections (hero + about) from chosen Unsplash set
- [ ] Confirm/rename the 3 service card names
- [ ] Legal disclaimer review
- [ ] Set up Google Business Profile + Google Search Console
