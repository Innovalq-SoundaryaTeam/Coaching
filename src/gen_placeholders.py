#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generates real local placeholder image files (JPGs) for every photo/avatar used
in the template, under assets/images/<seed>.jpg, so buyers can replace them by
copy-pasting a same-named file over the top instead of editing HTML.

Each placeholder shows its own seed name as centered text, so it's obvious at a
glance in a file browser which image belongs where.
"""
import hashlib
import os
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(ROOT, "assets", "images")
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

# Curated brand-adjacent gradient pairs (light -> dark of the same hue family)
PALETTE = [
    ("#6d5ef0", "#4338ca"),  # indigo (primary)
    ("#f59e0b", "#c2670a"),  # amber (accent)
    ("#22c55e", "#15803d"),  # green
    ("#0ea5e9", "#0369a1"),  # sky blue
    ("#f472b6", "#be185d"),  # pink
    ("#a78bfa", "#6d28d9"),  # violet
    ("#fb7185", "#be123c"),  # rose
    ("#2dd4bf", "#0f766e"),  # teal
]

# seed -> (width, height, kind)  kind: "photo" | "avatar"
SPECS = {}

def reg_img(seed, w, h):
    SPECS[seed] = (w, h, "photo")

def reg_avatar(seed, size=400):
    SPECS[seed] = (size, size, "avatar")

# --- From data.py img()/avatar() calls -------------------------------------
reg_img("ls-academy-og", 1200, 630)
reg_img("banking-exam-prep", 900, 650)
reg_img("ssc-exam-prep", 900, 650)
reg_img("upsc-civil-services", 900, 650)
reg_img("jee-engineering-prep", 900, 650)
reg_img("neet-medical-prep", 900, 650)
for seed in ["arvind-menon", "priya-raghavan", "rakesh-chauhan", "sanya-kapoor",
             "imran-siddiqui", "neha-verma", "karan-malhotra", "ritu-nair"]:
    reg_avatar(seed)
for seed in ["ankit-yadav", "simran-kaur", "devansh-rao", "meera-pillai",
             "aditya-bose", "fatima-sheikh", "rohit-sinha", "ishita-ghosh",
             "varun-kapoor", "ananya-iyer", "karthik-nair", "pooja-reddy"]:
    reg_avatar(seed)
for seed in ["study-plan-banking", "ssc-tier2-tips", "upsc-answer-writing",
             "jee-mechanics-mistakes", "neet-biology-strategy", "mock-test-analysis"]:
    reg_img(seed, 900, 600)
reg_avatar("aarav-sharma")
reg_avatar("rhea-kapoor")
for seed in ["diya-patel", "vihaan-gupta", "anaya-joshi", "kabir-khan",
             "sara-ahmed", "reyansh-rao", "myra-desai",
             "neelam-joshi", "parth-malhotra", "gauri-nambiar", "yash-trivedi",
             "ira-bhatt", "om-prakash"]:
    reg_avatar(seed)

# --- Hardcoded template images ----------------------------------------------
reg_avatar("s1", 200)
reg_avatar("s2", 200)
reg_avatar("s3", 200)
reg_img("coaching-hero-classroom", 900, 720)
reg_img("coaching-study-journey", 1000, 760)
reg_img("about-campus-1", 700, 820)
reg_img("about-campus-2", 500, 380)
reg_img("dashboard-preview-app", 900, 680)
reg_img("mock-test-engine-ui", 900, 700)
reg_img("analytics-dashboard-ui", 900, 700)
reg_img("all-courses-overview", 900, 650)
# Generic commenter avatars used on blog-details.html
for seed in ["commenter-1", "commenter-2", "commenter-3"]:
    reg_avatar(seed)


def label_for(seed):
    words = seed.replace("-", " ").split()
    return " ".join(w.capitalize() for w in words)


def initials_for(seed):
    words = [w for w in seed.replace("-", " ").split() if w.isalpha()]
    if not words:
        return seed[:2].upper()
    if len(words) == 1:
        return words[0][:2].upper()
    return (words[0][0] + words[-1][0]).upper()


def colors_for(seed):
    idx = int(hashlib.md5(seed.encode()).hexdigest(), 16) % len(PALETTE)
    return PALETTE[idx]


def make_gradient(w, h, c1, c2):
    def hex_to_rgb(hx):
        hx = hx.lstrip("#")
        return tuple(int(hx[i:i+2], 16) for i in (0, 2, 4))
    top, bottom = hex_to_rgb(c1), hex_to_rgb(c2)
    img = Image.new("RGB", (w, h), top)
    px = img.load()
    for y in range(h):
        t = y / max(h - 1, 1)
        r = int(top[0] + (bottom[0] - top[0]) * t)
        g = int(top[1] + (bottom[1] - top[1]) * t)
        b = int(top[2] + (bottom[2] - top[2]) * t)
        for x in range(w):
            px[x, y] = (r, g, b)
    return img


def fit_font(draw, text, max_width, start_size, font_path, min_size=14):
    size = start_size
    while size > min_size:
        font = ImageFont.truetype(font_path, size)
        bbox = draw.textbbox((0, 0), text, font=font)
        if bbox[2] - bbox[0] <= max_width:
            return font
        size -= 2
    return ImageFont.truetype(font_path, min_size)


def render_photo(seed, w, h):
    c1, c2 = colors_for(seed)
    img = make_gradient(w, h, c1, c2)
    # subtle diagonal texture
    overlay = Image.new("RGBA", (w, h), (255, 255, 255, 0))
    odraw = ImageDraw.Draw(overlay)
    step = max(int(min(w, h) / 12), 40)
    for x in range(-h, w, step):
        odraw.line([(x, 0), (x + h, h)], fill=(255, 255, 255, 18), width=2)
    img = Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")

    draw = ImageDraw.Draw(img)
    label = label_for(seed)
    font = fit_font(draw, label, w * 0.82, int(h * 0.11), FONT_BOLD)
    bbox = draw.textbbox((0, 0), label, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    cx, cy = w / 2, h / 2
    # translucent plate behind text for legibility
    pad_x, pad_y = 28, 18
    draw.rounded_rectangle(
        [cx - tw / 2 - pad_x, cy - th / 2 - pad_y, cx + tw / 2 + pad_x, cy + th / 2 + pad_y],
        radius=14, fill=(0, 0, 0, 90)
    )
    draw.text((cx - tw / 2 - bbox[0], cy - th / 2 - bbox[1]), label, font=font, fill=(255, 255, 255))

    sub = f"{w}×{h}  ·  replace: assets/images/{seed}.jpg"
    sfont = ImageFont.truetype(FONT_REG, max(int(h * 0.028), 13))
    sbbox = draw.textbbox((0, 0), sub, font=sfont)
    sw = sbbox[2] - sbbox[0]
    draw.text((cx - sw / 2 - sbbox[0], cy + th / 2 + pad_y + 14), sub, font=sfont, fill=(255, 255, 255, 210))
    return img


def render_avatar(seed, size):
    c1, c2 = colors_for(seed)
    img = make_gradient(size, size, c1, c2)
    draw = ImageDraw.Draw(img)
    initials = initials_for(seed)
    font = fit_font(draw, initials, size * 0.5, int(size * 0.42), FONT_BOLD)
    bbox = draw.textbbox((0, 0), initials, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    cx, cy = size / 2, size / 2
    draw.text((cx - tw / 2 - bbox[0], cy - th / 2 - bbox[1] - size * 0.05), initials, font=font, fill=(255, 255, 255))

    label = label_for(seed)
    sfont = ImageFont.truetype(FONT_REG, max(int(size * 0.065), 13))
    sbbox = draw.textbbox((0, 0), label, font=sfont)
    sw = sbbox[2] - sbbox[0]
    if sw > size * 0.86:
        sfont = fit_font(draw, label, size * 0.86, int(size * 0.065), FONT_REG)
        sbbox = draw.textbbox((0, 0), label, font=sfont)
        sw = sbbox[2] - sbbox[0]
    draw.text((cx - sw / 2 - sbbox[0], size * 0.72), label, font=sfont, fill=(255, 255, 255, 230))
    return img


# Gender-coded illustrated bust avatars — a step up from plain initials tiles for
# named people (students/faculty/toppers): a simple flat-icon silhouette (head +
# shoulders) with a gendered hairstyle, so it reads as "a person" rather than a
# color swatch at a glance. Deliberately abstract/non-photorealistic (no facial
# photo-realism) since these are still placeholders meant to be replaced.
GENDER = {
    "s1": "female", "s2": "male", "s3": "female",
    "arvind-menon": "male", "priya-raghavan": "female",
    "rakesh-chauhan": "male", "sanya-kapoor": "female",
    "imran-siddiqui": "male", "neha-verma": "female",
    "karan-malhotra": "male", "ritu-nair": "female",
    "devansh-rao": "male", "ankit-yadav": "male", "meera-pillai": "female",
    "aditya-bose": "male", "simran-kaur": "female", "rohit-sinha": "male",
    "ishita-ghosh": "female", "varun-kapoor": "male", "ananya-iyer": "female",
    "fatima-sheikh": "female", "karthik-nair": "male", "pooja-reddy": "female",
    "aarav-sharma": "male", "rhea-kapoor": "female",
    "diya-patel": "female", "vihaan-gupta": "male", "anaya-joshi": "female",
    "kabir-khan": "male", "sara-ahmed": "female", "reyansh-rao": "male",
    "myra-desai": "female", "neelam-joshi": "female", "parth-malhotra": "male",
    "gauri-nambiar": "female", "yash-trivedi": "male", "ira-bhatt": "female",
    "om-prakash": "male",
    "commenter-1": "male", "commenter-2": "female", "commenter-3": "male",
}


def render_person_avatar(seed, size, gender):
    c1, c2 = colors_for(seed)
    img = make_gradient(size, size, c1, c2).convert("RGBA")
    draw = ImageDraw.Draw(img, "RGBA")
    cx = size / 2
    skin = (255, 240, 227, 255)
    hair = (46, 34, 28, 255)

    head_r = size * 0.185
    head_cy = size * 0.40

    # Shoulders / bust (rounded shape, bottom of frame)
    shoulder_w = size * 0.98
    shoulder_top = size * 0.66
    draw.ellipse([cx - shoulder_w / 2, shoulder_top, cx + shoulder_w / 2, shoulder_top + size * 0.55], fill=skin)

    # Hair + head shape, gender-coded silhouette. Made deliberately BOLD/unmistakable
    # (not a subtle silhouette tweak) so the two styles read as different at a glance
    # even at small thumbnail sizes:
    #   - male: a compact short crop that stays entirely above the ears
    #   - female: a full frame around the head PLUS two long locks that hang
    #     down past the shoulders — unmistakably "long hair" from a distance
    if gender == "female":
        hair_w, hair_h = head_r * 2.55, head_r * 2.3
        hair_top = head_cy - head_r * 1.15
        draw.rounded_rectangle(
            [cx - hair_w / 2, hair_top, cx + hair_w / 2, hair_top + hair_h],
            radius=hair_w * 0.42, fill=hair,
        )
        # Long locks past the shoulders (the unmistakable "long hair" signal)
        lock_w = head_r * 0.5
        lock_top = head_cy + head_r * 0.35
        lock_bottom = shoulder_top + size * 0.14
        for side in (-1, 1):
            lx = cx + side * (head_r * 0.95)
            draw.rounded_rectangle(
                [lx - lock_w / 2, lock_top, lx + lock_w / 2, lock_bottom],
                radius=lock_w * 0.5, fill=hair,
            )
    else:
        draw.pieslice([cx - head_r * 1.05, head_cy - head_r * 1.35, cx + head_r * 1.05, head_cy - head_r * 0.35],
                       185, 355, fill=hair)

    draw.ellipse([cx - head_r * 0.9, head_cy - head_r * 0.82, cx + head_r * 0.9, head_cy + head_r], fill=skin)

    # Minimal friendly face: two dot eyes + a soft smile arc
    eye_y = head_cy + head_r * 0.02
    eye_dx = head_r * 0.36
    eye_r = max(head_r * 0.075, 2)
    eye_col = (70, 55, 48, 255)
    for dx in (-eye_dx, eye_dx):
        draw.ellipse([cx + dx - eye_r, eye_y - eye_r, cx + dx + eye_r, eye_y + eye_r], fill=eye_col)
    smile_w = head_r * 0.75
    draw.arc([cx - smile_w / 2, eye_y + head_r * 0.18, cx + smile_w / 2, eye_y + head_r * 0.72],
              start=15, end=165, fill=(150, 110, 90, 220), width=max(2, int(size * 0.012)))

    # Name label near the bottom edge, on a translucent plate for legibility
    label = label_for(seed)
    sfont = ImageFont.truetype(FONT_REG, max(int(size * 0.062), 13))
    sbbox = draw.textbbox((0, 0), label, font=sfont)
    sw, sh = sbbox[2] - sbbox[0], sbbox[3] - sbbox[1]
    if sw > size * 0.86:
        sfont = fit_font(draw, label, size * 0.86, int(size * 0.062), FONT_REG)
        sbbox = draw.textbbox((0, 0), label, font=sfont)
        sw, sh = sbbox[2] - sbbox[0], sbbox[3] - sbbox[1]
    plate_y = size * 0.885
    draw.rounded_rectangle([cx - sw / 2 - 10, plate_y - sh / 2 - 6, cx + sw / 2 + 10, plate_y + sh / 2 + 6],
                            radius=8, fill=(0, 0, 0, 100))
    draw.text((cx - sw / 2 - sbbox[0], plate_y - sh / 2 - sbbox[1]), label, font=sfont, fill=(255, 255, 255, 235))
    return img.convert("RGB")


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    for seed, (w, h, kind) in sorted(SPECS.items()):
        if kind == "avatar" and seed in GENDER:
            img = render_person_avatar(seed, w, GENDER[seed])
        elif kind == "avatar":
            img = render_avatar(seed, w)
        else:
            img = render_photo(seed, w, h)
        out_path = os.path.join(OUT_DIR, f"{seed}.jpg")
        img.convert("RGB").save(out_path, "JPEG", quality=82, optimize=True)
    print(f"Generated {len(SPECS)} placeholder images into {OUT_DIR}")


if __name__ == "__main__":
    main()
