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
| 2     | Backend  | Database models (MySQL via SQLAlchemy)        | ✅ Complete     |
| 3     | Backend  | Auth API (`/api/auth/login`) + real routes    | ✅ Complete     |
| 4     | Backend  | Task CRUD APIs                                | ✅ Complete     |
| 5     | Frontend | Wire `login.js` to real Flask API             | ✅ Complete     |
| 6     | Frontend | Dashboard pages (Admin / Employee)            | ✅ Complete     |

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

### ▶️ How to Run the Project (Frontend & Backend Unified)

The project is structured so that the Flask backend serves the frontend static assets. Follow these steps to run the application:

1. **Verify Database Configuration**:
   Make sure you have MySQL running and a database named `task_management_db` is created and seeded. 
   Check/update your MySQL credentials in `backend/.env`:
   ```
   SQLALCHEMY_DATABASE_URI=mysql+pymysql://<user>:<password>@localhost:3306/task_management_db
   ```

2. **Activate the Virtual Environment**:
   Open a terminal and navigate to the `backend/` directory:
   ```bash
   cd backend
   venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Server**:
   ```bash
   python run.py
   ```
   This will start the development server on `http://127.0.0.1:5000`.

5. **Open in Browser**:
   Open `http://127.0.0.1:5000/` in your web browser. It will automatically serve the login page.

### 🔑 Active Login Credentials (from database seed data)

| Role     | Username        | Password      |
|----------|-----------------|----------------|
| Admin    | `admin`         | `admin123`     |
| Employee | `aarav.sharma`  | `Employee123`  |
| Employee | `rohan.patel`   | `Employee123`  |

> **Note:** Redirection currently targets `dashboard.html` and `employee_dashboard.html`, which do not exist yet. You will see a `404 Not Found` page after a successful login. This is expected until these dashboards are created.

### 🔌 Flask Integration Details
The frontend is fully wired to the backend API:
- The login form submits a `POST /api/auth/login` request.
- The backend checks database credentials and establishes a signed session cookie.
- Reopening the site triggers `GET /api/auth/me` to automatically verify the active session and redirect the user if a valid session exists.

---

## 2️⃣ Backend — Project Architecture

The backend implements the **Application Factory Pattern** with clean separation of layers:
- **`run.py`**: Entry point which initializes the Flask app factory.
- **`task_management/__init__.py`**: Initializer configuring static serving of the frontend assets, CORS credentials, database binding, and blueprints.
- **`task_management/models/`**: SQLAlchemy database models (`User`, `Employee`, `Task`, `TaskAssignment`, `ActivityLog`).
- **`task_management/services/`**: Business logic implementations (`auth_service`, `employee_service`, `task_service`, `assignment_service`).
- **`task_management/routes/`**: Flask Blueprint routes (`auth_bp`, `employee_bp`, `task_bp`, `assignment_bp`).

---

## 🗺️ Overall Roadmap
1. ~~Frontend login page (fake auth)~~ ✅
2. ~~Backend Flask project structure~~ ✅
3. ~~Database models (MySQL via SQLAlchemy)~~ ✅
4. ~~Real `/api/login` route + authentication logic~~ ✅
5. ~~Task CRUD APIs~~ ✅
6. ~~Connect frontend `login.js` to the real API~~ ✅
7. ~~Build out `dashboard.html` and `employee_dashboard.html`~~ ✅
