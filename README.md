# Smart Aluminium Extraction System 🚀

An industrial Django-based web application and predictive platform for material processing, aluminum yield estimation, red mud byproduct tracking, and full administrative audit management.

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.x-green.svg)](https://www.djangoproject.com/)
[![Render](https://img.shields.io/badge/Hosted%20On-Render-black.svg)](https://render.com/)
[![GitHub Pages](https://img.shields.io/badge/Demo-GitHub%20Pages-brightgreen.svg)](https://evangelinblessy-03.github.io/Smart-Aluminium-Extraction-System/)

---

## 🌐 Live Demos & Links

- **Interactive Front Page (GitHub Pages)**: [https://evangelinblessy-03.github.io/Smart-Aluminium-Extraction-System/](https://evangelinblessy-03.github.io/Smart-Aluminium-Extraction-System/)
- **Full Cloud Application (Render)**: [https://smart-aluminium-extraction-system.onrender.com](https://smart-aluminium-extraction-system.onrender.com)
- **Full Architecture Documentation**: [`DOCUMENTATION.md`](DOCUMENTATION.md)

---

## ⚡ Key Features

- **Real-Time Material Processing**: Input raw mineral data (e.g. Bauxite, Kaolin) with weight and purity percentages to calculate accurate aluminum yield.
- **Red Mud Byproduct Calculation**: Automatically predict environmental byproduct (red mud) for sustainable waste tracking.
- **Dual Role-Based Authentication**:
  - **User Role**: Process materials, view instant calculations, and access personal yield history.
  - **Admin Role**: Administrative oversight dashboard, material database management, and process result auditing.
- **Modern Responsive Dark UI**: Custom-built glassmorphism design with responsive layouts and smooth micro-animations.
- **Interactive Simulator**: Client-side yield simulator available directly on GitHub Pages.

---

## 🛠️ Technology Stack

| Component | Technology |
| :--- | :--- |
| **Backend Framework** | Django 5.x (Python 3.11+) |
| **WSGI Server** | Gunicorn (Production), Django WSGI (Development) |
| **Static File Serving**| WhiteNoise |
| **Database** | SQLite3 / MySQL compatible |
| **Frontend** | HTML5, Modern CSS3 (Glassmorphism & CSS Variables) |
| **Hosting & CI/CD** | Render.com & GitHub Pages |

---

## 💻 Local Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/evangelinblessy-03/Smart-Aluminium-Extraction-System.git
cd Smart-Aluminium-Extraction-System
```

### 2. Create and activate a virtual environment
```powershell
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply migrations
```bash
python manage.py migrate
```

### 5. Run development server
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000/` in your browser.

---

## ☁️ Deployment on Render

This project is pre-configured for Render.com:
1. Fork or push this repository to GitHub.
2. In [Render Dashboard](https://dashboard.render.com/), create a **New Web Service**.
3. Connect `Smart-Aluminium-Extraction-System`.
4. Render will auto-detect `render.yaml` or you can specify:
   - **Build Command**: `./build.sh`
   - **Start Command**: `gunicorn aluminum_project.wsgi:application`
5. Click **Deploy**!

---

## 👤 Author
Developed by **Evangelin Blessy RS**  
GitHub: [@evangelinblessy-03](https://github.com/evangelinblessy-03)
