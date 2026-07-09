# RoseCare Advocacy — Monthly Online Presence Audit

**How to run:** Once a month, open a Claude session, paste your GitHub token, and say:
*"Run the RoseCare audit"* — Claude executes this checklist live, writes a dated
report to `/audits/YYYY-MM.md`, and pushes it to this repo so results are tracked
month over month.

---

## 1. Search rankings check
For each target phrase, search Google and record whether rosecare appears, and roughly where:

- [ ] patient advocate Boca Raton
- [ ] patient advocate Palm Beach County
- [ ] help managing elderly parent's medical care
- [ ] someone to go to doctor appointments with elderly parent
- [ ] does Medicare cover a patient advocate
- [ ] managing a parent's care from out of state Florida
- [ ] help disputing medical bills Florida
- [ ] hospital discharge help for elderly parent
- [ ] patient advocate vs geriatric care manager
- [ ] what does a patient advocate cost

## 2. AI-citation check (AEO)
Ask the key questions the way a family would ask an AI assistant, and record whether
RoseCare is cited or mentioned:

- [ ] "How do I find someone to help manage my mom's medical care in Boca Raton?"
- [ ] "Does Medicare pay for a patient advocate?"
- [ ] "Who can go with my elderly father to his doctor appointments in Palm Beach County?"

## 3. Directory & listing verification
Confirm each listing is live, accurate, and consistent (same name, description, service area):

- [ ] Google Business Profile — live, correct, review count vs. last month
- [ ] Umbra directory listing
- [ ] Greater National Advocates (GNA)
- [ ] NAHAC directory
- [ ] APHA / AdvoConnection

## 4. Competitor scan
- [ ] Search "patient advocate Palm Beach County" — note who ranks top 3 and what they've published recently
- [ ] Check 1–2 competitor sites for new pages, services, or positioning changes
- [ ] Note any new advocates appearing in local results

## 5. Content gap → new page
- [ ] Based on the above, identify ONE question families are asking that the site
      doesn't yet answer
- [ ] Draft and publish that page (add to `tools/build_pages.py`, regenerate, push)
- [ ] Add its target phrase to Section 1 of this checklist

## 6. Site health
- [ ] Homepage and all guide pages load correctly on the live domain
- [ ] Free-consultation CTA link works (Healthie scheduler)
- [ ] Any Google Search Console errors or warnings (once GSC is set up)

---

## Report format (`/audits/YYYY-MM.md`)
- Rankings table (phrase → position/absent, change vs. last month)
- AI-citation results
- Directory status
- Competitor notes
- New page published this month
- Action items for next month
