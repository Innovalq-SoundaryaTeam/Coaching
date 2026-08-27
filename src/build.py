#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Static-site builder for the LS Academy coaching-institute HTML template.
Renders Jinja2 page templates (src/templates/pages/*.html) into flat,
self-contained HTML files under dist/ — no build step is required by the
end buyer, this script is only a development convenience.
"""
import os
import shutil
import sys

from jinja2 import Environment, FileSystemLoader, StrictUndefined

sys.path.insert(0, os.path.dirname(__file__))
import data as D

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES_DIR = os.path.join(ROOT, "src", "templates")
DIST_DIR = os.path.join(ROOT, "dist")

env = Environment(
    loader=FileSystemLoader([TEMPLATES_DIR, os.path.join(TEMPLATES_DIR, "pages")]),
    undefined=StrictUndefined,
    trim_blocks=True,
    lstrip_blocks=True,
)


def blog_url(post):
    """Output filename for a given blog post — the first post keeps the
    plain 'blog-details.html' name (existing inbound links), every other
    post gets a slug suffix, mirroring the course-details.html pattern."""
    idx = next((i for i, p in enumerate(D.BLOG_POSTS) if p["slug"] == post["slug"]), 0)
    return "blog-details.html" if idx == 0 else f"blog-details-{post['slug']}.html"


def author_photo_for(author_name):
    for f in D.FACULTY:
        if f["name"] == author_name or f["name"].replace("Dr. ", "") == author_name.replace("Dr. ", ""):
            return f["photo"]
    return D.FACULTY[0]["photo"]


env.globals["blog_url"] = blog_url

BASE_CONTEXT = {
    "body_class": "",
    "variant": "solid",
    "search_placeholder": "Search…",
    "meta_description": D.SITE["tagline"],
    "site": D.SITE,
    "exam_categories": D.EXAM_CATEGORIES,
    "faculty": D.FACULTY,
    "testimonials": D.TESTIMONIALS,
    "results": D.RESULTS,
    "blog_posts": D.BLOG_POSTS,
    "faqs_general": D.FAQS_GENERAL,
    "faqs_course": D.FAQS_COURSE,
    "pricing_plans": D.PRICING_PLANS,
    "notifications": D.NOTIFICATIONS,
    "student_user": D.STUDENT_USER,
    "admin_user": D.ADMIN_USER,
    "mock_tests": D.MOCK_TESTS,
    "study_materials": D.STUDY_MATERIALS,
    "schedule_items": D.SCHEDULE_ITEMS,
    "admin_students": D.ADMIN_STUDENTS,
    "admin_orders": D.ADMIN_ORDERS,
    "admin_messages": D.ADMIN_MESSAGES,
}

# Each entry: (template_path_relative_to_pages_dir, output_path_relative_to_dist, extra_context)
PAGES = [
    # ---- Public marketing site --------------------------------------------------
    ("home-1.html", "index.html", {
        "page_id": "index", "active": "home1", "title": "Home",
        "meta_description": D.SITE["tagline"],
    }),
    ("home-2.html", "home-2.html", {
        "page_id": "home-2", "active": "home2", "title": "Online Live Prep",
        "meta_description": "Live online classes, adaptive mock tests and a personal dashboard — competitive exam prep built for the way you actually study.",
        "variant": "transparent",
    }),
    ("about.html", "about.html", {
        "page_id": "about", "active": "about", "title": "About Us",
        "meta_description": "Learn about LS Academy's mission, history, leadership faculty and the results that make us India's trusted exam coaching institute.",
    }),
    ("courses.html", "courses.html", {
        "page_id": "courses", "active": "courses", "title": "Courses",
        "meta_description": "Explore coaching programmes for Banking, SSC, Civil Services (UPSC), Engineering (JEE) and Medical (NEET) entrance exams.",
    }),
    ("course-details.html", "course-details.html", {
        "page_id": "course-details", "active": "course-details", "title": "Banking Exams Coaching — Course Details",
        "meta_description": "Full syllabus, faculty, pricing and FAQs for LS Academy's Banking Exams coaching programme (SBI, IBPS, RBI).",
        "course": D.EXAM_CATEGORIES[0],
    }),
    ("course-details.html", "course-details-ssc.html", {
        "page_id": "course-details", "active": "course-details", "title": "SSC Exams Coaching — Course Details",
        "meta_description": "Full syllabus, faculty, pricing and FAQs for LS Academy's SSC Exams coaching programme (CGL, CHSL, MTS, GD).",
        "course": D.EXAM_CATEGORIES[1],
    }),
    ("course-details.html", "course-details-civil-services.html", {
        "page_id": "course-details", "active": "course-details", "title": "Civil Services (UPSC) Coaching — Course Details",
        "meta_description": "Full syllabus, faculty, pricing and FAQs for LS Academy's Civil Services (UPSC) coaching programme.",
        "course": D.EXAM_CATEGORIES[2],
    }),
    ("course-details.html", "course-details-engineering.html", {
        "page_id": "course-details", "active": "course-details", "title": "Engineering Entrance (JEE) Coaching — Course Details",
        "meta_description": "Full syllabus, faculty, pricing and FAQs for LS Academy's Engineering Entrance (JEE) coaching programme.",
        "course": D.EXAM_CATEGORIES[3],
    }),
    ("course-details.html", "course-details-medical.html", {
        "page_id": "course-details", "active": "course-details", "title": "Medical Entrance (NEET) Coaching — Course Details",
        "meta_description": "Full syllabus, faculty, pricing and FAQs for LS Academy's Medical Entrance (NEET) coaching programme.",
        "course": D.EXAM_CATEGORIES[4],
    }),
    ("faculty.html", "faculty.html", {
        "page_id": "faculty", "active": "faculty", "title": "Our Faculty",
        "meta_description": "Meet the subject-matter experts and former exam toppers behind LS Academy's coaching programmes.",
    }),
    ("results.html", "results.html", {
        "page_id": "results", "active": "results", "title": "Results & Achievements",
        "meta_description": "Real ranks, real students — browse LS Academy's selection results across Banking, SSC, UPSC, JEE and NEET.",
        "needs_charts": True,
    }),
    ("fees.html", "fees.html", {
        "page_id": "fees", "active": "fees", "title": "Fees & Pricing",
        "meta_description": "Transparent fee structure and pricing plans for every LS Academy coaching programme.",
    }),
    ("blog.html", "blog.html", {
        "page_id": "blog", "active": "blog", "title": "Blog",
        "meta_description": "Exam strategy, study plans and topper interviews from LS Academy's faculty.",
    }),
    ("contact.html", "contact.html", {
        "page_id": "contact", "active": "contact", "title": "Contact Us",
        "meta_description": "Get in touch with LS Academy — visit a center, call our counsellors or book a free demo class.",
    }),

    # ---- Utility pages ------------------------------------------------------------
    ("login.html", "login.html", {
        "page_id": "login", "active": "login", "title": "Login / Register",
        "meta_description": "Sign in to your LS Academy student dashboard or create a new account.",
        "template_base": "base_auth.html",
    }),
    ("404.html", "404.html", {
        "page_id": "404", "active": "404", "title": "Page Not Found",
        "meta_description": "The page you're looking for doesn't exist.",
        "template_base": "base_minimal.html",
    }),
    ("coming-soon.html", "coming-soon.html", {
        "page_id": "coming-soon", "active": "coming-soon", "title": "Coming Soon",
        "meta_description": "LS Academy's new batch enrollment portal is launching soon.",
        "template_base": "base_minimal.html",
    }),

    # ---- Student dashboard ----------------------------------------------------
    ("student/dashboard.html", "student/dashboard.html", {
        "page_id": "student-dashboard", "active": "dashboard", "title": "Student Dashboard",
        "dash_type": "student", "page_title": "Dashboard", "needs_charts": True,
        "user": D.STUDENT_USER, "rel": "../", "search_placeholder": "Search tests, topics, materials…",
    }),
    ("student/tests.html", "student/tests.html", {
        "page_id": "student-tests", "active": "tests", "title": "Test Library",
        "dash_type": "student", "page_title": "Test Library",
        "user": D.STUDENT_USER, "rel": "../", "search_placeholder": "Search mock tests…",
    }),
    ("student/performance.html", "student/performance.html", {
        "page_id": "student-performance", "active": "performance", "title": "Performance Tracker",
        "dash_type": "student", "page_title": "Performance Tracker", "needs_charts": True,
        "user": D.STUDENT_USER, "rel": "../", "search_placeholder": "Search topics…",
    }),
    ("student/materials.html", "student/materials.html", {
        "page_id": "student-materials", "active": "materials", "title": "Study Material",
        "dash_type": "student", "page_title": "Study Material",
        "user": D.STUDENT_USER, "rel": "../", "search_placeholder": "Search materials…",
    }),
    ("student/schedule.html", "student/schedule.html", {
        "page_id": "student-schedule", "active": "schedule", "title": "Class & Exam Schedule",
        "dash_type": "student", "page_title": "Schedule",
        "user": D.STUDENT_USER, "rel": "../", "search_placeholder": "Search schedule…",
    }),

    # ---- Admin dashboard --------------------------------------------------------
    ("admin/dashboard.html", "admin/dashboard.html", {
        "page_id": "admin-dashboard", "active": "dashboard", "title": "Admin Analytics",
        "dash_type": "admin", "page_title": "Analytics", "needs_charts": True,
        "user": D.ADMIN_USER, "rel": "../", "search_placeholder": "Search anything…",
    }),
    ("admin/students.html", "admin/students.html", {
        "page_id": "admin-students", "active": "students", "title": "Users & Students",
        "dash_type": "admin", "page_title": "Users & Students",
        "user": D.ADMIN_USER, "rel": "../", "search_placeholder": "Search students…",
    }),
    ("admin/courses.html", "admin/courses.html", {
        "page_id": "admin-courses", "active": "courses", "title": "Courses & Tests",
        "dash_type": "admin", "page_title": "Courses & Tests",
        "user": D.ADMIN_USER, "rel": "../", "search_placeholder": "Search courses…",
    }),
    ("admin/orders.html", "admin/orders.html", {
        "page_id": "admin-orders", "active": "orders", "title": "Orders & Payments",
        "dash_type": "admin", "page_title": "Orders & Payments",
        "user": D.ADMIN_USER, "rel": "../", "search_placeholder": "Search orders…",
    }),
    ("admin/messages.html", "admin/messages.html", {
        "page_id": "admin-messages", "active": "messages", "title": "Messages",
        "dash_type": "admin", "page_title": "Messages",
        "user": D.ADMIN_USER, "rel": "../", "search_placeholder": "Search messages…",
    }),

    # ---- Profile (shared template, rendered per dash type) ---------------------
    ("profile.html", "student/profile.html", {
        "page_id": "student-profile", "active": "profile", "title": "My Profile",
        "dash_type": "student", "page_title": "My Profile",
        "user": D.STUDENT_USER, "rel": "../", "search_placeholder": "Search…",
    }),
    ("profile.html", "admin/profile.html", {
        "page_id": "admin-profile", "active": "profile", "title": "My Profile",
        "dash_type": "admin", "page_title": "My Profile",
        "user": D.ADMIN_USER, "rel": "../", "search_placeholder": "Search…",
    }),
]

# ---- Test attempt / score report — one pair per mock test ---------------------
# First test keeps the plain filename (linked from the sidebar's generic
# "Score Reports" / default "Test Library" entry points); the rest get a
# slug suffix, mirroring the course-details.html / course-details-<slug>.html
# pattern used above.
for _i, _t in enumerate(D.MOCK_TESTS):
    _attempt_out = "student/test-attempt.html" if _i == 0 else f"student/test-attempt-{_t['slug']}.html"
    PAGES.append(("student/test-attempt.html", _attempt_out, {
        "page_id": "student-test-attempt", "active": "tests", "title": f"Attempt Test — {_t['name']}",
        "dash_type": "student", "page_title": "Attempt Test",
        "user": D.STUDENT_USER, "rel": "../", "search_placeholder": "Search…",
        "test": _t,
    }))
    if _t["report"]:
        _report_out = "student/score-report.html" if _i == 0 else f"student/score-report-{_t['slug']}.html"
        PAGES.append(("student/score-report.html", _report_out, {
            "page_id": "student-score-report", "active": "score-report", "title": f"Score Report — {_t['name']}",
            "dash_type": "student", "page_title": "Score Report", "needs_charts": True,
            "user": D.STUDENT_USER, "rel": "../", "search_placeholder": "Search past attempts…",
            "test": _t,
        }))

# ---- Blog details — one page per post ------------------------------------------
# First post keeps the plain 'blog-details.html' filename (existing inbound
# links); the rest get a slug suffix, mirroring the pattern above.
for _p in D.BLOG_POSTS:
    _out = blog_url(_p)
    PAGES.append(("blog-details.html", _out, {
        "page_id": "blog-details", "active": "blog", "title": _p["title"],
        "meta_description": _p["excerpt"], "post": _p, "post_url": _out,
        "author_photo": author_photo_for(_p["author"]),
    }))


def build():
    if os.path.exists(DIST_DIR):
        shutil.rmtree(DIST_DIR)
    os.makedirs(DIST_DIR)

    for template_name, out_rel, extra in PAGES:
        ctx = dict(BASE_CONTEXT)
        ctx["rel"] = extra.get("rel", "")
        ctx["needs_charts"] = extra.get("needs_charts", False)
        ctx.update(extra)
        # rel already resolved above; avoid duplicate kwarg issues
        ctx["rel"] = extra.get("rel", "")

        template = env.get_template(template_name)
        html = template.render(**ctx)

        out_path = os.path.join(DIST_DIR, out_rel)
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html)
        print("built:", out_rel)

    # Copy shared assets
    shutil.copytree(os.path.join(ROOT, "assets"), os.path.join(DIST_DIR, "assets"))
    print("\nDone. %d pages built into %s" % (len(PAGES), DIST_DIR))


if __name__ == "__main__":
    build()
