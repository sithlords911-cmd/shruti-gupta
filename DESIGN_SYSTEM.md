# DESIGN_SYSTEM.md — Shruti Gupta portfolio

**Named direction:** Quiet editorial magazine (elevenlabs-benchmark). The site itself is her best writing sample: it should feel like opening a well-edited magazine — calm, confident, printed.

## Color (from `theme/tokens.json`)

| Role | Hex | Use |
|---|---|---|
| paper | `#FAF7F2` | page background — warm white, never pure white |
| paperTint | `#F1ECE3` | tinted panels, sample cards, footer band |
| ink | `#1B1814` | headlines, body-strong — warm near-black, never pure black |
| inkSoft | `#4A443B` | secondary text |
| muted | `#75705F` | meta, captions, folio numbers |
| hairline | `#DDD6C8` | rules, borders, dividers — the signature structural element |
| accent | `#7A2E1F` | oxblood — links, CTAs, kicker labels, the period in the mark. Sparingly: one accent moment per screen |
| accentSoft | `#F0E1DC` | accent-tinted hover states/chips |
| accentInk | `#FFFFFF` | text on accent fills |

**Contrast:** ink on paper ≈ 14:1, inkSoft on paper ≈ 7:1, accent on paper ≈ 7.5:1 — all AA/AAA for text. Muted reserved for non-essential meta ≥ small size.

## Typography

- **Display — Fraunces** (400/500/600, `opsz` auto): hero, page titles, section heads, pull-quotes. Negative tracking `-0.015em`, line-height 1.05–1.15. Italic Fraunces for emphasis inside headings ("ranks *and reads*").
- **Prose — Source Serif 4** (400/600 + italics): paragraphs on /about and long text. 1.0625rem, 1.65 line-height, `measure` 68ch.
- **UI — Inter** (400/500/600): nav, kickers, buttons, meta, sample card labels, footer. Kicker style = 0.75rem, uppercase, `letter-spacing: 0.14em`, muted or accent.
- Self-hosted woff2, subset latin, `font-display: swap`. Fallbacks: Georgia/system — layout must survive fallback (Fraunces ≈ Georgia metrics-close enough).

## Layout grammar

- **Container** 72rem, equal gutters `clamp(1.25rem, 4vw, 3rem)` — same left/right edge everywhere (hard rule).
- **Folio header** on every section: kicker (uppercase, accent) + hairline rule + optional folio number `01 / 02 / 03` — like magazine section markers.
- **Hairline rules** are the structure: `1px` #DDD6C8 above/below sections, between sample rows, under the masthead. No card shadows — ever.
- **Asymmetric magazine grid:** hero title spans ~8-9 cols; meta/portrait in remaining cols; samples as full-width ruled rows (title | client | niche | year) or 2-col cards.
- **Whitespace is the luxury:** section padding `clamp(4.5rem, 10vw, 8rem)` vertical.
- **Print details:** drop-cap on about-page lede, end-mark `■`/`∎` or `— 30 —` at article ends (old press convention — an "editor's Easter egg"), page footer folio `shrutigupta — page 01`.

## The mark

- **Wordmark:** `Shruti Gupta` in Fraunces 500, ink — with an oxblood full stop: "Shruti Gupta."
- **Monogram:** `sg.` lowercase Fraunces italic + oxblood period — used in masthead-left and as favicon. Legible ≥ 24px.
- Files: `brand/logo.svg`, `brand/mark.svg`, favicon derived.

## Components

- **Buttons:** text-link style with underline-draw animation (default) OR solid accent pill for the single primary CTA. No gradients, no shadows.
- **Sample rows/cards:** ruled rows — title (Fraunces) · client name · niche tag (small caps chip) · year · "ghostwritten" label where true. Hover: accent title + subtle translate.
- **Chips/tags:** hairline-bordered or accentSoft-filled pills, Inter 0.75rem.
- **Nav:** minimal masthead — monogram left, section links right (Work · About · Contact), active = accent underline. Sticky, hairline bottom border, paper bg at ~92% opacity + blur on scroll.
- **Footer:** paperTint band, folio line, email CTA repeat, end-mark.

## Imagery grammar (for `generate-images.py`)

- **Style:** editorial still-life photography — desk scenes, paper, print textures, warm side-light, muted warm palette (paper/accent family). Matte, slight film grain, negative space.
- **Never:** glossy 3D renders, neon, tech-blue gradients, stock-photo handshakes/laptops-with-smiles, AI-looking flat illustration.
- **Portraits:** the real cutout PNGs (`imagery/raw/user-assets/photo*_nobg.png`) — set on paper or paperTint panels, framed like a magazine portrait plate (hairline border or inset). photo3 (car selfie cutout) likely unusable for editorial — prefer photo1 (formal) / photo2 (casual).
- **OG/social card:** paper bg + wordmark + oxblood period + one-line value prop, Fraunces.

## Motion principles (restrained)

- Ease `cubic-bezier(0.22,1,0.36,1)`; fast 160ms / base 320ms / slow 700ms.
- Allowed: fade+rise reveals (translateY 12-20px → 0), hairline rule draw-on (scaleX 0→1), hero staged entrance (kicker → headline → sub → CTA staggered ~90ms), underline draws on links, sample-row hover shift, image scale-on-load (1.04→1).
- Not allowed: bounces/springs on text, parallax stacks, scroll-jacking, marquee tickers, cursor effects.
- `prefers-reduced-motion`: all reveals → instant or simple opacity fade; no transform.

## Voice (site copy)
Confident, plain-spoken, first-person. Short declaratives. Banned: passionate, delve, leverage, synergy, unlock, elevate, "in today's fast-paced world". Signature: honest labels ("ghostwritten for EaseUS"), numbers with sources.
