# The Link Edit | URL Shortener

A high-end, aesthetic URL shortening service designed with a **"Premium E-commerce"** aesthetic. Built using **FastAPI** and **SQLAlchemy**, featuring a **Glassmorphism** dashboard inspired by luxury platforms like Myntra and Nykaa.

## Features
* **Sophisticated UI:** Soft blush and berry pink color palette with custom floating bubble animations.
* **Glassmorphism Design:** Translucent, blurred containers using advanced CSS `backdrop-filter` properties.
* **FastAPI Backend:** High-performance asynchronous API handling for efficient link generation.
* **Database Persistence:** Integrated with SQLAlchemy and SQLite to manage and store redirected URLs.
* **Responsive Layout:** Fully optimized for mobile and desktop viewports.

## Tech Stack
* **Backend:** Python, FastAPI
* **Database:** SQLAlchemy, SQLite
* **Frontend:** HTML5, CSS3 (Custom Glassmorphism), Vanilla JavaScript
* **Deployment:** Railway / Render

## Project Structure
```text
url-shortener/
├── app/
│   ├── main.py        # API routes and core logic
│   └── models.py      # SQLAlchemy database models
├── static/            # Glam CSS, animations, and JS
├── templates/         # Jinja2 HTML templates
├── Procfile           # Deployment configuration
└── requirements.txt   # Project dependencies


```
---

### The Setup Instructions
## How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/prakratis/URL-Shortener-FastAPI-Glam.git
cd URL-Shortener-FastAPI-Glam
```

### 2. Set up a Virtual Environment
```bash
python -m venv venv
# On Windows:
.\venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Launch the Dashboard
```bash
fastapi dev app/main.py
```
The application will be live at http://127.0.0.1:8000

## Technical Challenges & Fixes

### 1. The "Localhost" Redirection Bug
* **Issue:** Initially, the API generated short links using `127.0.0.1:8000`, which worked locally but failed in production.
* **Fix:** Implemented dynamic base URL detection using the FastAPI `Request` object to ensure the app is "environment-aware."

### 2. Deployment Host Binding
* **Issue:** The application was unreachable on Railway due to default host binding.
* **Fix:** Configured the `Procfile` to bind to `0.0.0.0` and dynamically use the `${PORT}` assigned by the platform.

### 3. Variable Shadowing
* **Issue:** Experienced an `AttributeError` during the transition to dynamic URLs.
* **Fix:** Resolved a naming conflict where the `Request` object was being shadowed by a local variable, ensuring clean scope management.


## Deployment & Validity
**Live Demo:** [https://url-shortener-1904.up.railway.app/]
* **Link Validity:** Since this project uses an ephemeral SQLite database on Railway's trial tier, links are valid as long as the current deployment is active. 
* **Note:** Database records may reset during redeployments. For a permanent solution, a persistent PostgreSQL instance is recommended.



