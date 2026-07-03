# Task Management System — Project README

This is the **single source of truth** for the Task Management System
internship project. It tracks overall progress across both the frontend
and backend, and explains how to run each part that currently exists.

The project is being built **incrementally, one step at a time**. This
file is updated after each completed step so it always reflects the
current state of the repo.

---

## 📊 Project Progress Tracker

| Phase | Area     | Description                                  | Status         |
|-------|----------|-----------------------------------------------|----------------|
| 1     | Frontend | Standalone login page (fake auth)             | ✅ Complete     |
| 1     | Backend  | Flask project structure (no logic yet)        | ✅ Complete     |
| 2     | Backend  | Database models (MySQL via SQLAlchemy)        | ⬜ Not started |
| 3     | Backend  | Auth API (`/api/login`) + real routes         | ⬜ Not started |
| 4     | Backend  | Task CRUD APIs                                | ⬜ Not started |
| 5     | Frontend | Wire `login.js` to real Flask API             | ⬜ Not started |
| 6     | Frontend | Dashboard pages (Admin / Employee)            | ⬜ Not started |

Legend: ✅ Complete · 🟡 In progress · ⬜ Not started

---

## 📁 Full Project Structure (current state)

```
project-root/
│
├── frontend/
│   ├── login.html            # Main login page
│   ├── css/
│   │   └── style.css          # Custom styles (theme, layout, animations)
│   ├── js/
│   │   └── login.js            # Validation, fake auth, session handling
│   └── assets/
│       └── logo.png             # Placeholder company logo
│
├── backend/
│   ├── app.py                 # Flask app factory + dev server entry point
│   ├── config.py               # Config class (env-based settings)
│   ├── extensions.py            # Shared extension instances (db, cors)
│   ├── requirements.txt          # Python dependencies for this phase
│   ├── models/
│   │   └── __init__.py            # Empty — DB models added in a later phase
│   ├── routes/
│   │   └── __init__.py            # Placeholder Blueprint, no endpoints yet
│   ├── services/
│   │   └── __init__.py            # Empty — business logic added later
│   ├── utils/
│   │   └── __init__.py            # Empty — shared helpers added later
│   └── instance/
│       └── .gitkeep               # Keeps the empty folder tracked in Git
│
└── README.md                  # This file
```

---

## 1️⃣ Frontend — Phase 1 (Complete)

A fully functional, standalone **frontend login page** using simulated
(fake) authentication via JavaScript and `localStorage`, built so it can
be demonstrated and evaluated before the Flask + MySQL backend exists.

### ✅ Features Implemented
- **Responsive, centered login card** built with Bootstrap 5 (desktop,
  laptop, tablet, mobile).
- **White / Blue / Light Gray** theme via CSS variables
  (`--primary-color`, `--secondary-color`, `--background-color`).
- Bootstrap **floating labels** for Username and Password.
- **Show Password** checkbox to reveal/hide the password field.
- **Remember Me** checkbox (UI only — no backend logic yet).
- **Client-side validation**:
  - Username: required, minimum 4 characters.
  - Password: required, minimum 6 characters.
  - Inline errors via Bootstrap's `is-invalid` / `invalid-feedback`.
- **Fake authentication** using two hard-coded users (see credentials
  below), simulating a ~1.5 second network delay with a loading spinner.
- **Login button**: full-width, large, blue, hover animation, disabled +
  spinner state while "logging in."
- **Forgot Password** link opening a Bootstrap modal ("Feature coming
  soon").
- **Session persistence** via `localStorage` (`loggedIn`, `username`,
  `role`, `loginTime`).
- **Auto-redirect on existing session** when reopening `login.html`.
- **Keyboard support**: Enter submits the form.
- **Accessibility**: semantic HTML, `<label>` for every input, ARIA
  attributes (`aria-describedby`, `aria-live`, `aria-hidden`), logical
  tab order, auto-focus on username field.
- **Animations**: card fade-in, button hover lift, input focus glow,
  smooth modal transitions, loading spinner.
- **Well-organized JavaScript** (`js/login.js`): `initializeLogin()`,
  `validateForm()`, `validateField()`, `togglePassword()`,
  `fakeAuthentication()`, `saveSession()`, `redirectUser()`,
  `showAlert()`, `hideAlert()`, `checkExistingLogin()`,
  `setLoadingState()`.

### ▶️ How to Run the Frontend
No build tools, servers, or dependencies required.
1. Download / clone the `frontend/` folder.
2. Open `login.html` directly in any modern browser (Chrome, Edge,
   Firefox, Safari) — double-click it, or use an extension like VS
   Code's "Live Server" for auto-reload during development.
3. Log in using one of the fake credentials below.

> **Note:** Since the backend isn't wired up yet, `dashboard.html` and
> `employee_dashboard.html` don't exist — a successful login currently
> leads to a "page not found" state. Expected until those pages (and the
> real API) are built in a later phase.

### 🔑 Fake Login Credentials
| Role     | Username   | Password      |
|----------|------------|----------------|
| Admin    | `admin`    | `admin123`     |
| Employee | `employee` | `employee123`  |

Any other combination triggers **"Invalid username or password."**

### 🔌 Future Flask Integration Plan
The frontend was built so it can be wired to a real Flask backend
**without changing any HTML/CSS**:
1. Replace `fakeAuthentication()` in `js/login.js` with a real `fetch()`
   call to `/api/login`.
2. Flask backend exposes `/api/login` (POST), verifying credentials
   against the MySQL `users` table (hashed passwords via
   `werkzeug.security`), returning `{ username, role, token }` on
   success or `401` on failure.
3. Session handling moves from `localStorage` flags to a secure token
   (JWT or Flask session cookie), keeping the same `saveSession()` /
   `checkExistingLogin()` structure.
4. **Remember Me** connects to a longer-lived token/cookie expiry.
5. `redirectUser(role)` continues routing Admins to `dashboard.html` and
   Employees to `employee_dashboard.html`, built out in later phases.

### 🛠️ Frontend Tech Stack
- HTML5 (semantic markup)
- CSS3 (custom properties, Flexbox, media queries)
- Bootstrap 5 (via CDN)
- Vanilla JavaScript (ES6)

No frontend frameworks and no backend code included in this phase.

---

## 2️⃣ Backend — Phase 1 (Complete)

The base Flask project skeleton only. No models, routes, business
logic, or database connections yet — this step sets up a clean,
scalable structure for later phases to build on.

### ✅ What's Implemented
- **Application factory pattern** (`create_app()` in `app.py`) instead
  of a global `Flask` object, keeping the app testable and scalable.
- **Configuration loading** from environment variables via
  `python-dotenv`, with placeholders for:
  - `SECRET_KEY`
  - `SQLALCHEMY_DATABASE_URI` (MySQL connection string format)
  - `SQLALCHEMY_TRACK_MODIFICATIONS`
- **Extensions initialized separately** (`extensions.py`) from the app
  instance to avoid circular imports later:
  - `db` (Flask-SQLAlchemy)
  - `cors` (Flask-CORS)
- **Placeholder Blueprint** registered in `app.py`, confirming
  `routes/` is wired up correctly — no endpoints defined yet.
- **Package skeletons** for `models/`, `services/`, `utils/` — each just
  an `__init__.py`, ready for future code.
- **`instance/` folder** reserved for Flask's instance-relative config
  and local/machine-specific files not meant for version control.

### ▶️ How to Run the Backend
1. Create and activate a virtual environment:
   ```bash
   cd backend
   python -m venv venv
   venv\Scripts\activate   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. (Optional) Create a `.env` file in `backend/` to override defaults:
   ```
   SECRET_KEY=your-secret-key
   DATABASE_URL=mysql+pymysql://user:password@localhost/task_management_db
   ```
4. Run the development server:
   ```bash
   python app.py
   ```
   No routes exist yet, so every URL currently returns Flask's default
   404 page — this is expected for this phase.

### 🔌 Deliberately Not Included Yet
- Database models
- API routes / endpoints
- Business logic / services
- Database tables or migrations
- Authentication
- CRUD operations

These are added incrementally in later phases without needing to change
`app.py`, `config.py`, or `extensions.py`.

### 🛠️ Backend Tech Stack (Phase 1)
- Python 3.12+
- Flask (latest stable)
- Flask-SQLAlchemy
- Flask-CORS
- python-dotenv
- PyMySQL

---

## 🗺️ Overall Roadmap
1. ~~Frontend login page (fake auth)~~ ✅
2. ~~Backend Flask project structure~~ ✅
3. Database models (MySQL via SQLAlchemy)
4. Real `/api/login` route + authentication logic
5. Task CRUD APIs
6. Connect frontend `login.js` to the real API
7. Build out `dashboard.html` and `employee_dashboard.html`
