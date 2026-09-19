# Govathoti Vamsi — Portfolio

Personal portfolio website for Govathoti Vamsi, built with Streamlit. It presents software projects, AI/ML experience, education, technical skills, and contact links in a responsive, visual layout.

## Highlights

- Responsive portfolio landing page with hero, about, experience, projects, skills, and contact sections
- Clickable project cards with detailed project dialogs
- Clickable AI/ML internship experience with a dedicated Smart Sorting case study
- Project-specific visual cards and technology tags
- Profile photo and project artwork stored locally in `assets/`
- Resume preview and download actions using the PDF in `assets/`
- GitHub, LinkedIn, email, and phone contact links
- Streamlit configuration for local-network access on port `8501`

## Featured work

- **vamsiMart** — Multipage e-commerce platform with search, categories, carts, checkout, and order history
- **StudyMind AI** — PDF-based agentic RAG study assistant using embeddings and FAISS
- **Job Application Tracker** — Frontend job-search workspace with CRUD, filtering, localStorage, and CSV export
- **Driver Safety AI** — Real-time drowsiness and distraction detection concept
- **Smart Sorting** — MobileNetV2 and Flask application for fresh/rotten fruit and vegetable classification

## Run locally

### Requirements

- Python 3.10 or newer
- `pip`

### Setup

```powershell
git clone https://github.com/vamsigovathoti8125/portfolio.git
cd portfolio
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Start the app

```powershell
streamlit run app.py
```

The app opens at:

```text
http://localhost:8501
```

The included `.streamlit/config.toml` also binds Streamlit to `0.0.0.0`, so the app can be accessed from another device on the same local network at:

```text
http://<your-local-ip>:8501
```

For example:

```text
http://10.20.58.82:8501
```

Windows Firewall and Wi-Fi network isolation may need to allow inbound TCP traffic on port `8501`.

## Project structure

```text
portfolio/
├── app.py
├── assets/
│   ├── profile.png
│   ├── Vamsi_Govathoti_Resume.pdf
│   ├── image.png
│   ├── pro exp 1.png
│   ├── pro exp 3.png
│   ├── pro exp 4.png
│   └── project explaining 2.png
├── .streamlit/
│   └── config.toml
├── requirements.txt
└── README.md
```

## Customization

Most portfolio content is defined near the top of [`app.py`](app.py):

- `PROFILE` — name, role, contact links, introduction, and location
- `EXPERIENCE` — internship details and Smart Sorting case-study content
- `EDUCATION` — college, degree, dates, and result
- `PROJECTS` — project descriptions, links, tags, artwork, and detailed content
- `SKILL_GROUPS` and `SKILL_ICONS` — technical skills shown on the page

Replace the files in `assets/` with your own images while keeping the filenames, or update the corresponding paths in `app.py`.

## Deployment

The app can be deployed with Streamlit Community Cloud:

1. Push the repository to GitHub.
2. Open [share.streamlit.io](https://share.streamlit.io/).
3. Select `vamsigovathoti8125/portfolio`.
4. Choose `app.py` as the main file.
5. Deploy.

## License

This repository is a personal portfolio project. Contact the owner before reusing personal content, images, or profile information.
