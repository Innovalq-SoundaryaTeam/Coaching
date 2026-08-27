# LS Academy — Source Build System (optional, for developers)

This folder contains the Jinja2 templating source used to generate the flat
static site in the main template package. You do NOT need this to use or sell
the template — it's provided as a convenience for making large-scale edits
(e.g. renaming the brand across all 26 pages at once) without hand-editing
every HTML file.

## Requirements
- Python 3.9+
- `pip install jinja2`

## Usage
```
python3 src/build.py
```
This renders every page in `src/templates/pages/**` into a flat `dist/`
folder (deleting and recreating it each run) and copies `assets/` alongside.

## Structure
- `src/data.py` — all editable content: site info, courses, faculty,
  testimonials, blog posts, pricing plans, dashboard sample data, etc.
- `src/templates/` — Jinja2 templates:
  - `base_public.html`, `base_dash.html`, `base_auth.html`, `base_minimal.html`
    — page shells/layouts
  - `partials/` — navbar, footer, sidebars, topbar, shared `<head>`
  - `pages/` — one template per page, mirroring the final site structure
- `src/build.py` — the `PAGES` list maps each template to its output path and
  per-page context (title, meta description, active-nav-item, etc.)
- `src/check_links.py` — a small script that walks the built `dist/` and
  verifies every local `href`/`src` resolves to a real file
- `src/gen_placeholders.py` — regenerates the labeled placeholder JPGs in
  `assets/images/` (one file per "seed" referenced from `src/data.py`). You
  normally won't need to run this — it's only useful if you add a brand-new
  image seed in `data.py` and want a matching placeholder auto-generated
  before you drop in your own photo. Run with `python3 src/gen_placeholders.py`
  (requires `pip install pillow`).

## Images
Every image used across the template lives as a real local JPG file in
`assets/images/`, named after its "seed" (e.g. `coaching-hero-classroom.jpg`).
`src/data.py`'s `img()`/`avatar()` helpers just build the path
`assets/images/{seed}.jpg` — templates prepend `{{ rel }}` so the same path
resolves correctly from both root-level pages and the `student/`/`admin/`
subfolders. To add a new image, either overwrite an existing seed's file
(simplest — no template changes needed) or add a new seed to `data.py` and a
matching `reg_img()`/`reg_avatar()` call in `gen_placeholders.py`.
