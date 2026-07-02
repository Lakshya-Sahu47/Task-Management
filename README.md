# Task Management System — Login Module (Phase 1: Frontend)

This is **Phase 1** of the Task Management System internship project: a fully
functional, standalone **frontend login page**. It uses simulated
(fake) authentication via JavaScript and `localStorage` so it can be
demonstrated and evaluated before the Flask + MySQL backend is built.

---

## 📁 Folder Structure

```
frontend/
│
├── login.html          # Main login page
│
├── css/
│   └── style.css        # Custom styles (theme, layout, animations)
│
├── js/
│   └── login.js          # Validation, fake auth, session handling
│
├── assets/
│   └── logo.png           # Placeholder company logo
│
└── README.md             # This file
```

---

## ✅ Features Implemented

- **Responsive, centered login card** built with Bootstrap 5 (works on
  desktop, laptop, tablet, and mobile).
- **White / Blue / Light Gray** theme using CSS variables
  (`--primary-color`, `--secondary-color`, `--background-color`).
- Bootstrap **floating labels** for Username and Password.
- **Show Password** checkbox to reveal/hide the password field.
- **Remember Me** checkbox (UI only — no backend logic yet).
- **Client-side validation**:
  - Username: required, minimum 4 characters.
  - Password: required, minimum 6 characters.
  - Inline error messages shown below each field using Bootstrap's
    `is-invalid` / `invalid-feedback` styling.
- **Fake authentication** using two hard-coded users (see credentials
  below), simulating a ~1.5 second network delay with a loading spinner.
- **Login button**: full-width, large, blue, with hover animation and a
  disabled + spinner state while "logging in."
- **Forgot Password** link that opens a Bootstrap modal showing
  "Feature coming soon."
- **Session persistence** via `localStorage` (`loggedIn`, `username`,
  `role`, `loginTime`).
- **Auto-redirect on existing session**: reopening `login.html` while
  already logged in redirects straight to the correct dashboard.
- **Keyboard support**: pressing Enter submits the form.
- **Accessibility**: semantic HTML, `<label>` elements for every input,
  ARIA attributes (`aria-describedby`, `aria-live`, `aria-hidden`),
  logical tab order, and auto-focus on the username field on load.
- **Animations**: card fade-in on load, button hover lift, input focus
  glow, smooth Bootstrap modal transitions, and a loading spinner.
- **Well-organized JavaScript**, split into small single-purpose
  functions (see `js/login.js`):
  `initializeLogin()`, `validateForm()`, `validateField()`,
  `togglePassword()`, `fakeAuthentication()`, `saveSession()`,
  `redirectUser()`, `showAlert()`, `hideAlert()`, `checkExistingLogin()`,
  `setLoadingState()`.

---

## ▶️ How to Run Locally

No build tools, servers, or dependencies are required.

1. Download / clone the `frontend/` folder.
2. Open `login.html` directly in any modern browser (Chrome, Edge,
   Firefox, Safari) — either by double-clicking it or using an
   extension like VS Code's "Live Server" for auto-reload during
   development.
3. Log in using one of the fake credentials below.

> **Note:** Since this phase has no backend, `dashboard.html` and
> `employee_dashboard.html` do not exist yet — the browser will show a
> "page not found" state after a successful login. This is expected
> until those pages (or the Flask backend) are built in a later phase.

---

## 🔑 Fake Login Credentials

| Role     | Username   | Password      |
|----------|------------|----------------|
| Admin    | `admin`    | `admin123`     |
| Employee | `employee` | `employee123`  |

Any other combination will trigger the
**"Invalid username or password."** alert.

---

## 🔌 Future Flask Integration Plan

This frontend was intentionally built so it can be wired up to a real
Flask backend later **without changing any HTML/CSS**. The plan is:

1. **Replace `fakeAuthentication()`** in `js/login.js` with a real
   `fetch()` call to a Flask endpoint, e.g.:

   ```js
   function authenticate(username, password) {
     return fetch("/api/login", {
       method: "POST",
       headers: { "Content-Type": "application/json" },
       body: JSON.stringify({ username, password }),
     })
       .then((response) => {
         if (!response.ok) {
           throw new Error("Invalid username or password.");
         }
         return response.json(); // expected: { username, role, token }
       });
   }
   ```

2. **Flask backend** will expose a `/api/login` route that:
   - Accepts `username` and `password` via POST (JSON body).
   - Verifies credentials against the **MySQL** `users` table
     (with hashed passwords, e.g. using `werkzeug.security`).
   - Returns a JSON response with the user's `role` and a session
     token / JWT on success, or a `401` error on failure.

3. **Session handling** will move from plain `localStorage` flags to a
   secure token (JWT or Flask session cookie), while keeping the same
   `saveSession()` / `checkExistingLogin()` structure so the rest of
   the frontend logic barely changes.

4. **Remember Me** will be connected to a longer-lived token/cookie
   expiry on the backend.

5. Once authenticated, the existing `redirectUser(role)` function will
   continue to route Admins to `dashboard.html` and Employees to
   `employee_dashboard.html` — these will be built out as real,
   data-driven pages in later phases.

---

## 🛠️ Tech Stack (Phase 1)

- HTML5 (semantic markup)
- CSS3 (custom properties, Flexbox, media queries)
- Bootstrap 5 (via CDN — cards, floating labels, modal, spinner, alerts)
- Vanilla JavaScript (ES6)

No frontend frameworks (React/Angular/Vue) and no backend code
(Flask/Python/MySQL) are included in this phase, per project
requirements.
