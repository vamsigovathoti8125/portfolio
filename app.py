from pathlib import Path
import base64

import streamlit as st


st.set_page_config(
    page_title="Govathoti Vamsi — Software Developer",
    page_icon="assets/favicon.jpg",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# Replace the values in this section with your own details and project links.
PROFILE = {
    "name": "Govathoti Vamsi",
    "role": "Software developer · AI/ML engineer",
    "intro": "I’m a curious software builder who moves between code, data, intelligent systems, and real-world problem solving.",
    "location": "Hyderabad, India · Electronics & Communication Engineering",
    "email": "vamsigovathoti8125@gmail.com",
    "phone": "8125723070",
    "github": "https://github.com/vamsigovathoti8125",
    "linkedin": "https://www.linkedin.com/in/vamsigovathoti8125/",
    "availability": "Open to software & AI/ML opportunities",
    "looking_for": "I’m looking for software development, backend, AI/ML, and frontend opportunities where I can build useful products and grow with a strong engineering team.",
    "about": (
        "I’m Govathoti Vamsi, an Electronics and Communication Engineering graduate who enjoys "
        "building things that make technology feel useful. I have created e-commerce products, "
        "AI study assistants, computer-vision classifiers, real-time safety systems, and frontend "
        "experiments — not just websites. I like taking an idea from a rough problem statement to "
        "a working product: understanding the user, choosing the right tools, testing the result, "
        "and improving the details that make it reliable. My interests sit at the intersection of "
        "software engineering, AI/ML, automation, data, and creative interfaces."
    ),
}

EXPERIENCE = {
    "title": "AI/ML Intern — APSCHE & SmartInternz",
    "date": "April 25 — July 2025 · Remote",
    "image": "pro exp 3.png",
    "overview": "Built Smart Sorting, a deep-learning web application that classifies uploaded fruit and vegetable images as fresh or rotten across 16 categories.",
    "details": [
        "Developed Smart Sorting: Rotten vs Fresh Fruit & Vegetable Classification Using Transfer Learning with Python, TensorFlow, Flask, and OpenCV.",
        "Trained and evaluated a MobileNetV2 transfer-learning pipeline on 32,769 images across 16 fresh and rotten fruit and vegetable classes, reaching approximately 95% accuracy.",
        "Debugged class-label mapping and prediction inconsistencies, then tested fresh and rotten categories to improve inference reliability.",
        "Built a Flask interface where users upload an image and receive a real-time prediction, supporting food quality control, smart packaging, and agricultural workflows.",
    ],
    "dataset": "32,769 images across 16 classes: 8 fresh and 8 rotten fruit and vegetable categories.",
    "workflow": "Image upload → OpenCV preprocessing → MobileNetV2 inference → class prediction → Base64 image preview and result display.",
    "impact": "Approximately 95% accuracy with low loss after tuning and corrected class-index mapping.",
    "link": "https://github.com/vamsigovathoti8125/smart-sorting-transfer-learning-for-identifying-rotten-fruits-and-vegetables",
}

EDUCATION = {
    "college": "Seshadri Rao Gudlavalleru Engineering College",
    "degree": "B.Tech in Electronics and Communication Engineering",
    "date": "2022 — 2026",
    "result": "CGPA: 7.69 / 10",
}

SKILL_GROUPS = {
    "Programming": "Python · Java · C · JavaScript",
    "Core programming": "OOP · Data Structures · Algorithms · Problem Solving · Debugging · Exception Handling",
    "Backend development": "Flask · FastAPI · REST API Fundamentals · API Development · Deployment",
    "Database": "SQL · MySQL · DBMS · Database Fundamentals",
    "Web technologies": "HTML5 · CSS3 · JavaScript · React.js · Tailwind CSS",
    "AI / ML": "Machine Learning · Deep Learning · CNN · Computer Vision · TensorFlow · OpenCV · Dlib",
    "Generative AI": "RAG · LLMs · Agentic AI · Prompt Engineering · Embeddings · Semantic Search · FAISS",
    "Frameworks & tools": "Streamlit · Git · GitHub · Git Branching · VS Code",
    "Computer science": "Operating Systems · Computer Networks · Software Development · Model Evaluation",
    "Cloud & systems": "AWS Fundamentals · CI/CD Fundamentals · Linux Fundamentals",
}

SKILL_ICONS = [
    ("Python", "python/python-original.svg"),
    ("Java", "java/java-original.svg"),
    ("C", "c/c-original.svg"),
    ("JavaScript", "javascript/javascript-original.svg"),
    ("HTML5", "html5/html5-original.svg"),
    ("CSS3", "css3/css3-original.svg"),
    ("React", "react/react-original.svg"),
    ("Tailwind", "tailwindcss/tailwindcss-original.svg"),
    ("Flask", "flask/flask-original.svg"),
    ("FastAPI", "fastapi/fastapi-original.svg"),
    ("MySQL", "mysql/mysql-original.svg"),
    ("SQLite", "sqlite/sqlite-original.svg"),
    ("TensorFlow", "tensorflow/tensorflow-original.svg"),
    ("OpenCV", "opencv/opencv-original.svg"),
    ("Git", "git/git-original.svg"),
    ("GitHub", "github/github-original.svg"),
    ("Linux", "linux/linux-original.svg"),
    ("AWS", "amazonwebservices/amazonwebservices-original-wordmark.svg"),
    ("VS Code", "vscode/vscode-original.svg"),
]

PROJECTS = [
    {
        "number": "01",
        "title": "vamsiMart",
        "description": "Built a multipage e-commerce site with category browsing, search, price sorting, load-more pagination, product details, persistent account-specific carts, checkout, payment options, and order history.",
        "tags": ["Node.js", "Express.js", "SQLite"],
        "accent": "coral",
        "logo": "🛒",
        "logo_label": "SHOP / SYSTEM",
        "impact": "735+ products · JWT accounts · checkout flow",
        "link": "https://github.com/vamsigovathoti8125/ecommerce-vamsiMart",
        "image": "pro exp 1.png",
        "readme": "A marketplace-style ecommerce platform with 735+ generated products across Electronics, Fashion, Beauty, Home, Grocery, Appliances, and Sports. It includes search, category filtering, price sorting, product pages, persistent carts, JWT login, checkout, UPI/card/net-banking/COD options, and order history.",
    },
    {
        "number": "02",
        "title": "StudyMind AI",
        "description": "Built a Streamlit study assistant that processes uploaded PDFs through chunking, embeddings, FAISS vector search, query classification, agent routing, and LLM-powered responses. Achieved 94% query-answering accuracy with responses below 15 seconds.",
        "tags": ["Python", "Streamlit", "RAG"],
        "accent": "blue",
        "logo": "✦",
        "logo_label": "READ / THINK",
        "impact": "94% answer accuracy · under 15 seconds",
        "link": "https://github.com/vamsigovathoti8125/studymindai-rag",
        "image": "project explaining 2.png",
        "readme": "An agentic RAG study assistant that accepts PDF notes, extracts page text, creates overlapping chunks, builds a FAISS semantic index, and answers questions from retrieved context. It also supports quiz generation, safe arithmetic, saved indexes, Gemini when available, and a local fallback when no API key is configured.",
    },
    {
        "number": "03",
        "title": "Job Application Tracker",
        "description": "Built a responsive frontend application for managing the full job-search lifecycle, from adding and editing applications to filtering statuses and exporting a portable CSV backup.",
        "tags": ["HTML", "CSS", "JavaScript"],
        "accent": "lime",
        "logo": "✓",
        "logo_label": "TRACK / GROW",
        "impact": "CRUD workflow · localStorage · CSV export",
        "link": "https://github.com/vamsigovathoti8125/job-application-tracker",
        "image": "image.png",
        "readme": "A frontend-only job search workspace with CRUD operations for company, role, location, date, status, URL, and notes. It includes search by company, role, or location; Applied, Interview, Offer, Rejected, and Withdrawn filters; dashboard statistics; localStorage persistence with separate username workspaces; CSV export; responsive layouts; and client-side URL validation.",
    },
    {
        "number": "04",
        "title": "Driver Safety AI",
        "description": "A real-time drowsiness and distraction detection system using facial landmarks, EAR/MAR signals, ESP32 alerts, and Blynk notifications.",
        "tags": ["Python", "Dlib", "ESP32"],
        "accent": "purple",
        "logo": "◉",
        "logo_label": "SENSE / ALERT",
        "impact": "Real-time signals · ESP32 alerts · Blynk",
        "link": "#",
        "image": "pro exp 4.png",
        "readme": "A real-time driver monitoring concept that uses facial landmarks, Eye Aspect Ratio, and Mouth Aspect Ratio to identify drowsiness, distraction, eye closure, and yawning. ESP32 and Blynk integrations are used for connected alerts and mobile notifications.",
    },
]

ROOT = Path(__file__).parent
PHOTO = ROOT / "assets" / "profile.png"
RESUME = ROOT / "assets" / "Vamsi_Govathoti_Resume.pdf"
ASSETS = ROOT / "assets"

skill_rows = "".join(
    f'<div class="skill-group"><strong>{name}</strong><span>{skills}</span></div>'
    for name, skills in SKILL_GROUPS.items()
)
skill_icons = "".join(
    f'<div class="icon-skill"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/{path}" alt="{name} logo"><span>{name}</span></div>'
    for name, path in SKILL_ICONS
)
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=DM+Sans:wght@400;500;700&family=Playfair+Display:ital,wght@0,600;1,600&display=swap');

    :root {
        --ink: #f8f6ff;
        --paper: #08080d;
        --muted: #aaa7b7;
        --line: rgba(248, 246, 255, .16);
        --coral: #bf63ff;
        --blue: #5fbdff;
        --lime: #caff32;
    }
    .stApp { background: var(--paper); color: var(--ink); }
    html { scroll-behavior: smooth; }
    .block-container { max-width: 1040px; padding: 22px 28px 55px; }
    header[data-testid="stHeader"] { background: transparent; }
    [data-testid="stSidebar"], [data-testid="collapsedControl"] { display: none; }
    .topbar {
        align-items: center; border-bottom: 1px solid var(--line); display: flex;
        justify-content: space-between; padding-bottom: 18px;
    }
    .brand, .brand:visited, .brand:hover, .brand:active { color: var(--coral) !important; font-family: 'DM Sans', sans-serif; font-size: 17px; font-weight: 700; letter-spacing: -.04em; text-decoration: none !important; }
    .nav { color: var(--muted); font-family: 'DM Mono', monospace; font-size: 11px; letter-spacing: .08em; }
    .nav a { color: inherit; margin-left: 24px; text-decoration: none; }
    .nav a:hover { color: var(--lime); }
    [id] { scroll-margin-top: 24px; }
    .topbar { position: sticky; top: 0; z-index: 20; background: rgba(8,8,13,.92); padding-top: 12px; }
    .eyebrow { color: var(--muted); font: 11px 'DM Mono', monospace; letter-spacing: .15em; text-transform: uppercase; }
    .hero { min-height: 610px; padding: 72px 0 86px; position: relative; }
    .hero h1 {
        font: 700 clamp(58px, 10vw, 145px)/.82 'DM Sans', sans-serif;
        letter-spacing: -.09em; margin: 34px 0 26px; max-width: 860px;
    }
    .hero h1 em { color: var(--coral); font-weight: 600; }
    .hero-copy { color: var(--muted); font: 16px/1.6 'DM Sans', sans-serif; max-width: 355px; }
    .hero-side {
        align-items: center; display: flex; font: 11px 'DM Mono', monospace;
        gap: 14px; margin-top: 55px; text-transform: uppercase;
    }
    .dot { background: var(--coral); border-radius: 50%; height: 9px; width: 9px; }
    .photo-wrap { margin-top: 16px; position: relative; }
    .photo-wrap img { aspect-ratio: 4/5; border-radius: 0 0 46% 46%; object-fit: cover; object-position: center top; width: 100%; }
    .photo-wrap:after {
        border: 1px solid var(--ink); border-radius: 0 0 46% 46%; content: '';
        height: 100%; left: 13px; position: absolute; top: 13px; width: 100%; z-index: -1;
    }
    .section { border-top: 1px solid var(--line); padding: 72px 0; }
    .section-title { font: 700 clamp(35px, 5vw, 67px)/.9 'DM Sans', sans-serif; letter-spacing: -.08em; margin: 0; }
    .section-title em { color: var(--coral); }
    .about-text { font: 22px/1.4 'DM Sans', sans-serif; letter-spacing: -.025em; max-width: 565px; }
    .meta { color: var(--muted); font: 12px/1.7 'DM Mono', monospace; text-transform: uppercase; }
    .info-panel { background: #15151f; border: 1px solid var(--line); border-radius: 20px; padding: 24px; }
    .experience-card-link, .experience-card-link:visited, .experience-card-link:hover, .experience-card-link:active { color: inherit !important; display: block; text-decoration: none !important; }
    .experience-card-link * { text-decoration: none !important; }
    .experience-card { transition: border-color .25s ease, box-shadow .25s ease, transform .25s ease; }
    .experience-card-link:hover .experience-card { border-color: var(--lime); box-shadow: 0 18px 45px rgba(191,99,255,.14); transform: translateY(-4px); }
    .info-panel h3 { font: 700 25px 'DM Sans', sans-serif; letter-spacing: -.06em; margin: 10px 0; }
    .info-panel p, .info-panel li { color: var(--muted); font: 13px/1.55 'DM Sans', sans-serif; }
    .info-panel ul { margin: 12px 0 0; padding-left: 18px; }
    .capability-grid { display: grid; gap: 12px; grid-template-columns: repeat(3, 1fr); margin-top: 28px; }
    .capability { background: #15151f; border: 1px solid var(--line); border-radius: 18px; padding: 20px; }
    .capability b { color: var(--lime); display: block; font: 700 24px 'DM Sans', sans-serif; margin-bottom: 8px; }
    .capability span { color: var(--muted); font: 12px/1.5 'DM Sans', sans-serif; }
    .project-card { background: #15151f; border: 1px solid var(--line); border-radius: 19px; padding: 18px; min-height: 345px; }
    .project-card-link, .project-card-link:visited, .project-card-link:hover, .project-card-link:active { color: inherit !important; display: block; text-decoration: none !important; }
    .project-card-link * { text-decoration: none !important; }
    .project-card h3 { font: 700 24px/1.05 'DM Sans', sans-serif; letter-spacing: -.06em; margin: 0 0 10px; }
    .project-card p { color: var(--muted); font: 15px/1.55 'DM Sans', sans-serif; margin: 0 0 12px; max-width: 430px; }
    .project-impact { color: var(--lime); font: 10px/1.5 'DM Mono', monospace; margin-bottom: 15px; text-transform: uppercase; }
    .project-number { color: var(--muted); font: 12px 'DM Mono', monospace; }
    .pill { border: 1px solid var(--line); border-radius: 100px; display: inline-block; font: 10px 'DM Mono', monospace; margin: 0 5px 5px 0; padding: 7px 11px; text-transform: uppercase; }
    .project-accent { border-radius: 13px; height: 160px; margin: 0 0 18px; overflow: hidden; position: relative; }
    .project-accent:before { border: 1px solid rgba(255,255,255,.5); border-radius: 50%; content: ''; height: 240px; position: absolute; right: -64px; top: -120px; transform: rotate(18deg); width: 240px; }
    .project-accent:after { background: rgba(255,255,255,.18); border-radius: 50%; bottom: -42px; content: ''; filter: blur(1px); height: 120px; left: -30px; position: absolute; width: 120px; }
    .project-grid { background-image: linear-gradient(rgba(255,255,255,.12) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,.12) 1px, transparent 1px); background-size: 22px 22px; inset: 0; opacity: .35; position: absolute; transform: perspective(260px) rotateX(58deg) scale(1.5); transform-origin: bottom; }
    .project-logo { align-items: center; backdrop-filter: blur(10px); background: rgba(8,8,13,.3); border: 1px solid rgba(255,255,255,.78); border-radius: 27px; box-shadow: 10px 10px 0 rgba(8,8,13,.18), inset 0 0 20px rgba(255,255,255,.13); color: #fff; display: flex; font: 400 58px/1 'DM Sans', sans-serif; height: 88px; justify-content: center; position: absolute; right: 25%; top: 31px; transform: rotate(-8deg); width: 88px; z-index: 2; }
    .project-logo-label { background: rgba(8,8,13,.48); border: 1px solid rgba(255,255,255,.45); border-radius: 100px; bottom: 15px; color: #fff; font: 10px 'DM Mono', monospace; left: 15px; letter-spacing: .12em; padding: 8px 11px; position: absolute; z-index: 3; }
    .project-orbit { border: 1px solid rgba(255,255,255,.62); border-radius: 50%; height: 130px; position: absolute; right: 14%; top: 10px; transform: rotate(-25deg); width: 195px; z-index: 1; }
    .project-orbit:after { background: #fff; border-radius: 50%; box-shadow: 0 0 14px #fff; content: ''; height: 7px; left: 7px; position: absolute; top: 29px; width: 7px; }
    .coral { background: linear-gradient(135deg, #ff6b6b, #bf63ff 65%, #4d2c83); } .blue { background: linear-gradient(135deg, #176bff, #5fbdff 60%, #203b9a); } .lime { background: linear-gradient(135deg, #7cad16, #caff32 58%, #247a5d); } .purple { background: linear-gradient(135deg, #44208c, #8154e8 58%, #d75cff); }
    .skills { background: #15151f; border: 1px solid var(--line); border-radius: 20px; margin-top: 35px; padding: 26px; }
    .skill-group { border-top: 1px solid var(--line); display: grid; gap: 8px; grid-template-columns: 180px 1fr; padding: 15px 0; }
    .skill-group strong { color: var(--lime); font: 11px 'DM Mono', monospace; text-transform: uppercase; }
    .skill-group span { color: var(--muted); font: 13px/1.45 'DM Sans', sans-serif; }
    .icon-skill-grid { display: grid; gap: 18px 10px; grid-template-columns: repeat(10, 1fr); margin: 18px 0 26px; }
    .icon-skill { align-items: center; border-radius: 14px; display: flex; flex-direction: column; gap: 9px; min-width: 0; padding: 10px 4px; transition: background .25s ease, transform .25s ease; }
    .icon-skill:hover { background: rgba(202,255,50,.08); transform: translateY(-7px); }
    .icon-skill img { height: 42px; object-fit: contain; width: 42px; }
    .icon-skill span { color: var(--muted); font: 10px 'DM Mono', monospace; text-align: center; }
    .skills-divider { background: var(--line); height: 1px; margin: 8px 0 6px; }
    .showcase { align-items: center; background: linear-gradient(100deg, #202039, #171721); border: 1px solid var(--line); border-radius: 20px; display: flex; gap: 28px; margin-top: 28px; padding: 25px; }
    .showcase-art { background: radial-gradient(circle at 70% 30%, #d75cff, #22214f 38%, #12121c 70%); border-radius: 15px; flex: 1.2; min-height: 150px; position: relative; }
    .showcase-art:after { border: 2px solid var(--lime); border-radius: 50%; content: ''; height: 80px; position: absolute; right: 20%; top: 22%; width: 80px; }
    .showcase-copy { flex: 1; }
    .showcase-copy h3 { font: 700 25px 'DM Sans', sans-serif; letter-spacing: -.06em; margin: 10px 0; }
    .showcase-copy p { color: var(--muted); font: 13px/1.5 'DM Sans', sans-serif; }
    .skill { background: #262634; border: 1px solid rgba(202,255,50,.35); border-radius: 100px; color: var(--lime); display: inline-block; font: 11px 'DM Mono', monospace; margin: 5px; padding: 10px 14px; text-transform: uppercase; }
    .contact { background: #15151f; border: 1px solid var(--line); border-radius: 22px; color: var(--ink); margin-top: 45px; padding: 64px 8vw; }
    .contact .section-title { color: var(--ink); max-width: 700px; }
    .contact a { color: var(--ink); font: 16px 'DM Mono', monospace; text-decoration: none; }
    .contact-links { display: flex; flex-wrap: wrap; gap: 11px; margin-top: 26px; }
    .contact-link { border: 1px solid var(--line); border-radius: 100px; color: var(--ink); font: 11px 'DM Mono', monospace; padding: 11px 15px; text-decoration: none; transition: background .2s ease, color .2s ease, transform .2s ease; }
    .contact-link:hover { background: var(--lime); color: #101019; transform: translateY(-3px); }
    .hero-actions { display: flex; flex-wrap: wrap; gap: 10px; margin-top: 22px; }
    .hero-action { border: 1px solid var(--line); border-radius: 100px; color: var(--ink) !important; font: 11px 'DM Mono', monospace; padding: 11px 15px; text-decoration: none !important; transition: background .2s ease, color .2s ease, transform .2s ease; }
    .hero-action:hover { background: var(--lime); color: #101019 !important; transform: translateY(-3px); }
    .hero-action:focus-visible, .contact-link:focus-visible, .nav a:focus-visible, .project-card-link:focus-visible { outline: 2px solid var(--lime); outline-offset: 4px; }
    .availability { border-left: 2px solid var(--lime); color: var(--muted); font: 14px/1.6 'DM Sans', sans-serif; margin-top: 25px; max-width: 620px; padding-left: 16px; }
    .achievement-grid { display: grid; gap: 12px; grid-template-columns: repeat(3, 1fr); margin-top: 28px; }
    .achievement { background: #15151f; border: 1px solid var(--line); border-radius: 18px; padding: 20px; }
    .achievement b { color: var(--lime); display: block; font: 700 18px 'DM Sans', sans-serif; margin-bottom: 7px; }
    .achievement span { color: var(--muted); font: 12px/1.5 'DM Sans', sans-serif; }
    .focus-list { color: var(--muted); font: 13px/1.7 'DM Sans', sans-serif; margin: 10px 0 0; padding-left: 18px; }
    .footer { color: var(--muted); display: flex; font: 11px 'DM Mono', monospace; justify-content: space-between; padding-top: 24px; text-transform: uppercase; }
    .reference-hero { background: radial-gradient(circle at 80% 20%, #37225c 0, #101019 35%, #08080d 72%); border: 1px solid var(--line); border-radius: 30px; min-height: 535px; overflow: hidden; position: relative; }
    .reference-hero:before { background: var(--coral); border-radius: 50%; content: ''; filter: blur(2px); height: 240px; left: -110px; opacity: .8; position: absolute; top: -105px; width: 330px; }
    .reference-hero:after { border: 1px solid rgba(202,255,50,.5); border-radius: 50%; content: ''; height: 470px; position: absolute; right: -220px; top: 160px; width: 470px; }
    .reference-photo { bottom: -20px; max-height: 82%; max-width: 47%; object-fit: contain; object-position: bottom center; position: absolute; right: 4%; z-index: 1; }
    .reference-copy { padding: 100px 45% 70px 8%; position: relative; z-index: 2; }
    .reference-copy h1 { font: 700 clamp(50px, 7vw, 96px)/.82 'DM Sans', sans-serif; letter-spacing: -.09em; margin: 30px 0; }
    .reference-copy h1 em { color: var(--coral); }
    .reference-copy p { color: var(--muted); font: 14px/1.55 'DM Sans', sans-serif; max-width: 440px; }
    .reference-copy a { color: var(--ink); display: inline-block; font: 13px 'DM Mono', monospace; margin-top: 14px; text-decoration: none; }
    .reference-rule { background: var(--line); height: 1px; max-width: 300px; }
    .hero-kicker { color: var(--lime); font: 11px 'DM Mono', monospace; letter-spacing: .14em; text-transform: uppercase; }
    .float-badge { animation: drift 5s ease-in-out infinite; background: var(--lime); border-radius: 50%; color: #101019; display: grid; font: 700 11px 'DM Mono', monospace; height: 78px; place-items: center; position: absolute; right: 9%; top: 11%; transform: rotate(10deg); width: 78px; z-index: 3; }
    .hero-scroll { bottom: 24px; color: var(--muted); font: 10px 'DM Mono', monospace; left: 8%; letter-spacing: .15em; position: absolute; text-transform: uppercase; z-index: 3; }
    .hero-scroll:before { background: var(--lime); border-radius: 50%; content: ''; display: inline-block; height: 7px; margin-right: 9px; width: 7px; }
    .marquee { border-bottom: 1px solid var(--line); border-top: 1px solid var(--line); color: var(--lime); font: 700 18px 'DM Sans', sans-serif; letter-spacing: .1em; margin: 26px 0 0; overflow: hidden; padding: 12px 0; text-transform: uppercase; white-space: nowrap; }
    .marquee span { animation: marquee 22s linear infinite; display: inline-block; }
    @keyframes drift { 0%,100% { margin-top: 0; } 50% { margin-top: 16px; } }
    @keyframes marquee { from { transform: translateX(0); } to { transform: translateX(-35%); } }
    @keyframes rise { from { opacity: 0; transform: translateY(22px); } to { opacity: 1; transform: translateY(0); } }
    .reference-hero, .showcase, .project-card, .info-panel, .skills, .contact { animation: rise .8s ease both; }
    .project-card { transition: transform .3s ease, border-color .3s ease, box-shadow .3s ease; }
    .project-card:hover { border-color: var(--lime); box-shadow: 0 18px 45px rgba(191,99,255,.18); transform: translateY(-10px) rotate(-1deg); }
    .project-card:hover .project-accent { transform: scale(.96) rotate(2deg); }
    .project-accent { transition: transform .3s ease; }
    .project-detail h4 { color: var(--lime); font: 700 20px 'DM Sans', sans-serif; margin: 0 0 8px; }
    .project-detail p { color: var(--muted); font: 13px/1.55 'DM Sans', sans-serif; margin: 0; }
    .project-detail a { color: var(--ink); display: inline-block; font: 11px 'DM Mono', monospace; margin-top: 13px; text-decoration: none; }
    div[role="dialog"] { background: #101019; border: 1px solid rgba(202,255,50,.4); border-radius: 24px; }
    div[role="dialog"] img { border-radius: 18px; max-height: 430px; object-fit: contain; }
    div[role="dialog"] h2 { color: var(--lime); font: 700 38px 'DM Sans', sans-serif; letter-spacing: -.07em; }
    div[role="dialog"] p { color: var(--muted); font: 15px/1.65 'DM Sans', sans-serif; }
    div[role="dialog"] .stButton button { border: 1px solid var(--lime); border-radius: 100px; }
    .section-title em { display: inline-block; }
    div[data-testid="stVerticalBlock"] > div:has(> .section) { margin-bottom: 0; }
    @media (max-width: 700px) {
        .block-container { padding-left: 24px; padding-right: 24px; }
        .nav a { margin-left: 10px; }
        .hero { min-height: auto; padding-top: 50px; }
        .hero h1 { font-size: 66px; }
        .contact { margin-left: -24px; margin-right: -24px; padding: 64px 24px; }
        .footer { gap: 18px; flex-direction: column; }
        .reference-hero { display: flex; flex-direction: column; min-height: 0; }
        .reference-copy { order: 1; padding: 64px 8% 30px; }
        .reference-copy h1 { font-size: clamp(50px, 16vw, 76px); }
        .reference-copy p { max-width: none; }
        .reference-photo { align-self: flex-end; bottom: auto; max-height: none; max-width: none; object-fit: contain; position: relative; right: auto; width: 78%; z-index: 1; }
        .float-badge { right: 7%; top: 5%; z-index: 3; }
        .hero-scroll { display: none; }
        .showcase { align-items: stretch; flex-direction: column; }
        .icon-skill-grid { grid-template-columns: repeat(4, 1fr); }
        .capability-grid, .achievement-grid { grid-template-columns: 1fr; }
        .project-logo { right: 28%; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)


@st.dialog("Project details", width="large")
def show_project_details(project):
    image_path = ASSETS / project["image"]
    left, right = st.columns([0.9, 1.1], gap="large")
    with left:
        if image_path.exists():
            st.image(str(image_path), width="stretch")
        st.caption(f'{project["number"]} / {project["title"]}')
    with right:
        st.markdown(f"## {project['title']}")
        st.markdown(f"**What it is**  \n{project['description']}")
        st.markdown(f"**How it works**  \n{project['readme']}")
        st.markdown(f"**Technology stack**  \n{' · '.join(project['tags'])}")
        st.markdown(f"**Impact**  \n{project['impact']}")
        st.markdown("This project demonstrates how I move from a real problem to a usable product: planning the flow, building the core system, testing the result, and refining the experience.")
        if project["link"] != "#":
            st.link_button("View source repository", project["link"], width="stretch")
        else:
            st.info("Prototype — repository details available on request.")
        if st.button("Close project details", key=f'close-{project["number"]}', width="stretch"):
            st.query_params.clear()
            st.rerun()


@st.dialog("Experience details", width="large")
def show_experience_details():
    image_path = ASSETS / EXPERIENCE["image"]
    left, right = st.columns([0.9, 1.1], gap="large")
    with left:
        if image_path.exists():
            st.image(str(image_path), width="stretch")
        st.caption("AI/ML internship case study")
    with right:
        st.markdown(f"## {EXPERIENCE['title']}")
        st.markdown(f"**Duration**  \n{EXPERIENCE['date']}")
        st.markdown(f"**Project**  \n{EXPERIENCE['overview']}")
        st.markdown(f"**Dataset**  \n{EXPERIENCE['dataset']}")
        st.markdown(f"**System workflow**  \n{EXPERIENCE['workflow']}")
        st.markdown(f"**Result**  \n{EXPERIENCE['impact']}")
        st.markdown(
            "**Implementation**  \n"
            "The work covered data collection and preprocessing, CNN and transfer-learning "
            "experiments, evaluation and accuracy tuning, model/class-index saving, Flask "
            "integration, and deployment preparation."
        )
        st.markdown(
            "**Technology stack**  \n"
            "Python · TensorFlow/Keras · MobileNetV2 · Flask · OpenCV · HTML · CSS"
        )
        st.markdown(
            "**Use cases**  \n"
            "Food sorting systems, supply-chain checks, agricultural quality control, smart "
            "packaging, and academic research."
        )
    st.link_button("View internship project repository", EXPERIENCE["link"], width="stretch")
    if st.button("Close experience details", key="close-experience", width="stretch"):
        st.query_params.clear()
        st.rerun()


selected_project_key = st.query_params.get("project")
selected_project = next(
    (project for project in PROJECTS if project["title"].lower().replace(" ", "-") == selected_project_key),
    None,
)
selected_experience = st.query_params.get("experience")
if selected_project is not None:
    st.query_params.clear()
    show_project_details(selected_project)
elif selected_experience == "internship":
    st.query_params.clear()
    show_experience_details()


st.markdown(
    f"""
    <div class="topbar">
        <a class="brand" href="#top">{PROFILE["name"]}</a>
        <div class="nav"><a href="#work">Work</a><a href="#about">About</a><a href="#skills">Skills</a><a href="#contact">Contact</a></div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div id="top"></div>', unsafe_allow_html=True)
if PHOTO.exists():
    photo_data = base64.b64encode(PHOTO.read_bytes()).decode("ascii")
    resume_actions = ""
    if RESUME.exists():
        resume_data = base64.b64encode(RESUME.read_bytes()).decode("ascii")
        resume_actions = (
            f'<a class="hero-action" href="data:application/pdf;base64,{resume_data}" '
            'target="_blank" rel="noreferrer">See resume ↗</a>'
            f'<a class="hero-action" href="data:application/pdf;base64,{resume_data}" '
            'download="Vamsi_Govathoti_Resume.pdf">Download resume ↓</a>'
        )
    st.markdown(
        f"""
        <div class="reference-hero">
            <img class="reference-photo" src="data:image/png;base64,{photo_data}" alt="{PROFILE["name"]}">
            <div class="reference-copy">
                <div class="hero-kicker">Hello, I’m Vamsi ✦</div>
                <h1>Building<br><em>what’s next.</em></h1>
                <div class="reference-rule"></div>
                <p>{PROFILE["intro"]} I love turning ambitious ideas into clean, working experiences.</p>
                <div class="hero-actions">
                    <a class="hero-action" href="#work">See selected work ↘</a>
                    {resume_actions}
                    <a class="hero-action" href="{PROFILE["github"]}" target="_blank" rel="noreferrer">GitHub ↗</a>
                </div>
            </div>
            <div class="float-badge">LET’S<br>BUILD<br>✦</div>
            <div class="hero-scroll">Scroll to explore</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown(
    '<div class="marquee"><span>Python · AI / ML · Full-stack development · Computer vision · RAG · Creative problem solving · Python · AI / ML · Full-stack development · Computer vision · RAG · </span></div>',
    unsafe_allow_html=True,
)

st.markdown('<div id="about" class="section">', unsafe_allow_html=True)
about_left, about_right = st.columns([0.8, 1.25], gap="large")
with about_left:
    st.markdown('<div class="eyebrow">01 / About</div><h2 class="section-title">A little<br><em>about me.</em></h2>', unsafe_allow_html=True)
with about_right:
    st.markdown(
        f'<p class="about-text">{PROFILE["about"]}</p><p class="meta">{PROFILE["location"]}<br>{PROFILE["role"]}<br><br>Python · Java · JavaScript · SQL<br>TensorFlow · OpenCV · Streamlit · React</p>',
        unsafe_allow_html=True,
    )
st.markdown("</div>", unsafe_allow_html=True)

st.markdown(
    f"""
    <div class="capability-grid">
        <div class="capability"><b>01 / Build</b><span>Responsive products with thoughtful interfaces and dependable backend foundations.</span></div>
        <div class="capability"><b>02 / Explore</b><span>AI, retrieval, vision, and experiments that turn new technology into useful tools.</span></div>
        <div class="capability"><b>03 / Improve</b><span>Debug, measure, refine, and ship work that gets better with every iteration.</span></div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    f"""
    <section id="experience" class="section">
        <div class="eyebrow">02 / Experience & education</div>
        <div style="height:20px"></div>
        <a class="experience-card-link" href="?experience=internship#experience">
        <div class="info-panel experience-card">
            <div class="eyebrow">Experience</div>
            <h3>{EXPERIENCE["title"]}</h3>
            <p>{EXPERIENCE["date"]}</p>
            <p>{EXPERIENCE["overview"]}</p>
            <div class="meta">Open experience details ↗</div>
        </div>
        </a>
        <div style="height:14px"></div>
        <div class="info-panel">
            <div class="eyebrow">Education</div>
            <h3>{EDUCATION["college"]}</h3>
            <p>{EDUCATION["degree"]}<br>{EDUCATION["date"]} · {EDUCATION["result"]}</p>
        </div>
    </section>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div id="work" class="section">', unsafe_allow_html=True)
st.markdown('<div class="eyebrow">03 / Selected work</div><h2 class="section-title">Things I’ve<br><em>made.</em></h2>', unsafe_allow_html=True)
project_columns = st.columns(4, gap="small")
for column, project in zip(project_columns, PROJECTS):
    with column:
        tags = "".join(f'<span class="pill">{tag}</span>' for tag in project["tags"])
        st.markdown(
            f"""
            <a class="project-card-link" href="?project={project["title"].lower().replace(" ", "-")}#work" target="_self">
                <article class="project-card">
                    <div class="project-number">{project["number"]}</div>
                    <div class="project-accent {project["accent"]}">
                        <div class="project-grid"></div>
                        <div class="project-orbit"></div>
                        <div class="project-logo">{project["logo"]}</div>
                        <div class="project-logo-label">{project["logo_label"]}</div>
                    </div>
                    <h3>{project["title"]}</h3>
                    <p>{project["description"]}</p>
                    <div class="project-impact">{project["impact"]}</div>
                    <div>{tags}</div>
                    <div class="meta">Open project ↗</div>
                </article>
            </a>
            """,
            unsafe_allow_html=True,
        )
st.markdown("</div>", unsafe_allow_html=True)

st.markdown(
    f"""
    <section class="section">
        <div class="eyebrow">04 / What I’m looking for</div>
        <h2 class="section-title">Ready to<br><em>contribute.</em></h2>
        <p class="availability">{PROFILE["looking_for"]}</p>
        <div class="achievement-grid">
            <div class="achievement"><b>AI/ML internship</b><span>Built and evaluated a transfer-learning computer-vision product during an APSCHE & SmartInternz internship.</span></div>
            <div class="achievement"><b>Product mindset</b><span>From e-commerce flows to job-search tools, I focus on useful features, clear interfaces, and reliable behavior.</span></div>
            <div class="achievement"><b>Engineering range</b><span>Comfortable moving across Python, JavaScript, APIs, databases, computer vision, and retrieval systems.</span></div>
        </div>
    </section>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    f"""
    <section id="skills" class="skills">
        <div class="eyebrow">05 / Technical skills</div>
        <div class="icon-skill-grid">{skill_icons}</div>
        <div class="skills-divider"></div>
        <div class="eyebrow">Complete toolkit</div>
        {skill_rows}
    </section>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    f"""
    <section id="contact" class="contact">
        <div class="eyebrow">06 / Let’s work together</div>
        <h2 class="section-title">Have an idea?<br><em>Let’s make it real.</em></h2>
        <p class="meta">I’m open to software, AI/ML, computer-vision, and product engineering opportunities.</p>
        <div class="contact-links">
            <a class="contact-link" href="mailto:{PROFILE["email"]}">Email ↗</a>
            <a class="contact-link" href="tel:+91{PROFILE["phone"]}">+91 {PROFILE["phone"]}</a>
            <a class="contact-link" href="{PROFILE["github"]}" target="_blank" rel="noreferrer">GitHub ↗</a>
            <a class="contact-link" href="{PROFILE["linkedin"]}" target="_blank" rel="noreferrer">LinkedIn ↗</a>
        </div>
    </section>
    <div class="footer"><span>© 2026 {PROFILE["name"]}</span><span>{PROFILE["location"]}</span><span>Made with intention ✦</span></div>
    """,
    unsafe_allow_html=True,
)
