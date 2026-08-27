# -*- coding: utf-8 -*-
"""
Shared content/data fixtures for the LS Academy coaching-institute
HTML template. Kept separate from build.py so it's easy for a developer
(or Claude, on a future edit) to swap in real content later.
"""

def img(seed, w=800, h=600, grayscale=False):
    # Local placeholder file (see src/gen_placeholders.py) — root-relative path.
    # Templates prefix this with {{ rel }} so it resolves correctly at any depth.
    return f"assets/images/{seed}.jpg"

def avatar(seed, size=200):
    return f"assets/images/{seed}.jpg"

SITE = {
    "name": "LS Academy",
    "short_name": "LS Academy",
    "tagline": "India's most trusted coaching institute for Banking, SSC, Civil Services, Engineering & Medical entrance exams — expert faculty, adaptive mock tests and real results.",
    "url": "https://ls-academy.example.com",
    "og_image": img("ls-academy-og", 1200, 630),
    "phone": "+91 98765 43210",
    "phone_alt": "+91 11 4567 8901",
    "email": "hello@lsacademy.example.com",
    "support_email": "support@lsacademy.example.com",
    "address": "4th Floor, Vertex Business Park, Sector 62, Noida, Uttar Pradesh 201301",
    "map_embed": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3502.019!2d77.362!3d28.627!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2zMjjCsDM3JzQ3LjAiTiA3N8KwMjEnNDMuMCJF!5e0!3m2!1sen!2sin!4v1700000000000",
    "stats": {"students": 24000, "selections": 3200, "faculty": 85, "centers": 18},
}

EXAM_CATEGORIES = [
    {
        "slug": "banking",
        "name": "Banking Exams",
        "icon": "bi-bank",
        "short": "SBI PO/Clerk, IBPS PO/Clerk/RRB, RBI Grade B",
        "description": "Crack SBI, IBPS, RBI and NABARD exams with structured quant, reasoning, English and banking-awareness modules, backed by sectional and full-length mocks on the latest pattern.",
        "exams": ["SBI PO", "SBI Clerk", "IBPS PO", "IBPS Clerk", "IBPS RRB", "RBI Grade B"],
        "duration": "6 months",
        "students": 6800,
        "fee": 14999,
        "fee_old": 19999,
        "rating": 4.8,
        "image": img("banking-exam-prep", 900, 650),
    },
    {
        "slug": "ssc",
        "name": "SSC Exams",
        "icon": "bi-file-earmark-text",
        "short": "SSC CGL, CHSL, MTS, GD, Stenographer",
        "description": "Comprehensive coverage of Quantitative Aptitude, Reasoning, English and General Awareness tailored to SSC's tier-wise exam pattern, with daily practice sets and speed drills.",
        "exams": ["SSC CGL", "SSC CHSL", "SSC MTS", "SSC GD", "SSC Stenographer"],
        "duration": "5 months",
        "students": 5400,
        "fee": 12999,
        "fee_old": 16999,
        "rating": 4.7,
        "image": img("ssc-exam-prep", 900, 650),
    },
    {
        "slug": "civil-services",
        "name": "Civil Services (UPSC)",
        "icon": "bi-bank2",
        "short": "UPSC CSE Prelims, Mains & Interview",
        "description": "An integrated Prelims-cum-Mains programme covering GS I-IV, CSAT, optional subjects and answer-writing practice, with weekly current-affairs sessions and mentor-guided interviews.",
        "exams": ["UPSC Prelims", "UPSC Mains", "State PCS", "UPSC Interview"],
        "duration": "12 months",
        "students": 3100,
        "fee": 45999,
        "fee_old": 59999,
        "rating": 4.9,
        "image": img("upsc-civil-services", 900, 650),
    },
    {
        "slug": "engineering",
        "name": "Engineering Entrance (JEE)",
        "icon": "bi-gear",
        "short": "JEE Main & Advanced, state CETs",
        "description": "Concept-first Physics, Chemistry and Mathematics taught by IIT alumni, reinforced with chapter tests, All-India test series and rank-improvement workshops for JEE Main & Advanced.",
        "exams": ["JEE Main", "JEE Advanced", "BITSAT", "State CET"],
        "duration": "24 months",
        "students": 5200,
        "fee": 68999,
        "fee_old": 84999,
        "rating": 4.8,
        "image": img("jee-engineering-prep", 900, 650),
    },
    {
        "slug": "medical",
        "name": "Medical Entrance (NEET)",
        "icon": "bi-heart-pulse",
        "short": "NEET-UG Physics, Chemistry & Biology",
        "description": "NCERT-anchored Biology, Physics and Chemistry modules with 500+ mock tests, previous-year paper analysis and doubt-clearing labs designed around the NEET-UG blueprint.",
        "exams": ["NEET-UG", "AIIMS Prep", "State Medical CET"],
        "duration": "24 months",
        "students": 4900,
        "fee": 68999,
        "fee_old": 84999,
        "rating": 4.9,
        "image": img("neet-medical-prep", 900, 650),
    },
]

FACULTY = [
    {"name": "Dr. Arvind Menon", "role": "Head of Quant & Reasoning", "qual": "Ph.D. Mathematics, IIT Delhi", "exp": "16 yrs",
     "bio": "Ex-SBI probationary officer turned mentor; has coached 40+ national toppers in banking exams.",
     "photo": avatar("arvind-menon", 300), "subject": "banking"},
    {"name": "Priya Raghavan", "role": "English & Verbal Ability Lead", "qual": "M.A. English, JNU", "exp": "12 yrs",
     "bio": "Specialist in exam-oriented grammar and reading comprehension for SSC & banking aspirants.",
     "photo": avatar("priya-raghavan", 300), "subject": "ssc"},
    {"name": "Rakesh Chauhan", "role": "General Studies Mentor (UPSC)", "qual": "Ex-IAS (Retd.), M.Phil Political Science", "exp": "20 yrs",
     "bio": "Former district collector guiding UPSC aspirants on GS strategy, ethics and interview readiness.",
     "photo": avatar("rakesh-chauhan", 300), "subject": "civil-services"},
    {"name": "Dr. Sanya Kapoor", "role": "Physics Faculty (JEE/NEET)", "qual": "Ph.D. Physics, IIT Bombay", "exp": "14 yrs",
     "bio": "Known for simplifying mechanics and electrodynamics through first-principles problem solving.",
     "photo": avatar("sanya-kapoor", 300), "subject": "engineering"},
    {"name": "Dr. Imran Siddiqui", "role": "Biology Faculty (NEET)", "qual": "MBBS, M.D.", "exp": "11 yrs",
     "bio": "Practicing physician who translates NCERT biology into high-yield, exam-ready concepts.",
     "photo": avatar("imran-siddiqui", 300), "subject": "medical"},
    {"name": "Neha Verma", "role": "Chemistry Faculty (JEE/NEET)", "qual": "M.Sc. Chemistry, BHU", "exp": "10 yrs",
     "bio": "Builds strong organic-chemistry fundamentals through visual reaction mapping techniques.",
     "photo": avatar("neha-verma", 300), "subject": "engineering"},
    {"name": "Karan Malhotra", "role": "Quantitative Aptitude Faculty (SSC)", "qual": "B.Tech, M.Sc. Statistics", "exp": "9 yrs",
     "bio": "Creator of the institute's popular '20-minute speed maths' drills used by 10,000+ students.",
     "photo": avatar("karan-malhotra", 300), "subject": "ssc"},
    {"name": "Dr. Ritu Nair", "role": "Current Affairs & GK Mentor", "qual": "Ph.D. Economics", "exp": "13 yrs",
     "bio": "Curates the institute's daily current-affairs digest read by over 18,000 aspirants every morning.",
     "photo": avatar("ritu-nair", 300), "subject": "civil-services"},
]

TESTIMONIALS = [
    {"name": "Ankit Yadav", "result": "SBI PO 2025 · AIR 18", "quote": "The sectional mocks were harder than the real exam — that's exactly why I cleared it comfortably. LS Academy's analytics showed me my weak topics weeks before the exam.",
     "photo": avatar("ankit-yadav", 200), "rating": 5},
    {"name": "Simran Kaur", "result": "SSC CGL 2025 · Selected, Income Tax Inspector", "quote": "Daily speed-maths drills changed my approach to the quant section completely. I went from 40% to 88% accuracy in three months.",
     "photo": avatar("simran-kaur", 200), "rating": 5},
    {"name": "Devansh Rao", "result": "UPSC CSE 2024 · AIR 142", "quote": "The mentor-guided answer writing sessions were the single biggest reason I cleared Mains. Personal feedback on every essay made all the difference.",
     "photo": avatar("devansh-rao", 200), "rating": 5},
    {"name": "Meera Pillai", "result": "JEE Advanced 2025 · AIR 890", "quote": "Faculty explained concepts from first principles instead of shortcuts, so nothing felt like rote learning. The All-India test series kept me honest about my rank.",
     "photo": avatar("meera-pillai", 200), "rating": 4.5},
    {"name": "Aditya Bose", "result": "NEET-UG 2025 · AIR 512", "quote": "500+ mock tests meant exam day felt like just another test. The topic-wise performance tracker showed exactly where to focus in the last month.",
     "photo": avatar("aditya-bose", 200), "rating": 5},
    {"name": "Fatima Sheikh", "result": "IBPS RRB 2025 · Selected, Office Assistant", "quote": "I was working full time, so the recorded live classes and mobile-friendly dashboard let me study on my commute. Cleared it in my second attempt.",
     "photo": avatar("fatima-sheikh", 200), "rating": 4.5},
]

RESULTS = [
    {"name": "Devansh Rao", "exam": "UPSC CSE 2024", "rank": "AIR 142", "photo": avatar("devansh-rao", 240), "course": "civil-services", "year": 2024},
    {"name": "Ankit Yadav", "exam": "SBI PO 2025", "rank": "AIR 18", "photo": avatar("ankit-yadav", 240), "course": "banking", "year": 2025},
    {"name": "Meera Pillai", "exam": "JEE Advanced 2025", "rank": "AIR 890", "photo": avatar("meera-pillai", 240), "course": "engineering", "year": 2025},
    {"name": "Aditya Bose", "exam": "NEET-UG 2025", "rank": "AIR 512", "photo": avatar("aditya-bose", 240), "course": "medical", "year": 2025},
    {"name": "Simran Kaur", "exam": "SSC CGL 2025", "rank": "AIR 63", "photo": avatar("simran-kaur", 240), "course": "ssc", "year": 2025},
    {"name": "Rohit Sinha", "exam": "IBPS PO 2025", "rank": "AIR 41", "photo": avatar("rohit-sinha", 240), "course": "banking", "year": 2025},
    {"name": "Ishita Ghosh", "exam": "UPSC CSE 2024", "rank": "AIR 276", "photo": avatar("ishita-ghosh", 240), "course": "civil-services", "year": 2024},
    {"name": "Varun Kapoor", "exam": "JEE Main 2025", "rank": "99.7 %ile", "photo": avatar("varun-kapoor", 240), "course": "engineering", "year": 2025},
    {"name": "Ananya Iyer", "exam": "NEET-UG 2024", "rank": "AIR 1204", "photo": avatar("ananya-iyer", 240), "course": "medical", "year": 2024},
    {"name": "Fatima Sheikh", "exam": "IBPS RRB 2025", "rank": "Selected", "photo": avatar("fatima-sheikh", 240), "course": "banking", "year": 2025},
    {"name": "Karthik Nair", "exam": "SSC CHSL 2024", "rank": "AIR 29", "photo": avatar("karthik-nair", 240), "course": "ssc", "year": 2024},
    {"name": "Pooja Reddy", "exam": "State PCS 2025", "rank": "AIR 8", "photo": avatar("pooja-reddy", 240), "course": "civil-services", "year": 2025},
]

BLOG_POSTS = [
    {"slug": "smart-study-plan-banking-2026", "category": "banking", "category_label": "Banking",
     "title": "How to Build a Smart 6-Month Study Plan for SBI & IBPS 2026",
     "excerpt": "A week-by-week roadmap covering quant, reasoning, English and banking awareness — with revision cycles that actually stick.",
     "date": "August 12, 2026", "author": "Dr. Arvind Menon", "read_time": "7 min read",
     "image": img("study-plan-banking", 900, 600), "tags": ["Strategy", "Banking", "Time Management"]},
    {"slug": "ssc-cgl-tier2-tips", "category": "ssc", "category_label": "SSC",
     "title": "SSC CGL Tier 2: 9 High-Yield Topics You Can't Afford to Skip",
     "excerpt": "Not all topics carry equal weight. Here's where toppers spend 70% of their revision time in the final month.",
     "date": "August 5, 2026", "author": "Karan Malhotra", "read_time": "6 min read",
     "image": img("ssc-tier2-tips", 900, 600), "tags": ["SSC", "Exam Pattern"]},
    {"slug": "upsc-answer-writing-framework", "category": "civil-services", "category_label": "Civil Services",
     "title": "The 3-Part Framework Toppers Use for UPSC Mains Answer Writing",
     "excerpt": "Introduction, body, conclusion isn't enough. Learn the structure that consistently scores 15+ per 150-word answer.",
     "date": "July 29, 2026", "author": "Rakesh Chauhan", "read_time": "9 min read",
     "image": img("upsc-answer-writing", 900, 600), "tags": ["UPSC", "Mains", "Answer Writing"]},
    {"slug": "jee-physics-mechanics-mistakes", "category": "engineering", "category_label": "Engineering",
     "title": "7 Mechanics Mistakes That Cost JEE Aspirants 20+ Marks",
     "excerpt": "Sign convention errors, frame-of-reference slips and other silent rank-killers — and how to eliminate them.",
     "date": "July 21, 2026", "author": "Dr. Sanya Kapoor", "read_time": "5 min read",
     "image": img("jee-mechanics-mistakes", 900, 600), "tags": ["JEE", "Physics"]},
    {"slug": "neet-biology-ncert-strategy", "category": "medical", "category_label": "Medical",
     "title": "Why NCERT Biology Alone Can Get You 320+ in NEET",
     "excerpt": "A line-by-line reading strategy for NCERT Biology that converts textbook facts into exam-ready recall.",
     "date": "July 14, 2026", "author": "Dr. Imran Siddiqui", "read_time": "6 min read",
     "image": img("neet-biology-strategy", 900, 600), "tags": ["NEET", "Biology"]},
    {"slug": "mock-test-analysis-habit", "category": "exam-tips", "category_label": "Exam Tips",
     "title": "The Post-Mock-Test Habit That Separates Toppers from the Rest",
     "excerpt": "Taking a mock test is only half the job. Here's the 20-minute review ritual our AIR-1 students swear by.",
     "date": "July 3, 2026", "author": "Dr. Ritu Nair", "read_time": "4 min read",
     "image": img("mock-test-analysis", 900, 600), "tags": ["Mock Tests", "Strategy"]},
]

FAQS_GENERAL = [
    {"q": "Do you offer both online and offline (classroom) coaching?",
     "a": "Yes. All programmes are available as live online classes with recordings, in-person classroom batches across 18 centers, or a hybrid mode — you can switch modes anytime from your student dashboard."},
    {"q": "What is included in the mock-test library?",
     "a": "Every plan includes subject-wise tests, sectional tests and full-length mocks on the latest exam pattern, each with instant scoring, an all-India percentile, and a question-by-question correct/incorrect breakdown."},
    {"q": "Can I switch from one exam category to another later?",
     "a": "Absolutely — many students preparing for banking also attempt SSC. You can add an additional exam category to your dashboard at a discounted bundle rate from the Fees page."},
    {"q": "Do you provide study material and previous year papers?",
     "a": "Yes, downloadable PDFs of topic notes, formula sheets and 10+ years of previous year papers are available in the Study Material section of the student dashboard."},
    {"q": "Is there a free trial before I enroll?",
     "a": "Yes — book a free demo class and get 3 free mock tests to experience the platform before choosing a plan."},
    {"q": "How do I track my improvement over time?",
     "a": "The Performance Tracker on your dashboard plots topic-wise accuracy and score trends across every test you attempt, highlighting weak areas that need more practice."},
]

FAQS_COURSE = [
    {"q": "What is the batch size for live classes?", "a": "We cap live batches at 60 students to ensure faculty can address individual doubts during and after sessions."},
    {"q": "Are recorded lectures available if I miss a class?", "a": "Yes, every live session is recorded and available in your dashboard within 2 hours, with unlimited replays until your course validity ends."},
    {"q": "How many mock tests are included?", "a": "This programme includes 120+ sectional tests and 40 full-length mock tests mapped to the latest official exam pattern."},
    {"q": "Is doubt-clearing support available?", "a": "Yes — a dedicated doubt-clearing forum plus weekly live Q&A sessions with subject faculty are included at no extra cost."},
    {"q": "What if I don't clear the exam in the first attempt?", "a": "Our re-enrollment policy offers a 40% discount on the next attempt's programme for students who complete 80%+ of the course content."},
    {"q": "Do you provide a printed study kit?", "a": "Comprehensive and Elite plans include a printed study kit shipped to your address; Foundation plan includes downloadable PDFs only."},
]

PRICING_PLANS = [
    {"name": "Foundation", "tagline": "For self-paced starters", "monthly": 1499, "yearly": 14999, "popular": False,
     "features": [
        ("Access to recorded video lectures", True),
        ("50 subject-wise mock tests", True),
        ("Downloadable study notes (PDF)", True),
        ("Live doubt-clearing classes", False),
        ("Personal mentor sessions", False),
        ("Printed study kit", False),
     ]},
    {"name": "Comprehensive", "tagline": "Our most popular plan", "monthly": 2999, "yearly": 28999, "popular": True,
     "features": [
        ("Everything in Foundation", True),
        ("Live interactive classes (daily)", True),
        ("150+ sectional & full mock tests", True),
        ("Weekly live doubt-clearing sessions", True),
        ("Printed study kit shipped home", True),
        ("1:1 mentor sessions", False),
     ]},
    {"name": "Elite Mentorship", "tagline": "For serious rank-seekers", "monthly": 5499, "yearly": 52999, "popular": False,
     "features": [
        ("Everything in Comprehensive", True),
        ("Weekly 1:1 mentor sessions", True),
        ("Personalised study planner", True),
        ("Priority doubt resolution (< 2 hrs)", True),
        ("Mock interview & GD practice", True),
        ("Result-linked scholarship eligibility", True),
     ]},
]

NOTIFICATIONS = [
    {"icon": "bi-award", "title": "New mock test 'SSC CGL Full Mock #14' is live", "time": "10 minutes ago"},
    {"icon": "bi-calendar-event", "title": "Live class: Quant Speed Techniques at 6:00 PM today", "time": "1 hour ago"},
    {"icon": "bi-file-earmark-pdf", "title": "New study material uploaded: Banking Awareness Notes", "time": "3 hours ago"},
    {"icon": "bi-chat-left-text", "title": "Faculty replied to your doubt in Reasoning forum", "time": "Yesterday"},
    {"icon": "bi-trophy", "title": "You moved up to Rank #42 in this week's leaderboard", "time": "2 days ago"},
]

STUDENT_USER = {"name": "Aarav Sharma", "email": "aarav.sharma@example.com", "phone": "+91 98450 11223", "avatar": avatar("aarav-sharma", 200), "course": "Banking Exams (SBI/IBPS)", "member_since": "12 Jan 2026"}
ADMIN_USER = {"name": "Rhea Kapoor", "email": "rhea.kapoor@lsacademy.example.com", "phone": "+91 98765 43210", "avatar": avatar("rhea-kapoor", 200), "role": "Super Admin", "member_since": "04 Mar 2024"}

def _gen_palette(total, fresh=False):
    """Deterministic, purely-cosmetic question-palette state list for the
    test-attempt screen (no real per-question grading data behind it)."""
    states = []
    progress = max(2, round(total * 0.55))
    for i in range(1, total + 1):
        if i == 1:
            states.append("current")
        elif fresh:
            states.append("")
        elif i % 11 == 0:
            states.append("not-answered")
        elif i % 5 == 0:
            states.append("marked")
        elif i <= progress:
            states.append("answered")
        else:
            states.append("")
    return states

MOCK_TESTS = [
    {
        "name": "SBI PO Prelims Full Mock #12", "slug": "sbi-po-prelims-12", "category": "Banking", "type": "Full-length",
        "questions": 100, "duration": 60, "difficulty": "Moderate", "attempts": 3, "best_score": 78,
        "attempt": {
            "section": "Quantitative Aptitude",
            "question": "A sum of ₹12,500 is invested at compound interest of 8% per annum. What will be the amount after 2 years (compounded annually)?",
            "options": [("A", "₹14,580"), ("B", "₹14,580.00"), ("C", "₹14,580.80"), ("D", "₹13,500")],
            "selected": "C",
        },
        "report": {
            "date": "18 Aug 2026", "correct": 80, "incorrect": 8, "skipped": 12,
            "percentile": 92, "time_taken": "54m", "rank": "Rank #187", "out_of": "8,420 attempts",
            "sections": [
                ("Quantitative Aptitude", 22, 2, 1, 92),
                ("Reasoning Ability", 19, 4, 2, 83),
                ("English Language", 21, 1, 3, 95),
                ("General Awareness", 18, 1, 6, 95),
            ],
            "review": [
                ("A train 150m long crosses a platform of 200m in 20 seconds. What is the speed of the train in km/hr?", "B) 63 km/hr", "B) 63 km/hr", "correct"),
                ("If 'CHAIR' is coded as 'DIBJS', how is 'TABLE' coded?", "C) UBCMF", "D) UBCMG", "incorrect"),
                ("Which Indian city hosts the headquarters of the Reserve Bank of India?", "Not attempted", "B) Mumbai", "skipped"),
            ],
        },
    },
    {
        "name": "Quantitative Aptitude — Simplification & Approximation", "slug": "quant-simplification", "category": "Banking", "type": "Subject-wise",
        "questions": 25, "duration": 20, "difficulty": "Easy", "attempts": 5, "best_score": 88,
        "attempt": {
            "section": "Quantitative Aptitude",
            "question": "What approximate value should come in place of the question mark? 48.92% of 649.87 + 15.03% of 320.16 ≈ ?",
            "options": [("A", "342"), ("B", "350"), ("C", "366"), ("D", "378")],
            "selected": "C",
        },
        "report": {
            "date": "20 Aug 2026", "correct": 22, "incorrect": 1, "skipped": 2,
            "percentile": 95, "time_taken": "17m", "rank": "Rank #42", "out_of": "3,150 attempts",
            "sections": [("Quantitative Aptitude — Simplification & Approximation", 22, 1, 2, 96)],
            "review": [
                ("Simplify: (2/5 of 350) + (3/7 of 490) = ?", "B) 350", "B) 350", "correct"),
                ("Find the approximate value: √2499.98 + √624.97 ≈ ?", "A) 68", "C) 75", "incorrect"),
                ("What is 34.98% of 850.02, approximately?", "Not attempted", "B) 298", "skipped"),
            ],
        },
    },
    {
        "name": "Reasoning — Puzzles & Seating Arrangement", "slug": "reasoning-puzzles", "category": "Banking", "type": "Subject-wise",
        "questions": 30, "duration": 25, "difficulty": "Hard", "attempts": 2, "best_score": 61,
        "attempt": {
            "section": "Reasoning Ability",
            "question": "Eight friends P, Q, R, S, T, U, V and W sit around a circular table facing the centre. R sits third to the right of P. Who sits immediately to the left of R?",
            "options": [("A", "Q"), ("B", "S"), ("C", "T"), ("D", "Cannot be determined")],
            "selected": "D",
        },
        "report": {
            "date": "15 Aug 2026", "correct": 18, "incorrect": 8, "skipped": 4,
            "percentile": 58, "time_taken": "24m", "rank": "Rank #612", "out_of": "2,980 attempts",
            "sections": [("Reasoning Ability — Puzzles & Seating Arrangement", 18, 8, 4, 69)],
            "review": [
                ("In a row of 12 children facing north, A is fourth from the left and B is fifth from the right. How many children are between A and B?", "B) 3", "B) 3", "correct"),
                ("Rahul walks 5 km towards north, turns right and walks 3 km, then turns right again and walks 5 km. How far is he from his starting point?", "A) 8 km", "C) 3 km", "incorrect"),
                ("In a certain code, 'BOOK' is written as 'CPPL'. How is 'PAGE' written in that code?", "Not attempted", "D) QBHF", "skipped"),
            ],
        },
    },
    {
        "name": "IBPS Clerk Mains Full Mock #08", "slug": "ibps-clerk-mains-08", "category": "Banking", "type": "Full-length",
        "questions": 190, "duration": 160, "difficulty": "Moderate", "attempts": 1, "best_score": 65,
        "attempt": {
            "section": "General & Financial Awareness",
            "question": "Which committee's recommendations led to the establishment of Regional Rural Banks (RRBs) in India?",
            "options": [("A", "Narasimham Working Group (1975)"), ("B", "Kelkar Committee"), ("C", "Rangarajan Committee"), ("D", "Nachiket Mor Committee")],
            "selected": "A",
        },
        "report": {
            "date": "10 Aug 2026", "correct": 124, "incorrect": 46, "skipped": 20,
            "percentile": 71, "time_taken": "142m", "rank": "Rank #2,340", "out_of": "31,860 attempts",
            "sections": [
                ("General & Financial Awareness", 28, 14, 8, 67),
                ("English Language", 30, 6, 4, 83),
                ("Reasoning Ability & Computer Aptitude", 34, 10, 6, 77),
                ("Quantitative Aptitude", 32, 16, 2, 67),
            ],
            "review": [
                ("Which of the following is NOT a function of the Reserve Bank of India?", "C) Sanctioning individual home loans", "C) Sanctioning individual home loans", "correct"),
                ("A cheque with the words 'Account Payee' written between the two parallel crossing lines is called a ______ crossing.", "B) Special crossing", "C) Account Payee crossing", "incorrect"),
                ("What does the banking term 'NPA' stand for?", "Not attempted", "B) Non-Performing Asset", "skipped"),
            ],
        },
    },
    {
        "name": "English — Reading Comprehension Set 6", "slug": "english-rc-set6", "category": "Banking", "type": "Subject-wise",
        "questions": 20, "duration": 15, "difficulty": "Moderate", "attempts": 4, "best_score": 82,
        "attempt": {
            "section": "English Language",
            "question": "Choose the word most similar in meaning to 'MERIDIAN' as used in the sentence: 'She was at the meridian of her career when she decided to mentor young analysts.'",
            "options": [("A", "Beginning"), ("B", "Peak"), ("C", "Decline"), ("D", "Midpoint")],
            "selected": "B",
        },
        "report": {
            "date": "22 Aug 2026", "correct": 16, "incorrect": 3, "skipped": 1,
            "percentile": 88, "time_taken": "13m", "rank": "Rank #98", "out_of": "4,760 attempts",
            "sections": [("English Language — Reading Comprehension", 16, 3, 1, 84)],
            "review": [
                ("Choose the correct synonym of 'PRUDENT':", "B) Wise", "B) Wise", "correct"),
                ("Identify the error in the sentence: 'Neither of the students have submitted their assignment.'", "A) Neither", "B) have", "incorrect"),
                ("Fill in the blank: 'The committee ______ its decision by Friday.'", "Not attempted", "A) will announce", "skipped"),
            ],
        },
    },
    {
        "name": "Banking & Financial Awareness — Monthly Capsule", "slug": "banking-awareness-capsule", "category": "Banking", "type": "Subject-wise",
        "questions": 40, "duration": 20, "difficulty": "Easy", "attempts": 2, "best_score": 91,
        "attempt": {
            "section": "Banking & Financial Awareness",
            "question": "Which body in India is responsible for deciding the repo rate under the inflation-targeting framework?",
            "options": [("A", "Monetary Policy Committee (MPC)"), ("B", "Board for Financial Supervision"), ("C", "Banks Board Bureau"), ("D", "Financial Stability and Development Council")],
            "selected": "A",
        },
        "report": {
            "date": "24 Aug 2026", "correct": 36, "incorrect": 2, "skipped": 2,
            "percentile": 97, "time_taken": "17m", "rank": "Rank #21", "out_of": "5,230 attempts",
            "sections": [("Banking & Financial Awareness", 36, 2, 2, 95)],
            "review": [
                ("The term 'Repo Rate' refers to the rate at which:", "A) RBI lends to commercial banks against securities", "A) RBI lends to commercial banks against securities", "correct"),
                ("Which of these is classified as a 'Scheduled Commercial Bank' in India?", "A) NABARD", "B) A public sector bank listed in the Second Schedule of the RBI Act", "incorrect"),
                ("'KYC' in banking stands for:", "Not attempted", "A) Know Your Customer", "skipped"),
            ],
        },
    },
    {
        "name": "SSC CGL Tier 1 Full Mock #21", "slug": "ssc-cgl-tier1-21", "category": "SSC", "type": "Full-length",
        "questions": 100, "duration": 60, "difficulty": "Moderate", "attempts": 0, "best_score": None,
        "attempt": {
            "section": "General Intelligence & Reasoning",
            "question": "In a certain code, 'RIVER' is written as 'SJWFS'. How is 'STONE' written in that code?",
            "options": [("A", "TUPOF"), ("B", "TUPOE"), ("C", "TUQOF"), ("D", "TVPOF")],
            "selected": None,
        },
        "report": None,
    },
    {
        "name": "General Awareness — Static GK Set 3", "slug": "gk-static-set3", "category": "SSC", "type": "Subject-wise",
        "questions": 25, "duration": 15, "difficulty": "Easy", "attempts": 1, "best_score": 72,
        "attempt": {
            "section": "General Awareness",
            "question": "Who was the first President of India?",
            "options": [("A", "Dr. Rajendra Prasad"), ("B", "Dr. S. Radhakrishnan"), ("C", "Zakir Hussain"), ("D", "V. V. Giri")],
            "selected": "A",
        },
        "report": {
            "date": "12 Aug 2026", "correct": 18, "incorrect": 5, "skipped": 2,
            "percentile": 64, "time_taken": "13m", "rank": "Rank #1,120", "out_of": "9,840 attempts",
            "sections": [("General Awareness — Static GK", 18, 5, 2, 78)],
            "review": [
                ("The Tropic of Cancer does NOT pass through which of these Indian states?", "B) Punjab", "B) Punjab", "correct"),
                ("Which Indian classical dance form originated in Tamil Nadu?", "A) Kathak", "B) Bharatanatyam", "incorrect"),
                ("The Wular Lake, the largest freshwater lake in India, is located in which state/UT?", "Not attempted", "A) Jammu & Kashmir", "skipped"),
            ],
        },
    },
]
for _t in MOCK_TESTS:
    _t["marks"] = 1 if _t["category"] == "Banking" else 2
    _t["negative"] = 0.25 if _t["category"] == "Banking" else 0.5
    _t["attempt"]["palette"] = _gen_palette(_t["questions"], fresh=(_t["attempts"] == 0))
    if _t["report"]:
        _t["report"]["total"] = _t["report"]["correct"] + _t["report"]["incorrect"] + _t["report"]["skipped"]
        assert _t["report"]["total"] == _t["questions"], _t["name"]

STUDY_MATERIALS = [
    {"title": "Banking Awareness — Complete Notes 2026", "type": "PDF", "size": "4.2 MB", "category": "Banking"},
    {"title": "Quant Formula Handbook", "type": "PDF", "size": "1.8 MB", "category": "Banking"},
    {"title": "SBI PO Previous Year Papers (2019–2025)", "type": "ZIP", "size": "12.6 MB", "category": "Banking"},
    {"title": "Reasoning Shortcut Techniques", "type": "PDF", "size": "3.1 MB", "category": "Banking"},
    {"title": "SSC CGL Previous Year Papers (2018–2025)", "type": "ZIP", "size": "15.4 MB", "category": "SSC"},
    {"title": "Current Affairs — August 2026 Capsule", "type": "PDF", "size": "2.4 MB", "category": "General"},
    {"title": "English Grammar Rules & Practice Set", "type": "PDF", "size": "2.9 MB", "category": "Banking"},
    {"title": "Computer Aptitude Quick Notes", "type": "PDF", "size": "1.5 MB", "category": "Banking"},
]

SCHEDULE_ITEMS = [
    {"day": "Today, 21 Aug", "time": "6:00 PM – 7:30 PM", "title": "Live Class: Quant — Speed Maths Techniques", "faculty": "Dr. Arvind Menon", "type": "class"},
    {"day": "Today, 21 Aug", "time": "8:00 PM – 8:45 PM", "title": "Doubt Clearing Session — Reasoning", "faculty": "Karan Malhotra", "type": "doubt"},
    {"day": "Tomorrow, 22 Aug", "time": "10:00 AM – 11:00 AM", "title": "SBI PO Prelims Full Mock #13", "faculty": "Test Portal", "type": "exam"},
    {"day": "Sat, 24 Aug", "time": "5:00 PM – 6:30 PM", "title": "Live Class: English — Cloze Test Strategy", "faculty": "Priya Raghavan", "type": "class"},
    {"day": "Sun, 25 Aug", "time": "9:00 AM – 12:00 PM", "title": "Weekly Full-Length Mock Test", "faculty": "Test Portal", "type": "exam"},
    {"day": "Mon, 26 Aug", "time": "6:00 PM – 7:00 PM", "title": "Live Class: Banking Awareness Capsule Review", "faculty": "Dr. Ritu Nair", "type": "class"},
]

ADMIN_STUDENTS = [
    {"name": "Aarav Sharma", "email": "aarav.sharma@example.com", "course": "Banking", "joined": "12 Jan 2026", "status": "active", "avatar": avatar("aarav-sharma", 100)},
    {"name": "Diya Patel", "email": "diya.patel@example.com", "course": "SSC", "joined": "03 Feb 2026", "status": "active", "avatar": avatar("diya-patel", 100)},
    {"name": "Vihaan Gupta", "email": "vihaan.gupta@example.com", "course": "Civil Services", "joined": "19 Nov 2025", "status": "active", "avatar": avatar("vihaan-gupta", 100)},
    {"name": "Anaya Joshi", "email": "anaya.joshi@example.com", "course": "Engineering (JEE)", "joined": "27 Mar 2026", "status": "trial", "avatar": avatar("anaya-joshi", 100)},
    {"name": "Kabir Khan", "email": "kabir.khan@example.com", "course": "Medical (NEET)", "joined": "08 Aug 2026", "status": "active", "avatar": avatar("kabir-khan", 100)},
    {"name": "Sara Ahmed", "email": "sara.ahmed@example.com", "course": "Banking", "joined": "15 May 2025", "status": "suspended", "avatar": avatar("sara-ahmed", 100)},
    {"name": "Reyansh Rao", "email": "reyansh.rao@example.com", "course": "SSC", "joined": "22 Jul 2026", "status": "active", "avatar": avatar("reyansh-rao", 100)},
    {"name": "Myra Desai", "email": "myra.desai@example.com", "course": "Civil Services", "joined": "30 Dec 2025", "status": "trial", "avatar": avatar("myra-desai", 100)},
]

ADMIN_ORDERS = [
    {"id": "ORD-10231", "student": "Aarav Sharma", "plan": "Comprehensive — Banking", "amount": 28999, "date": "18 Aug 2026", "status": "success"},
    {"id": "ORD-10230", "student": "Diya Patel", "plan": "Foundation — SSC", "amount": 14999, "date": "18 Aug 2026", "status": "success"},
    {"id": "ORD-10229", "student": "Kabir Khan", "plan": "Elite Mentorship — NEET", "amount": 84999, "date": "17 Aug 2026", "status": "pending"},
    {"id": "ORD-10228", "student": "Anaya Joshi", "plan": "Comprehensive — JEE", "amount": 28999, "date": "17 Aug 2026", "status": "success"},
    {"id": "ORD-10227", "student": "Sara Ahmed", "plan": "Foundation — Banking", "amount": 14999, "date": "16 Aug 2026", "status": "refunded"},
    {"id": "ORD-10226", "student": "Reyansh Rao", "plan": "Comprehensive — SSC", "amount": 28999, "date": "15 Aug 2026", "status": "success"},
    {"id": "ORD-10225", "student": "Myra Desai", "plan": "Foundation — Civil Services", "amount": 45999, "date": "14 Aug 2026", "status": "failed"},
    {"id": "ORD-10224", "student": "Vihaan Gupta", "plan": "Elite Mentorship — Civil Services", "amount": 52999, "date": "12 Aug 2026", "status": "success"},
]

ADMIN_MESSAGES = [
    {"name": "Neelam Joshi", "email": "neelam.joshi@example.com", "subject": "Question about SSC CGL batch timings", "preview": "Hi, I wanted to check if there's a weekend-only batch available for the SSC CGL comprehensive plan...", "time": "9:42 AM", "unread": True, "avatar": avatar("neelam-joshi", 100)},
    {"name": "Parth Malhotra", "email": "parth.malhotra@example.com", "subject": "Refund request for ORD-10225", "preview": "I would like to request a refund for my recent enrollment as I've decided to defer my UPSC attempt...", "time": "8:15 AM", "unread": True, "avatar": avatar("parth-malhotra", 100)},
    {"name": "Gauri Nambiar", "email": "gauri.nambiar@example.com", "subject": "Unable to access recorded lecture", "preview": "The recording for yesterday's Physics live class isn't playing on my dashboard, could you help...", "time": "Yesterday", "unread": False, "avatar": avatar("gauri-nambiar", 100)},
    {"name": "Yash Trivedi", "email": "yash.trivedi@example.com", "subject": "Corporate batch enquiry for 40 employees", "preview": "We're an HR consultancy looking to enroll 40 employees preparing for banking exams. Could you share...", "time": "Yesterday", "unread": True, "avatar": avatar("yash-trivedi", 100)},
    {"name": "Ira Bhatt", "email": "ira.bhatt@example.com", "subject": "Study material not downloading", "preview": "The Banking Awareness PDF gives an error when I try to download it from the materials section...", "time": "2 days ago", "unread": False, "avatar": avatar("ira-bhatt", 100)},
    {"name": "Om Prakash", "email": "om.prakash@example.com", "subject": "Switching from SSC to Banking track", "preview": "I've decided to prepare for banking exams instead of SSC. Is it possible to switch my existing plan...", "time": "3 days ago", "unread": False, "avatar": avatar("om-prakash", 100)},
]
