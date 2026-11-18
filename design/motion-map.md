# Motion map — Shruti Gupta portfolio

**Direction:** restrained editorial. Ease `cubic-bezier(0.22,1,0.36,1)`; durations fast 160ms / base 320ms / slow 700ms. `prefers-reduced-motion` → opacity-only equivalents, zero transform.

## / (Home)
| # | Moment | Trigger | Behavior | Layer |
|---|---|---|---|---|
| H1 | Hero entrance | load | staggered: kicker → H1 lines → sub → CTAs → portrait (fade+rise 16px, ~90ms apart, 500ms each) | CSS class + IO |
| H2 | Portrait settle | load | scale 1.04→1 + fade, 700ms, inside plate | CSS |
| H3 | Proof strip | scroll into view | rule draws; numbers count-up 0→final over 900ms, once | JS+IO |
| H4 | Section folios | scroll | kicker fades, hairline rule draws scaleX 0→1 (origin left, 600ms) | IO+CSS |
| H5 | Sample rows | scroll | rows fade+rise staggered 60ms; hover → accent title + translateX 4px (160ms) | IO+CSS |
| H6 | About teaser img | scroll | fade+rise | IO |
| H7 | CTA block | scroll | fade+rise | IO |
| H8 | Masthead rule | scroll y>8 | hairline border fades in 160ms | CSS class |

## /work/
| # | Moment | Trigger | Behavior |
|---|---|---|---|
| W1 | Page title | load | kicker → H1 → chips stagger |
| W2 | Group sections | scroll | header + rows fade+rise stagger |
| W3 | Filter | click chip | chips restyle (accentSoft); rows crossfade+slight rise on filter change (250ms) — no FLIP needed |
| W4 | Row hover | hover | accent title + translateX 4px |

## /about/
| # | Moment | Trigger | Behavior |
|---|---|---|---|
| A1 | Header | load | stagger entrance |
| A2 | Portrait plate | load | scale-settle (same as H2) |
| A3 | Drop-cap lede | scroll | fade+rise |
| A4 | Differentiator cards | scroll | 3-card stagger rise |
| A5 | Still-life band | scroll | slow fade in + 2% scale settle |
| A6 | Toolbox chips | scroll | chips stagger fade+rise 30ms each |
| A7 | Education rows | scroll | ruled rows draw + rise |

## /contact/
| # | Moment | Trigger | Behavior |
|---|---|---|---|
| C1 | Centered block | load | kicker → headline → sub → button stagger |
| C2 | Email button | hover | subtle lift (translateY -1px) + darker accent |

## /privacy/
| # | Moment | Trigger | Behavior |
|---|---|---|---|
| P1 | Header | load | simple stagger, then static reading |

## Global
- Link underline-draw on hover (background-size 0→100% trick), 160ms.
- `prefers-reduced-motion`: all above → opacity fade only; count-up shows final numbers; no transforms.
