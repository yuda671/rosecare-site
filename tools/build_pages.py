#!/usr/bin/env python3
"""RoseCare guide-page generator.
Each entry below becomes /<slug>/index.html with FAQ schema baked in.
To add a page: add an entry, run `python3 tools/build_pages.py`, commit."""
import json, os, html

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

NAV = '''<nav>
  <div class="nav-inner">
    <a class="nav-logo" href="/" aria-label="RoseCare Advocacy home">
      <svg width="34" height="26" viewBox="0 0 34 26" aria-hidden="true">
        <circle cx="11" cy="13" r="9" fill="none" stroke="#C97B5D" stroke-width="1.6"/>
        <circle cx="17" cy="13" r="9" fill="none" stroke="#3F4736" stroke-width="1.6"/>
        <circle cx="23" cy="13" r="9" fill="none" stroke="#E8B79B" stroke-width="1.6"/>
      </svg>
      <span class="nav-name">Rose<em>Care</em> Advocacy</span>
    </a>
    <ul>
      <li class="nav-hide"><a href="/#services">Services</a></li>
      <li class="nav-hide"><a href="/#about">About</a></li>
      <li><a class="btn" href="/#contact" style="padding:10px 22px;">Free consultation</a></li>
    </ul>
  </div>
</nav>'''

FOOTER = '''<footer>
  <div class="wrap">
    <div>
      <h4>RoseCare Advocacy</h4>
      <p>Private patient advocacy for seniors and families in Boca Raton and Palm Beach County, Florida.<br><em style="font-family:'Cormorant',serif; font-size:1.05rem;">It begins with care.</em></p>
    </div>
    <div>
      <h4>Family guides</h4>
      <ul>
        <li><a href="/help-managing-parents-medical-care/">Managing a parent's medical care</a></li>
        <li><a href="/doctor-appointment-accompaniment/">Doctor appointment accompaniment</a></li>
        <li><a href="/out-of-state-caregiver-florida/">Caregiving from out of state</a></li>
        <li><a href="/hospital-discharge-help/">Hospital discharge help</a></li>
      </ul>
    </div>
    <div>
      <h4>Answers</h4>
      <ul>
        <li><a href="/does-medicare-cover-patient-advocate/">Does Medicare cover an advocate?</a></li>
        <li><a href="/what-does-a-patient-advocate-cost/">What does an advocate cost?</a></li>
        <li><a href="/medical-bill-help-florida/">Help with medical bills</a></li>
        <li><a href="/patient-advocate-vs-geriatric-care-manager/">Advocate vs. geriatric care manager</a></li>
      </ul>
    </div>
  </div>
  <div class="foot-bottom">&copy; 2026 RoseCare Advocacy LLC &middot; Boca Raton, Florida &middot; RoseCare Advocacy provides non-medical patient advocacy services and does not provide medical, legal, or financial advice.</div>
</footer>'''

TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{meta}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant:ital,wght@0,500;0,600;0,700;1,500&family=Outfit:wght@300;400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/css/style.css">
<script type="application/ld+json">
{schema}
</script>
</head>
<body>
{nav}
<header class="guide-hero">
  <div class="wrap">
    <p class="eyebrow">{eyebrow}</p>
    <h1>{h1}</h1>
    <p class="answer">{answer}</p>
  </div>
</header>
<article class="guide">
{body}
<p class="local-note">RoseCare Advocacy serves families throughout Palm Beach County — Boca Raton, Delray Beach, Boynton Beach, Deerfield Beach, and surrounding communities — including at Boca Raton Regional Hospital, Delray Medical Center, and Bethesda Hospital.</p>
</article>
<section class="band-sage cta-band">
  <h2>Start with a free 20-minute consultation</h2>
  <p>Tell us what's happening. We'll tell you honestly whether an advocate would help — and what we'd do first.</p>
  <a class="btn btn-light" href="/#contact">Schedule your free consultation</a>
</section>
{footer}
</body>
</html>'''

def faq_schema(faqs):
    return json.dumps({
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in faqs
        ]
    }, indent=1)

def faq_html(faqs):
    out = ['<h2>Common questions</h2><div class="faq" style="margin-top:10px;">']
    for q, a in faqs:
        out.append(f'<details><summary>{html.escape(q)}</summary><p>{a}</p></details>')
    out.append('</div>')
    return "\n".join(out)

PAGES = {}

PAGES["help-managing-parents-medical-care"] = dict(
    title="Help Managing an Elderly Parent's Medical Care | Boca Raton, FL — RoseCare Advocacy",
    meta="Overwhelmed managing a parent's doctors, medications, and appointments in Palm Beach County? A private patient advocate coordinates it all. Free 20-minute consultation.",
    eyebrow="Family guide",
    h1="Help managing an elderly parent's medical care",
    answer="If coordinating your parent's doctors, medications, appointments, and paperwork has become a second job, a private patient advocate can take over the coordination — attending appointments, managing records between specialists, and keeping the whole family informed. Here's how it works in Palm Beach County.",
    body="""<h2>Why a parent's care becomes unmanageable</h2>
<p>Most seniors in South Florida see four or more doctors — a primary physician, a cardiologist, perhaps a neurologist, an orthopedist, an eye doctor. Each one prescribes, orders tests, and schedules follow-ups. Almost none of them talk to each other. The coordination falls to the family: tracking medications from different prescribers, repeating the medical history at every visit, chasing test results, and noticing when one doctor's plan contradicts another's.</p>
<p>That works until it doesn't — a hospitalization, a new diagnosis, or simply the accumulation of appointments crossing the line from "manageable" to "someone's full-time job."</p>
<h2>What a patient advocate actually takes off your plate</h2>
<ul>
<li><strong>Appointment management</strong> — scheduling, preparing questions in advance, attending visits, and sending the family a plain-language summary afterward.</li>
<li><strong>Medication oversight</strong> — maintaining one master list across all prescribers and flagging duplications or interactions for the doctors to review.</li>
<li><strong>Records coordination</strong> — making sure the cardiologist knows what the neurologist changed, and that the primary doctor sees everything.</li>
<li><strong>Hospital response</strong> — when something happens, being on-site quickly, understanding what's going on, and managing the discharge so it doesn't fail.</li>
<li><strong>One point of contact</strong> — the family gets a single knowledgeable person to call instead of six front desks.</li>
</ul>
<h2>How this works with RoseCare</h2>
<p>Every engagement begins with a free 20-minute consultation, followed by a full assessment: we map the diagnoses, providers, medications, insurance, and family concerns into one clear picture. From there you receive a written care plan — what needs to happen, who is responsible, and exactly what we'll handle. Some families need us intensively for a few weeks around a crisis; others keep us on for ongoing coordination, with regular updates to children near and far.</p>""",
    faqs=[
        ("Can you take over dealing with my parent's doctors?",
         "Yes. With your parent's authorization, we communicate directly with physicians' offices, attend appointments, obtain records, and coordinate between specialists — then report back to the family in plain language."),
        ("My parent is resistant to help. How do you handle that?",
         "Very common, and we don't push. We usually start as a low-key presence — a knowledgeable friend at one appointment — and let trust build. Seniors often accept help from a professional advocate more readily than from their own children, because it preserves their sense of independence."),
        ("Do you replace a home health aide or caregiver?",
         "No — we're a different layer. Aides help with daily living; we manage the medical system around your parent: doctors, hospitals, insurance, and records. We often work alongside aides and geriatric care managers."),
    ],
)

PAGES["doctor-appointment-accompaniment"] = dict(
    title="Someone to Go to Doctor Appointments With an Elderly Parent | Palm Beach County — RoseCare Advocacy",
    meta="A professional patient advocate attends doctor visits with your elderly parent in Boca Raton and Palm Beach County — asking questions, taking notes, and reporting back to family.",
    eyebrow="Family guide",
    h1="Someone to go to doctor appointments with your elderly parent",
    answer="Yes, this service exists: a professional patient advocate attends medical appointments with your parent — asking the right questions, taking notes, making sure instructions are understood, and sending you a clear summary afterward. It's one of the most requested services at RoseCare Advocacy.",
    body="""<h2>Why appointments go wrong when seniors go alone</h2>
<p>The average doctor visit lasts about 15 minutes. In that window, an 82-year-old is expected to accurately recall symptoms, report every medication, absorb a diagnosis, understand a treatment plan, and remember the follow-up instructions. Research on patient recall consistently finds that patients forget a large share of what doctors tell them — and that's for all patients, not just seniors managing hearing loss, memory changes, or the stress of a worrying diagnosis.</p>
<p>Families see the result: "What did the doctor say?" — "He said everything's fine." Meanwhile the after-visit summary mentions a medication change no one implemented and a specialist referral no one scheduled.</p>
<h2>What we do before, during, and after each visit</h2>
<ul>
<li><strong>Before:</strong> prepare a written list of symptoms, questions, and current medications; gather any records the doctor should see.</li>
<li><strong>During:</strong> take notes, ask the questions your parent won't ("What are the alternatives?" "What happens if we wait?"), and make sure the doctor's instructions are actually understood before we leave the room.</li>
<li><strong>After:</strong> send the family a plain-language summary — what was said, what changed, and what happens next — and follow through on referrals, tests, and prescriptions so nothing falls through the cracks.</li>
</ul>
<h2>Especially for out-of-town children</h2>
<p>If you live out of state and your parent is in Boca Raton, Delray Beach, or anywhere in Palm Beach County, appointment accompaniment gives you what a phone call can't: a professional set of eyes and ears in the room, and a reliable report afterward. No more reconstructing what happened from your parent's recollection.</p>""",
    faqs=[
        ("Will doctors allow an advocate in the appointment?",
         "Yes. With the patient's consent, advocates routinely attend appointments. Most physicians welcome it — an organized advocate makes the visit more productive for them too."),
        ("Can you also drive my parent to the appointment?",
         "Our role is advocacy rather than transportation, but we coordinate with transport services and family so the logistics are covered, and we meet your parent at the visit."),
        ("What if I want to join by phone from out of state?",
         "We can arrange for you to join the key part of a visit by phone or video when the doctor permits it, and in every case you'll receive a written summary the same day."),
    ],
)

PAGES["does-medicare-cover-patient-advocate"] = dict(
    title="Does Medicare Cover a Patient Advocate? (2026 Guide) — RoseCare Advocacy",
    meta="Medicare doesn't directly pay independent patient advocates, but 2024 CMS navigation codes (PIN and CHI) changed the landscape. What Original Medicare covers and what families pay for.",
    eyebrow="Coverage guide",
    h1="Does Medicare cover a patient advocate?",
    answer="Mostly no — Medicare does not directly reimburse an independent patient advocate you hire privately. But the picture changed in 2024, when Medicare introduced new navigation billing codes (Principal Illness Navigation and Community Health Integration) that allow certain advocacy-type services to be covered when delivered under a treating practitioner. Here's what that means for your family in practice.",
    body="""<h2>The short version</h2>
<p>If you hire a private patient advocate directly, that is a private, out-of-pocket service — like hiring an accountant or an attorney. Medicare, Medicare Advantage, and Medigap plans do not have a benefit category for independently hired advocates.</p>
<h2>What changed in 2024: PIN and CHI codes</h2>
<p>In 2024, CMS created new billing codes for <strong>Principal Illness Navigation (PIN)</strong> and <strong>Community Health Integration (CHI)</strong>. These allow navigation services — helping a patient with a serious, high-risk condition understand their care, coordinate between providers, and overcome barriers to treatment — to be billed to Original Medicare (Part B) when the services are furnished under the direction of the patient's treating practitioner.</p>
<p>In plain language: the navigation work a patient advocate does can be Medicare-covered in specific situations — when it's connected to a qualifying condition and delivered through a physician's practice rather than hired independently. RoseCare Advocacy operates within a national partner network that supports these arrangements for Original Medicare (Part A &amp; B) patients, and we can tell you in a free consultation whether your situation may qualify.</p>
<h2>What Medicare does cover that families confuse with advocacy</h2>
<ul>
<li><strong>Care management programs</strong> — some physician practices bill Medicare for chronic care management; this is coordination run by the doctor's office, not an advocate working for you.</li>
<li><strong>Hospital discharge planning</strong> — hospitals are required to provide it, but the discharge planner works for the hospital, whose interest is a timely discharge.</li>
<li><strong>SHINE / SHIP counseling</strong> — Florida's free volunteer program answers Medicare enrollment questions, but doesn't attend appointments or manage your care.</li>
</ul>
<h2>Why families hire an advocate anyway</h2>
<p>An independent advocate works only for you — no hospital, insurer, or practice owns their loyalty. Families typically find the cost is offset by caught billing errors, avoided readmissions, denied claims overturned, and the hours of coordination handed off. And it starts with a free consultation, so you can find out what your situation actually needs before spending anything.</p>""",
    faqs=[
        ("Does Medicare Advantage cover a patient advocate?",
         "Medicare Advantage plans include their own case managers, but those work for the insurance company. Independent advocates hired by the family are generally private-pay under Medicare Advantage as well."),
        ("What are PIN and CHI codes?",
         "Principal Illness Navigation and Community Health Integration are Medicare billing codes introduced in 2024 that let navigation services be billed to Original Medicare when provided under a treating practitioner for qualifying conditions. Ask us whether your situation may fit."),
        ("Is a patient advocate tax-deductible or HSA-eligible?",
         "It depends on the services and your tax situation — some care-coordination costs may qualify as medical expenses. Confirm with your tax professional; we can provide the documentation you'd need."),
    ],
)

PAGES["out-of-state-caregiver-florida"] = dict(
    title="Managing a Parent's Care From Out of State | Florida Long-Distance Caregiving — RoseCare Advocacy",
    meta="Your parent is in South Florida and you're not. A local patient advocate becomes your eyes, ears, and voice on the ground — appointments, hospitals, and honest reports back to you.",
    eyebrow="Family guide",
    h1="Managing a parent's care in Florida from out of state",
    answer="You can't manage a Florida parent's healthcare well from New York or Chicago — not because you aren't capable, but because the system requires someone physically present. A local patient advocate becomes your professional presence on the ground: attending appointments, responding when something happens, and reporting back to you after every step.",
    body="""<h2>The South Florida reality</h2>
<p>Palm Beach County may be the long-distance caregiving capital of America. Parents retire to Boca Raton, Delray Beach, and Boynton Beach; their adult children build lives in the Northeast and Midwest. It works beautifully until the first health complication — and then the distance becomes the whole problem.</p>
<p>You know the pattern: the fragmented phone updates ("the doctor said it's nothing"), the guesswork about whether Mom is really taking her medications, the 2am flight when something happens, the vacation days burned on crisis trips instead of visits.</p>
<h2>What a local advocate changes</h2>
<ul>
<li><strong>Scheduled presence</strong> — we attend the appointments that matter and send you a same-day summary of what was actually said.</li>
<li><strong>Crisis response</strong> — if your parent lands in Boca Regional, Delray Medical, or Bethesda, we can be there while you're still checking flights, and we manage the situation until you arrive — or so you don't have to.</li>
<li><strong>Honest ground truth</strong> — a professional assessment of how your parent is really doing, not the "I'm fine, don't worry" version.</li>
<li><strong>Discharge management</strong> — the most dangerous moment in elder care is a hospital discharge with no family present. We make sure the plan is safe, understood, and actually followed.</li>
<li><strong>One number to call</strong> — instead of six front desks in a timezone you're not in.</li>
</ul>
<h2>How families typically structure it</h2>
<p>Most long-distance families start with an assessment visit and a baseline report, then choose a rhythm: some want us at every specialist appointment; others keep us on standby for hospitalizations and check-ins. Either way, you get a written update after every touchpoint, and your parent gets a consistent, familiar professional — not a stranger each time.</p>""",
    faqs=[
        ("How quickly can you respond if my parent is hospitalized?",
         "We serve Palm beach County locally, so in most cases we can be at the hospital the same day — often within hours — and begin managing the situation and updating you immediately."),
        ("Will you tell me the truth about how my parent is doing?",
         "Yes — that's much of our value. We give you a professional, unvarnished picture: what we observed, what concerns us, and what we recommend. Your parent's privacy choices are respected, but our reports to authorized family are honest."),
        ("Can my siblings and I share the updates?",
         "Yes. We send updates to whichever family members your parent authorizes, so everyone works from the same information — which alone prevents a lot of family conflict."),
    ],
)

PAGES["medical-bill-help-florida"] = dict(
    title="Help Understanding & Disputing Medical Bills in Florida — RoseCare Advocacy",
    meta="Confusing or surprise medical bills in Florida? A patient advocate reviews, disputes, and resolves billing errors and denied claims. Most bills contain errors worth checking.",
    eyebrow="Billing guide",
    h1="Help understanding and disputing medical bills in Florida",
    answer="If a medical bill doesn't make sense, don't pay it yet — and don't ignore it. A large share of medical bills contain errors, from duplicate charges to services never received, and denied insurance claims are frequently overturned on appeal. A patient advocate reviews the bill line by line, identifies what's wrong, and handles the dispute for you.",
    body="""<h2>Why medical bills are so often wrong</h2>
<p>A single hospital stay can generate bills from the hospital, the attending physician, the anesthesiologist, the radiologist, the lab, and the pathologist — each billing separately, each capable of coding errors. Add insurance processing on top, and mistakes are routine: duplicate charges, upcoded procedures, services billed but never rendered, claims denied for missing paperwork rather than actual coverage reasons.</p>
<p>Billing offices count on two things: that you can't read the codes, and that you'll eventually pay to make it stop — or ignore it until collections. There's a better path.</p>
<h2>What we do with your bills</h2>
<ul>
<li><strong>Line-by-line review</strong> — we obtain the itemized bill (not the summary) and check every charge against the actual care received.</li>
<li><strong>Insurance reconciliation</strong> — matching bills against your Explanation of Benefits to find what insurance should have paid but didn't.</li>
<li><strong>Denial appeals</strong> — insurers deny claims routinely; a properly documented appeal frequently reverses them.</li>
<li><strong>Error disputes and negotiation</strong> — we handle the calls, the letters, and the escalations, and where appropriate negotiate reductions or reasonable payment arrangements.</li>
<li><strong>Protection from mistakes</strong> — including checking your rights under the federal No Surprises Act for out-of-network surprise bills.</li>
</ul>
<h2>When to bring in an advocate</h2>
<p>The best time is before you pay anything you don't understand — and especially before a bill heads to collections. Bring us the pile (yes, the whole shoebox); sorting medical-billing chaos into a clear picture of what's actually owed is exactly the work we do.</p>""",
    faqs=[
        ("Is it worth disputing a medical bill?",
         "Often yes. Billing errors are common, itemized reviews regularly surface charges that don't belong, and denied claims are frequently overturned on appeal. Even one corrected hospital bill can exceed the cost of the advocacy work many times over."),
        ("Can you help if the bill already went to collections?",
         "Yes — options remain, including disputing the underlying charges and negotiating resolution. But earlier is always better, so bring bills to us as soon as something looks wrong."),
        ("Do you work on contingency?",
         "Our engagement structure is discussed in your free consultation, where we'll also give you an honest read on whether your bills are worth pursuing before you commit to anything."),
    ],
)

PAGES["hospital-discharge-help"] = dict(
    title="Hospital Discharge Help for an Elderly Parent | Palm Beach County — RoseCare Advocacy",
    meta="A rushed hospital discharge is the most dangerous moment in elder care. A patient advocate makes sure your parent's discharge plan in Palm Beach County is safe, understood, and followed.",
    eyebrow="Family guide",
    h1="Hospital discharge help for an elderly parent",
    answer="A hospital discharge is the single most failure-prone moment in a senior's care — instructions given in a rush, medications changed without explanation, follow-ups left unscheduled. A patient advocate manages the discharge: making sure the plan is safe before your parent leaves, and actually executed after.",
    body="""<h2>Why discharges fail</h2>
<p>Hospitals are under pressure to discharge quickly, and the discharge planner — competent and well-meaning as they usually are — works for the hospital. The result is a familiar story: a stack of papers handed over in twenty minutes, three medication changes nobody explains, a "follow up with your cardiologist in one week" that never gets scheduled, and a readmission a month later that everyone calls bad luck.</p>
<p>Poor discharges are a major driver of hospital readmissions among seniors — and most of the failure happens in the first days at home, when no one is checking whether the plan is actually being followed.</p>
<h2>What an advocate does differently</h2>
<ul>
<li><strong>Before discharge:</strong> we review the plan while there's still time to change it — Is home actually safe? Is rehab more appropriate? Are the new medications reconciled against the old ones? What does Medicare cover for the next step?</li>
<li><strong>At discharge:</strong> we make sure instructions are understood in plain language, equipment and home health orders are truly in place, and follow-up appointments are booked before your parent leaves the building.</li>
<li><strong>After discharge:</strong> the first two weeks are where readmissions happen. We confirm medications were filled and are being taken correctly, follow-ups happen, and warning signs get acted on early.</li>
</ul>
<h2>If you're out of state when it happens</h2>
<p>Discharges rarely wait for a convenient time. If your parent is at Boca Raton Regional, Delray Medical Center, Bethesda, or any Palm Beach County facility and you can't be there, we can be — reviewing the plan, asking the hard questions, and reporting to you before anything is signed.</p>""",
    faqs=[
        ("Can you stop the hospital from discharging my parent too early?",
         "Medicare patients have formal appeal rights when they believe a discharge is too soon, and hospitals must inform you of them. We help families understand and exercise those rights when a discharge genuinely isn't safe — and improve the plan when discharge is appropriate."),
        ("What's the difference between you and the hospital's discharge planner?",
         "The discharge planner works for the hospital and manages dozens of discharges at once. We work only for your family, on one discharge: yours. We're the second set of eyes asking whether this plan actually works for your parent's real situation at home."),
        ("Do you help choose a rehab facility?",
         "Yes. When rehab is the next step, we help evaluate the options available to you locally, ask the right questions about staffing and outcomes, and continue advocating during the rehab stay."),
    ],
)

PAGES["patient-advocate-vs-geriatric-care-manager"] = dict(
    title="Patient Advocate vs. Geriatric Care Manager: What's the Difference? — RoseCare Advocacy",
    meta="Patient advocates and geriatric care managers overlap but differ: advocates focus on navigating the medical system; care managers on ongoing aging-life management. Which does your family need?",
    eyebrow="Answers",
    h1="Patient advocate vs. geriatric care manager: what's the difference?",
    answer="The roles overlap, but the center of gravity differs: a patient advocate specializes in navigating the medical system — appointments, hospitals, insurance, and bills — while a geriatric care manager (aging life care professional) manages the broader life needs of an aging person, like housing, daily care, and long-term planning. Many families need one; some need both, working together.",
    body="""<h2>What a patient advocate does</h2>
<p>A patient advocate is your professional for the <em>medical system</em>: attending doctor appointments, coordinating between specialists, managing hospital stays and discharges, resolving insurance denials, and disputing billing errors. The advocate's home turf is the exam room, the hospital floor, and the insurance phone tree.</p>
<h2>What a geriatric care manager does</h2>
<p>A geriatric care manager — often a social worker or nurse by background — manages the <em>life</em> of an aging person: assessing whether it's time for assisted living, hiring and supervising home caregivers, coordinating daily support, and planning long-term arrangements. Their home turf is the home, the family meeting, and the senior-living tour.</p>
<h2>Where they overlap — and how to choose</h2>
<ul>
<li><strong>Choose a patient advocate</strong> when the problem is medical-system-shaped: a new serious diagnosis, too many uncoordinated doctors, a hospitalization, insurance battles, or a pile of confusing bills.</li>
<li><strong>Choose a geriatric care manager</strong> when the problem is life-shaped: declining independence, caregiver hiring, housing decisions, or family disagreement about what Mom needs next.</li>
<li><strong>Use both</strong> in complex situations — and expect them to collaborate. We regularly work alongside care managers in Palm Beach County: they manage the living situation, we manage the medical maze, and the family gets full coverage.</li>
</ul>
<h2>The honest answer for your situation</h2>
<p>In a free 20-minute consultation, we'll tell you plainly which kind of help your situation calls for — including when the answer is "you need a care manager, not us," in which case we'll point you to reputable ones locally.</p>""",
    faqs=[
        ("Is a patient advocate cheaper than a geriatric care manager?",
         "Hourly rates for the two professions are broadly similar and vary by market and complexity. The real cost question is scope: advocates are typically engaged around specific medical situations, while care management is often an ongoing monthly relationship."),
        ("Can one professional do both roles?",
         "Some professionals carry both skill sets, but the disciplines are genuinely different. For complex situations, a specialist in each — collaborating — usually serves the family better than one generalist stretched across both."),
        ("Do either of these replace a power of attorney or guardian?",
         "No. Advocates and care managers are professional helpers, not legal decision-makers. They work with whoever holds decision authority — the patient, or their healthcare surrogate or POA."),
    ],
)

PAGES["what-does-a-patient-advocate-cost"] = dict(
    title="What Does a Patient Advocate Cost? (2026) — RoseCare Advocacy",
    meta="Private patient advocates typically bill hourly, with rates varying by service and market. What drives the cost, what families actually spend, and why it often pays for itself.",
    eyebrow="Answers",
    h1="What does a patient advocate cost?",
    answer="Private patient advocates typically bill by the hour, with rates in most U.S. markets ranging from roughly $100 to $350 per hour depending on the service, the advocate's background, and the region. Most engagements are scoped in a free consultation first, so you know what you're committing to before spending anything.",
    body="""<h2>How advocates charge</h2>
<p>Most independent advocates bill hourly, with the rate varying by service type — reviewing medical bills, attending appointments, and managing a hospitalization are different kinds of work. Some offer flat-fee packages for defined projects (a records review, a discharge management engagement) or monthly retainers for ongoing coordination. Insurance generally doesn't cover privately hired advocates, though <a href="/does-medicare-cover-patient-advocate/">recent Medicare navigation codes</a> have created coverage paths in specific situations.</p>
<h2>What drives the cost up or down</h2>
<ul>
<li><strong>Scope</strong> — a one-time bill review is a few hours; managing a complex hospitalization is more.</li>
<li><strong>Intensity</strong> — crisis work (a hospitalization happening now) runs hotter than steady-state coordination.</li>
<li><strong>Complexity</strong> — five specialists and two insurance disputes cost more to untangle than one doctor and a billing question.</li>
</ul>
<h2>The offset most families don't expect</h2>
<p>Advocacy frequently pays for part or all of itself in hard dollars: billing errors caught, denied claims overturned, unnecessary readmissions avoided, and duplicated tests prevented. A single corrected hospital bill or overturned denial can exceed the entire cost of the engagement. The soft-dollar side — vacation days not burned on crisis trips, the coordination hours handed back to your family — is real too.</p>
<h2>How RoseCare handles pricing</h2>
<p>We start every engagement with a free 20-minute consultation. You describe the situation; we tell you honestly what it needs, what it doesn't, and what the scope would look like — including when the honest answer is that you don't need us. No pressure, no surprise invoices, and clear scope before any work begins.</p>""",
    faqs=[
        ("Is a patient advocate covered by insurance?",
         "Generally no — privately hired advocates are an out-of-pocket service. Recent Medicare navigation billing codes (PIN and CHI) created limited coverage paths when navigation is delivered under a treating practitioner; ask us whether your situation may qualify."),
        ("Do you charge for the first consultation?",
         "No. The first 20-minute consultation is free, and we use it to give you an honest scope — including telling you if you don't need an advocate."),
        ("Can several family members split the cost?",
         "Yes, and it's common — siblings frequently share the cost of advocacy for a parent, and our reporting keeps every contributing family member equally informed."),
    ],
)

for slug, p in PAGES.items():
    d = os.path.join(SITE, slug)
    os.makedirs(d, exist_ok=True)
    page = TEMPLATE.format(
        title=p["title"], meta=p["meta"].replace('"', "&quot;"),
        schema=faq_schema(p["faqs"]), nav=NAV, eyebrow=p["eyebrow"],
        h1=p["h1"], answer=p["answer"],
        body=p["body"] + "\n" + faq_html(p["faqs"]),
        footer=FOOTER,
    )
    with open(os.path.join(d, "index.html"), "w") as f:
        f.write(page)
    print(f"built /{slug}/")
print("done.")
