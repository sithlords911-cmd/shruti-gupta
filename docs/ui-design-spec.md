# UI design spec — Shruti Gupta portfolio (quiet editorial magazine)

Consumes `theme/tokens.json` + `DESIGN_SYSTEM.md`. Plain HTML/CSS/JS, multi-page, gh-pages (relative asset paths — NO root-absolute URLs).

## Shared chrome (every page)
- **Masthead:** sticky top, paper bg @ ~92% + blur. Left: `sg.` monogram (Fraunces italic, ink; period in accent) linking home. Right: Work · About · Contact (Inter 0.875rem). Active link = accent + underline. Hairline bottom border appears on scroll (>8px).
- **Folio header per section:** kicker (Inter, 0.75rem, uppercase, 0.14em, accent) + hairline rule that draws on scroll. Right-aligned folio number `01 —` muted.
- **Footer:** paperTint band. Left: wordmark + tagline line. Right: email + back-to-top. Folio bottom line: `© 2026 · Amritsar, India · — 30 —`.
- **Container:** 72rem max, equal gutters `clamp(1.25rem,4vw,3rem)`.

## / (Home)
- **Hero:** folio-kicker "SEO Content Writer — Amritsar, India". Fraunces display H1 (~clamp 2.75–5.25rem) two-line: "Content that ranks *and reads* like a human wrote it." (italic accent on "and reads"). Sub in prose 1.25rem inkSoft (2 lines max). CTA row: primary pill accent "Email me" (mailto) + text-link "See the work →". Right column (desktop ≥1024): portrait plate — photo cutout in hairline-framed plate on paperTint, offset like a magazine portrait, small caption "Shruti Gupta". Mobile: portrait below copy, full-width hairline plate.
- **Proof strip:** hairline top+bottom band, 4 stats in a row: `6+` yrs · `20+` brands · `60%` CTR lift · `4` niches. Numbers Fraunces, labels Inter small. Scroll row→2×2 grid on mobile.
- **Featured work:** kicker "Selected work", 3 ruled rows (sample title Fraunces 1.25rem | client name | niche chip | year). Hover: title→accent, row shifts 4px right. "See all work →" text link.
- **Services teaser:** "What I write" — 4 col grid → 2×2 mobile: SEO blogs & articles · Landing pages · Product & tool content · Editing & content cleanup. Each: title + 2-line description. No icons — numbered `01–04` muted.
- **About teaser:** portrait thumb left (2nd photo variant), 3-line bio + "More about me →".
- **Contact CTA:** big centered block: kicker "Hiring a writer?", Fraunces H2 "Tell me what you're building.", email button.
- **Dealt moment (motion):** hero entrance stagger; proof numbers count-up on first view; rules draw under each kicker.

## /work/
- Header: kicker "Work", H1 "The work, by niche.", one-line sub.
- **Filter chips:** All · SaaS & AI · Crypto & Web3 · E-commerce · Auto & Lifestyle — client-side filter of sample rows (JS toggles `data-niche` visibility; chips are buttons, aria-pressed).
- **Groups:** each niche = section header (kicker + count) + ruled rows. Row fields: title · client · type (Blog/Landing/Guide/Review/Ghost) · year. "ghostwritten" labeled where true.
- Bottom CTA repeat.
- Empty state (if JS filters to none — defensive): "Nothing under this niche yet — ask me."

## /about/
- Header: kicker "About", H1 "The writer behind the byline."
- **Lede block:** drop-cap (Source Serif, first letter Fraunces 4×line-height float left), 3 short paras: 6 yrs/20+ brands story · tech literacy angle · editor's eye. Portrait plate right column (photo1 cutout).
- **Differentiators:** 3 ruled cards — "I read the docs" (MERN/REST/API literacy) · "Editor's eye" (trained interns at BidGrowth) · "Intent before ink" (keyword research + search-intent mapping before writing).
- **Toolbox:** chip cloud — WordPress, Google Workspace, Notion, Trello, Asana, Slack + AI tools (ChatGPT, Claude, Gemini, Perplexity, Windsurf) + tech (MERN, JS, HTML/CSS, REST APIs, MongoDB, PL/SQL, Power BI).
- **Education:** 2 ruled rows — M.Sc. Internet Studies (2024–26, 1st in university yr 1, MERN EdTech project) · B.Voc Software Development (2021–24, 89%, 3rd position).
- Still-life image band (generated editorial desk shot) as a quiet divider between differentiators and toolbox.

## /contact/
- Centered single-purpose page: kicker "Contact", display "Tell me what you're building.", sub-line (project-based, remote, IST — replies within a day), primary email button `shruuspeaks@gmail.com`, secondary "Browse the work →".
- Meta row: response time · location · collaboration modes (per-piece / monthly retainer / agency white-label).

## /privacy/
- Honest one-pager: what this site does NOT collect (no forms, no cookies, no analytics, no trackers), what clicking email does (opens your mail app), contact for questions. Plain prose sections.

## Motion (per design/motion-map.md)
Hero entrance stagger · rule draw-on · fade+rise section reveals · count-up stats · underline-draw links · row hover shift · portrait scale-settle · prefers-reduced-motion → opacity-only.

## States
- Hover/focus: links underline-draw; buttons accent→darker accent; chips accentSoft fill; focus-visible = 2px accent outline offset 3px.
- No forms → no validation states. Email = mailto only.
