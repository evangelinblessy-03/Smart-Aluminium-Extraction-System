# Smart Aluminum Extraction System — Full Documentation

---

## Table of Contents

1. [Project Overview](#1-project-overview)
2. [Technology Stack](#2-technology-stack)
3. [Project Structure](#3-project-structure)
4. [Setup & Installation](#4-setup--installation)
5. [Database Schema](#5-database-schema)
6. [URL Routes](#6-url-routes)
7. [Views & Logic](#7-views--logic)
8. [User Roles](#8-user-roles)
9. [Pages & Features](#9-pages--features)
10. [Admin Panel](#10-admin-panel)
11. [User Manual](#11-user-manual)
12. [Common Errors & Fixes](#12-common-errors--fixes)

---

## 1. Project Overview

The **Smart Aluminum Extraction System** is a web-based application built with Django that allows users to:

- Input raw material data (name, weight, purity)
- Automatically calculate **aluminum yield** and **red mud** output
- Store and track all extraction results
- Search and view historical records
- Manage data through a dedicated admin dashboard

The system supports two separate roles — **User** and **Admin** — each with their own login page and dashboard.

---

## 2. Technology Stack

| Component     | Technology              |
|---------------|-------------------------|
| Backend       | Python 3.14, Django 6.0 |
| Database      | SQLite3 (file-based)    |
| Frontend      | HTML5, CSS3 (custom)    |
| Fonts         | Google Fonts — Inter    |
| Session Auth  | Django Sessions         |
| Admin Panel   | Django Built-in Admin   |

---

## 3. Project Structure

```
aluminum_project/
│
├── aluminum_project/          # Project config
│   ├── settings.py            # Django settings
│   ├── urls.py                # Root URL config
│   ├── wsgi.py
│   └── __init__.py
│
├── core/                      # Main application
│   ├── models.py              # Database models
│   ├── views.py               # View functions
│   ├── urls.py                # App URL routes
│   ├── admin.py               # Admin panel config
│   │
│   ├── templates/             # HTML templates
│   │   ├── home.html
│   │   ├── user_login.html
│   │   ├── admin_login.html
│   │   ├── register.html
│   │   ├── dashboard.html
│   │   ├── admin_dashboard.html
│   │   ├── add_material.html
│   │   ├── results.html
│   │   └── history.html
│   │
│   └── static/
│       └── style.css          # Global stylesheet
│
├── db.sqlite3                 # SQLite database file
├── manage.py                  # Django management CLI
└── DOCUMENTATION.md           # This file
```

---

## 4. Setup & Installation

### Prerequisites
- Python 3.10 or higher
- pip

### Step-by-step

**1. Clone or open the project folder**
```bash
cd aluminum_project
```

**2. Create and activate virtual environment**
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

**3. Install dependencies**
```bash
pip install django pymysql
```

**4. Apply database migrations**
```bash
python manage.py migrate
```

**5. Create an admin user**
```bash
python manage.py shell
```
```python
from core.models import User
User.objects.create(username='admin', password='admin123', role='admin')
exit()
```

**6. Create a Django superuser (for /admin/ panel)**
```bash
python manage.py createsuperuser
```

**7. Run the development server**
```bash
python manage.py runserver
```

**8. Open in browser**
```
http://127.0.0.1:8000/
```

---

## 5. Database Schema

### `core_user`
| Field        | Type         | Description                  |
|--------------|--------------|------------------------------|
| id           | Integer (PK) | Auto-generated primary key   |
| username     | CharField    | Unique username              |
| password     | CharField    | Plain text password          |
| role         | CharField    | `user` or `admin`            |
| is_approved  | BooleanField | Approval status (default: False) |

### `core_rawmaterial`
| Field   | Type         | Description              |
|---------|--------------|--------------------------|
| id      | Integer (PK) | Auto-generated           |
| name    | CharField    | Material name            |
| weight  | FloatField   | Weight in kilograms      |
| purity  | FloatField   | Purity percentage (0–100)|

### `core_material`
| Field           | Type         | Description                    |
|-----------------|--------------|--------------------------------|
| id              | Integer (PK) | Auto-generated                 |
| name            | CharField    | Material name                  |
| quantity        | IntegerField | Quantity (derived from weight) |
| predicted_yield | FloatField   | Predicted aluminum yield (kg)  |

### `core_processresult`
| Field                | Type         | Description                        |
|----------------------|--------------|------------------------------------|
| id                   | Integer (PK) | Auto-generated                     |
| material             | ForeignKey   | Links to `core_material`           |
| red_mud              | FloatField   | Red mud output (kg)                |
| digestion_temp       | FloatField   | Digestion temperature              |
| digestion_pressure   | FloatField   | Digestion pressure                 |
| naoh_concentration   | FloatField   | NaOH concentration                 |
| residence_time       | FloatField   | Residence time                     |
| precipitation_temp   | FloatField   | Precipitation temperature          |
| precipitation_pressure | FloatField | Precipitation pressure             |
| calcination_temp     | FloatField   | Calcination temperature            |
| aluminum_yield       | FloatField   | Final aluminum yield (kg)          |
| energy_consumption   | FloatField   | Energy used                        |
| co2_emissions        | FloatField   | CO2 emissions                      |
| created_at           | DateTimeField| Auto timestamp on creation         |

---

## 6. URL Routes

| URL                  | View Function    | Name              | Access      |
|----------------------|------------------|-------------------|-------------|
| `/`                  | home             | home              | Public      |
| `/register/`         | register         | register          | Public      |
| `/login/`            | user_login       | user_login        | Public      |
| `/admin-login/`      | admin_login      | admin_login       | Public      |
| `/dashboard/`        | dashboard        | dashboard         | User only   |
| `/admin-dashboard/`  | admin_dashboard  | admin_dashboard   | Admin only  |
| `/add-material/`     | add_material     | add_material      | User only   |
| `/results/`          | view_results     | results           | User only   |
| `/history/`          | result_history   | history           | User only   |
| `/logout/`           | logout_view      | logout            | Logged in   |
| `/admin/`            | Django Admin     | —                 | Superuser   |

---

## 7. Views & Logic

### `home`
Renders the landing page with navigation to login, admin login, and register.

### `register`
- Accepts POST with `username`, `password`, `role`
- Checks for duplicate usernames
- Creates a new `User` record
- Redirects to user login on success

### `user_login`
- Filters `User` by `username`, `password`, `role='user'`
- Stores `user_id`, `username`, `role` in session
- Redirects to `/dashboard/`

### `admin_login`
- Filters `User` by `username`, `password`, `role='admin'`
- Stores session data
- Redirects to `/admin-dashboard/`

### `dashboard`
- Requires session `user_id`
- Renders user dashboard with quick action tiles

### `admin_dashboard`
- Requires session with `role='admin'`
- Displays total results, materials, users count
- Shows 10 most recent extraction records

### `add_material`
- Accepts POST with `name`, `weight`, `purity`
- Calculates:
  - `aluminum_yield = weight × (purity / 100)`
  - `red_mud = weight − aluminum_yield`
- Creates `RawMaterial`, `Material`, and `ProcessResult` records
- Stores `result_id` in session
- Renders results page immediately

### `view_results`
- Reads `result_id` from session
- Fetches and displays the corresponding `ProcessResult`

### `result_history`
- Lists all `ProcessResult` records
- Supports search by material name via `?q=` query parameter

### `logout_view`
- Clears the session
- Redirects admin → `/admin-login/`, user → `/login/`

---

## 8. User Roles

| Role  | Login URL       | Dashboard URL       | Capabilities                              |
|-------|-----------------|---------------------|-------------------------------------------|
| User  | `/login/`       | `/dashboard/`       | Process materials, view results, history  |
| Admin | `/admin-login/` | `/admin-dashboard/` | View stats, recent records, manage data   |

Role is stored in the session after login and checked on every protected view.

---

## 9. Pages & Features

### Home Page (`/`)
- Navigation bar with User Login, Admin Login, Register buttons
- Hero section with system title and description
- Stats row showing accuracy, speed, and tracking metrics

### User Login (`/login/`)
- Blue-themed login card
- Session-based authentication against custom `User` model
- Link to register and admin login

### Admin Login (`/admin-login/`)
- Orange/red-themed login card
- Authenticates only users with `role='admin'`
- Link back to user login

### Register (`/register/`)
- Create a new user account
- Role selection (User / Admin)
- Duplicate username check

### User Dashboard (`/dashboard/`)
- Welcome message with username
- Three action tiles: Process Material, View History, Last Result

### Admin Dashboard (`/admin-dashboard/`)
- Stats cards: Total Processes, Total Materials, Total Users
- Table of 10 most recent extraction records
- Links to full history and Django admin panel

### Process Material (`/add-material/`)
- Form: Material Name, Weight (kg), Purity (%)
- Instant calculation on submit
- Saves to database and shows results

### Results (`/results/`)
- Shows Material Name, Aluminum Yield, Red Mud
- Buttons to process again or view history

### History (`/history/`)
- Full table of all extraction records
- Search by material name
- Shows date, yield, and red mud per record

---

## 10. Admin Panel

Django's built-in admin is available at `/admin/`.

### Registered Models
| Model         | Features                                              |
|---------------|-------------------------------------------------------|
| User          | List by id, username, role, is_approved. Filter by role. |
| Material      | List by id, name, quantity, predicted_yield           |
| RawMaterial   | List by id, name, weight, purity                      |
| ProcessResult | List by id, material, yield, temp, pressure, date. Ordered by newest. |

### Access
Requires a Django superuser created with:
```bash
python manage.py createsuperuser
```

---

## 11. User Manual

### How to Register
1. Go to `http://127.0.0.1:8000/`
2. Click **Register**
3. Enter a username, password, and select role
4. Click **Create Account**

### How to Log In (User)
1. Click **User Login** on the home page
2. Enter your username and password
3. Click **Sign In**

### How to Log In (Admin)
1. Click **Admin Login** on the home page
2. Enter admin username and password
3. Click **Admin Sign In**

### How to Process a Material
1. Log in as a user
2. Click **Process Material** on the dashboard
3. Enter Material Name, Weight (kg), and Purity (%)
4. Click **Calculate Results**
5. View the aluminum yield and red mud output

### How to View History
1. From the dashboard click **View History**
2. Browse all past records in the table
3. Use the search box to filter by material name

### How to Logout
- Click **Logout** in the top navigation bar
- You will be redirected to the appropriate login page

---

## 12. Common Errors & Fixes

| Error | Cause | Fix |
|-------|-------|-----|
| `ModuleNotFoundError: django_extensions` | Package not installed | Remove from `INSTALLED_APPS` or run `pip install django-extensions` |
| `mysqlclient 2.2.1 or newer is required` | Old mysqlclient with MySQL backend | Switch to SQLite in `settings.py` |
| `MultipleObjectsReturned` | Duplicate users in database | Use `.filter().first()` instead of `.get()` |
| `IntegrityError: invalid foreign key` | Orphaned data in SQLite | Delete `db.sqlite3` and run `migrate` again |
| `ValueError: ProcessResult.material must be a Material instance` | Passing `RawMaterial` to FK field | Create a `Material` object and pass that instead |
| `No migrations to apply` | Fresh database, all good | This is not an error — run `runserver` |
| Autofill credentials in login form | Browser autofill | Use hidden dummy inputs + JS timeout clear |
