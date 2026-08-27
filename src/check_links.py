#!/usr/bin/env python3
import os, re, sys

DIST = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "dist")
link_re = re.compile(r'(?:href|src)="([^"]+)"')

errors = []
checked = 0
for root, dirs, files in os.walk(DIST):
    for fn in files:
        if not fn.endswith(".html"):
            continue
        path = os.path.join(root, fn)
        with open(path, encoding="utf-8") as f:
            content = f.read()
        for m in link_re.finditer(content):
            url = m.group(1)
            if url.startswith(("http://", "https://", "mailto:", "tel:", "#", "data:")):
                continue
            checked += 1
            target = url.split("#")[0]
            if not target:
                continue
            resolved = os.path.normpath(os.path.join(root, target))
            if not os.path.exists(resolved):
                errors.append(f"{os.path.relpath(path, DIST)} -> {url} (missing: {os.path.relpath(resolved, DIST)})")

print(f"Checked {checked} local links across HTML files.")
if errors:
    print(f"\n{len(errors)} BROKEN LINKS FOUND:")
    for e in sorted(set(errors)):
        print(" -", e)
    sys.exit(1)
else:
    print("No broken local links found.")
