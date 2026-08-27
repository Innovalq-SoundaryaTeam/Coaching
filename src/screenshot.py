#!/usr/bin/env python3
import os
from playwright.sync_api import sync_playwright

BASE = "http://localhost:8082"
OUT = "/tmp/shots"
os.makedirs(OUT, exist_ok=True)

PAGES = [
    ("index.html", "home1"),
    ("home-2.html", "home2"),
    ("about.html", "about"),
    ("courses.html", "courses"),
    ("course-details.html", "course-details"),
    ("faculty.html", "faculty"),
    ("results.html", "results"),
    ("fees.html", "fees"),
    ("blog.html", "blog"),
    ("blog-details.html", "blog-details"),
    ("contact.html", "contact"),
    ("login.html", "login"),
    ("404.html", "404"),
    ("coming-soon.html", "coming-soon"),
    ("student/dashboard.html", "student-dashboard"),
    ("student/tests.html", "student-tests"),
    ("student/test-attempt.html", "student-test-attempt"),
    ("student/score-report.html", "student-score-report"),
    ("student/performance.html", "student-performance"),
    ("student/materials.html", "student-materials"),
    ("student/schedule.html", "student-schedule"),
    ("admin/dashboard.html", "admin-dashboard"),
    ("admin/students.html", "admin-students"),
    ("admin/courses.html", "admin-courses"),
    ("admin/orders.html", "admin-orders"),
    ("admin/messages.html", "admin-messages"),
]

with sync_playwright() as p:
    browser = p.chromium.launch(executable_path="/opt/pw-browsers/chromium/chrome-linux/chrome" if os.path.exists("/opt/pw-browsers/chromium/chrome-linux/chrome") else None)
    # Desktop light
    ctx = browser.new_context(viewport={"width": 1440, "height": 900})
    page = ctx.new_page()
    errors = {}
    for path, name in PAGES:
        console_errors = []
        page.on("console", lambda msg: console_errors.append(msg.text) if msg.type == "error" else None)
        page.goto(f"{BASE}/{path}", wait_until="networkidle", timeout=20000)
        page.wait_for_timeout(4300)
        page.screenshot(path=f"{OUT}/{name}_light.png", full_page=True)
        if console_errors:
            errors[name] = console_errors
    ctx.close()

    # Dark mode for a subset
    ctx2 = browser.new_context(viewport={"width": 1440, "height": 900}, color_scheme="dark")
    page2 = ctx2.new_page()
    for path, name in [("index.html","home1"), ("student/dashboard.html","student-dashboard"), ("admin/dashboard.html","admin-dashboard"), ("login.html","login")]:
        page2.goto(f"{BASE}/{path}", wait_until="networkidle", timeout=20000)
        page2.wait_for_timeout(4300)
        page2.screenshot(path=f"{OUT}/{name}_dark.png", full_page=True)
    ctx2.close()

    # RTL toggle test on home page + admin dashboard
    ctx3 = browser.new_context(viewport={"width": 1440, "height": 900})
    page3 = ctx3.new_page()
    page3.goto(f"{BASE}/index.html", wait_until="networkidle", timeout=20000)
    page3.click("[data-dir-toggle]")
    page3.wait_for_timeout(500)
    page3.screenshot(path=f"{OUT}/home1_rtl.png", full_page=True)
    page3.goto(f"{BASE}/admin/dashboard.html", wait_until="networkidle", timeout=20000)
    page3.wait_for_timeout(500)
    # RTL setting persists via localStorage across navigation
    page3.screenshot(path=f"{OUT}/admin-dashboard_rtl.png", full_page=True)
    ctx3.close()

    # Mobile viewport
    ctx4 = browser.new_context(viewport={"width": 390, "height": 844})
    page4 = ctx4.new_page()
    for path, name in [("index.html","home1"), ("courses.html","courses"), ("student/dashboard.html","student-dashboard"), ("admin/dashboard.html","admin-dashboard")]:
        page4.goto(f"{BASE}/{path}", wait_until="networkidle", timeout=20000)
        page4.wait_for_timeout(4300)
        page4.screenshot(path=f"{OUT}/{name}_mobile.png", full_page=True)
    ctx4.close()

    browser.close()

print("Console errors per page:")
for name, errs in errors.items():
    print(f"  {name}:")
    for e in errs:
        print(f"    - {e}")
if not errors:
    print("  none")
print("\nDone. Screenshots in", OUT)
