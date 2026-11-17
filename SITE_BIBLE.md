# Shruti Gupta — Portfolio Site Bible

Single source of truth. Update at every phase gate; nothing contradicts this file.

## Site
- **Name:** Shruti Gupta (working title — domain TBD at ASK-ONCE)
- **One-line value prop:** SEO content that ranks and reads like a human wrote it — for SaaS, AI, and tech brands.
- **Positioning:** Writer portfolios are generic "I write words" pages; Shruti's edge is niche depth (SaaS/AI/crypto/e-commerce) + technical literacy (MERN, REST APIs — she understands what she writes about) + a named metric (60% CTR lift, 20+ brands, 6+ yrs).
- **ICP:** Content/marketing leads at SaaS, AI-tool, and e-commerce companies (and agencies like DesigningBrain) hiring a freelance SEO content writer.
- **Shape:** MARKETING_STATIC (single-page portfolio) — drives skip rules
- **Primary conversion goal:** Contact — "Email me" / hire-me CTA
- **Domain:** GitHub Pages — `<user>.github.io/<repo>/` (repo name at Phase 8) (user deferred)

## Identifiers
- **Live URL:** TBD — recorded at Phase 8
- **Hosting:** GitHub Pages (public repo, `gh-pages` branch, relative asset paths)
- **Email provider:** none (mailto CTA)
- **Analytics:** none (user deferred) — revisit Phase 10

## Design direction
- **Benchmark:** **Quiet editorial magazine** (elevenlabs-like) — print-calm, serif display, the site itself reads as a writing sample — picked by user at ASK-ONCE
- **Tokens:** `theme/tokens.json` · `DESIGN_SYSTEM.md`
- **Brand kit:** `brand/` — monogram/wordmark SVG
- **Imagery grammar:** mixed — real portrait cutouts (user-asset) + generated editorial spot art
- **Motion map:** `design/motion-map.md` — restrained editorial

## Sitemap + page inventory (multi-page — frozen at Phase 3)
| Page | Purpose | Primary CTA | Sections |
|---|---|---|---|
| / | Home — positioning + proof | See the work / Email me | hero, proof strip, featured samples, services teaser, about teaser, contact CTA, footer |
| /work/ | Writing samples grouped by niche | Email me | filterable sample grid: SaaS/AI · Crypto/Web3 · E-commerce · Auto/Lifestyle |
| /about/ | Person + credibility | Email me | portrait, bio, differentiators (tech literacy), tools, education |
| /contact/ | Hire path | Email me | email CTA, availability note, (LinkedIn if provided) |
| /privacy/ | Honest minimal legal page | — | privacy (no trackers, no forms — states exactly that) |

## Copy
- **Voice lock:** confident, plain-spoken, first-person; benefit-led; no buzzword soup ("delve", "leverage", "passionate" banned)
- **Customer vocabulary source:** `docs/customer-psychology.md`
- **Copy files:** `content/`
- **Language(s):** en

## Monetization (if any)
- **Model:** leads (freelance inquiries)
- **Rail:** none — email/LinkedIn contact
- **SKUs/plans:** none

## Tech stack
- **Frontend:** plain HTML/CSS/JS (picked at ASK-ONCE) — multi-page static, no build
- **UI deps:** none expected
- **Backend:** none · datastore none
- **API contract:** n/a
- **Email:** mailto CTA (or formspree-style endpoint if a form is chosen)
- **Design spec:** `docs/ui-design-spec.md` (Phase 3)

## Imagery
- **Manifest:** `imagery/IMAGE_MANIFEST.json` — seeded Phase 3
- **Raw sources:** `imagery/raw/` · **Shipped:** `site/assets/img/`
- **User assets on hand:** 3 portrait photos + 3 background-removed PNGs in `imagery/raw/user-assets/`; resume PDF content extracted
- **Total payload:** TBD — budget hero ≤300KB, section art ≤200KB

## Accounts (exist? provisioned?)
| Account | Status | Notes |
|---|---|---|
| Domain + DNS | TBD | |
| Hosting | TBD | SSH servers exist (apex/astro/cherry/oracle) or free route |
| Email provider | n/a | mailto only, unless form chosen |
| Payment | n/a | |
| Analytics | TBD | |
| Search Console / Bing WT | TBD | |

## Deploy access (server)
- **Route:** TBD — SSH (apex/astro/cherry/oracle available per global rules) or free-domain platform (gh-pages / vercel / netlify / cloudflare-pages)
- **SSH host:** TBD
- **Remote folder:** TBD
- **Domain→docroot mapping:** TBD — verify before deploy

## Privacy stance
- **Collected:** none (mailto only) — if contact form chosen: name, email, message
- **Cookies/tracking:** none by default
- **Data deletion path:** n/a

## Status
| Phase | State | Date | Notes |
|---|---|---|---|
| pre-0 scout | n/a | | concept given: portfolio for Shruti Gupta, SEO content writer |
| 0 research | done | 2026-11-18 | wedge: niche depth + tech literacy; dir: editorial magazine; multi-page HTML/CSS; deploy: gh-pages |
| 1 positioning | done | 2026-11-18 | ICP: SaaS/AI/e-com content leads; value prop locked; voice: confident first-person editorial |
| 2 brand | done | 2026-11-18 | direction: quiet editorial magazine — paper/ink/oxblood, Fraunces+SourceSerif+Inter, hairline structure, mark "sg." |
| 3 spec+wireframes | | | approved: |
| 4 backend | | | |
| 5 copy+imagery | | | images: |
| 6 build | | | tasteskill gate: |
| 7 verify | | | |
| 8 deploy | | | live URL: |
| 9 legal+launch | | | |
| 10 measure | | | |

## Now
- [x] Competitor/portfolio-pattern research → `docs/research/competitor-portfolio-patterns.md`
- [x] Repo scaffold + toolchain preflight (Node 22.18 ✓, Edge/Chrome ✓, Python+Pillow ✓, gh ✓)
- [x] User assets moved to `imagery/raw/user-assets/`
- [ ] ASK-ONCE gate — waiting on user answers

## Open items
- Live article URLs for writing samples → user, Phase 5 (deferred — samples show client+type+niche without links until provided)
- LinkedIn profile URL → user, Phase 5 (deferred — omitted until provided)
- Repo name for gh-pages URL → Phase 8 (deferred)
- Photos approved for site → default yes (user deferred — cutouts produced for this purpose)
- Resume PDF download → default no (user deferred — PDF contains phone numbers; email-only contact instead)

## Handoffs
(none yet)
