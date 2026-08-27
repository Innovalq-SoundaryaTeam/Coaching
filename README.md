# LS Academy — Coaching Institute HTML Template

A complete, multipurpose HTML template for a **competitive exam coaching institute**
(Banking, SSC, Civil Services/UPSC, Engineering-JEE, Medical-NEET), including a
full marketing website, a student learning dashboard, and an admin back-office —
26 pages in total. Built with Bootstrap 5.3, vanilla JS (no framework, no build
step required), Chart.js for analytics, and Bootstrap Icons.

## Quick start

This is a fully static site — no build step, no server-side language, no database.
Just open `index.html` in a browser, or upload the whole folder to any static host
(Netlify, Vercel, GitHub Pages, cPanel, S3, etc.).

All third-party libraries (Bootstrap CSS/JS, Bootstrap Icons, Chart.js) are
**vendored locally** under `assets/vendor/` so the template works fully offline
and isn't dependent on a CDN staying up. Google Fonts is the one exception and
loads from `fonts.googleapis.com` (with a system-font fallback if it's blocked).

## Structure

```
index.html                 Home 1 — general/classic coaching landing page
home-2.html                Home 2 — SaaS/product-style landing (niche variant)
about.html                 About: mission, history timeline, leadership, testimonials
courses.html                Courses grid, grouped by exam category (anchors: #banking, #ssc, #civil-services, #engineering, #medical)
course-details.html         Course detail page: tabs, syllabus accordion, FAQs, pricing sidebar
faculty.html                Faculty directory with category filter
results.html                 Results/achievements, filterable, with a category chart
fees.html                    Pricing plans + fee-by-category table + FAQ
blog.html                    Blog listing, searchable + filterable by category
blog-details.html            Full article with sidebar, comments, related posts
contact.html                 Contact form, map embed, office hours, FAQ
login.html                   Combined Login / Register (tabbed), social login stub
404.html                     Styled 404 page with search + quick links
coming-soon.html             Coming soon / maintenance page with live countdown

student/                     STUDENT DASHBOARD (protected app area, demo-only auth)
  dashboard.html              Overview: stats, score trend, today's schedule, weak areas
  tests.html                   Test library — subject-wise & full-length mocks, filters
  test-attempt.html            Sample mock-test-taking UI with a live question palette
  score-report.html            Score report: breakdown chart, section table, Q&A review
  performance.html              Topic-wise performance tracker (radar/bar/line charts)
  materials.html                 Study material + previous year paper downloads
  schedule.html                   Upcoming live classes & exam schedule

admin/                        ADMIN DASHBOARD
  dashboard.html                Analytics: revenue trend, category split, recent activity
  students.html                  Users & students management table + add-student modal
  courses.html                    Course & mock-test library management
  orders.html                      Orders & payments table with status filters
  messages.html                    Inbox-style message/enquiry management

assets/
  css/style.css                All custom design-system CSS (works with Bootstrap)
  js/main.js                    Theme toggle, RTL toggle, nav, filters, validation, etc.
  js/charts.js                   Chart.js chart definitions (auto-skipped if no canvas)
  vendor/bootstrap/             Bootstrap 5.3.3 CSS (+ RTL build) and bundled JS
  vendor/bootstrap-icons/       Bootstrap Icons font + CSS
  vendor/chartjs/                Chart.js UMD build
```

## Design principles implemented

- **Responsive / mobile-first** — every page tested from 390px to 1440px+.
- **Dark + light mode** — toggle in the navbar/topbar (moon/sun icon), persisted
  per-browser via `localStorage`, and also respects the OS preference on first visit.
- **RTL compatible** — the translate icon in the navbar/topbar flips the whole
  layout to right-to-left (Bootstrap's RTL stylesheet is swapped in live) for
  Arabic/Hebrew-ready markup. All custom components use logical/mirrored CSS.
- **Clean, semantic HTML** — proper heading hierarchy, landmark elements,
  labelled form fields, alt text on images, breadcrumbs on every inner page.
- **SEO-ready** — unique `<title>`/meta description per page, canonical tags,
  Open Graph/Twitter cards, and descriptive link text throughout.

## Customizing

- **Branding**: edit `SITE` in the Jinja data source (`src/data.py`, if you have
  the source build available) or simply find/replace "LS Academy" and
  the color tokens at the top of `assets/css/style.css` (`--ap-primary`, `--ap-accent`, etc.).
- **Content**: all copy (courses, faculty, testimonials, blog posts, pricing,
  results, dashboard tables) is plain HTML in each page — edit directly.
- **Images**: every image is a real local file in `assets/images/` — labeled,
  branded placeholder JPGs (60 files, ~1.3MB) generated specifically for this
  template, not remote stock-photo URLs. To swap one, just save your own photo
  over the matching file using the **exact same filename** (e.g. drop your own
  photo in as `assets/images/coaching-hero-classroom.jpg`) — every page that
  references that file updates automatically, no HTML editing needed. See
  `IMAGE-REFERENCE.md` for the full filename-to-page map, including which
  images repeat across multiple pages.
- **Forms**: contact/login/register/comment forms are front-end only (client-side
  validation via `needs-validation`), with a `data-demo-submit` attribute that
  shows a toast instead of submitting. Wire them up to your backend or a form
  service (Formspree, Netlify Forms, your own API) by removing that attribute
  and setting a real `action`/`method`, or handling the `submit` event yourself.
- **Dashboards**: the student and admin dashboards are static demo UIs with
  representative sample data — connect them to your real backend/API to make
  them live (test-taking, score calculation, payments, messaging, etc. are all
  presentational only).

## Credits / licenses

- [Bootstrap 5](https://getbootstrap.com/) — MIT License
- [Bootstrap Icons](https://icons.getbootstrap.com/) — MIT License
- [Chart.js](https://www.chartjs.org/) — MIT License
- [Plus Jakarta Sans](https://fonts.google.com/specimen/Plus+Jakarta+Sans) &
  [Manrope](https://fonts.google.com/specimen/Manrope) via Google Fonts — SIL Open Font License
- Placeholder photography: self-generated labeled placeholder images
  (`assets/images/`, 60 files) — demo use only, replace before production
  (see `IMAGE-REFERENCE.md`)
