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

