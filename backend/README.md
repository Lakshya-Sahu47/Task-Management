# Task Management System — Backend Refactor Tracker

This README tracks the incremental refactor of the Flask backend into the
**Application Factory Pattern**. It is updated after every file is
generated so it always reflects exactly what exists and what each file
does.

---

## 📦 Package Rename

The top-level package is renamed from `app` → **`task_management`** to
avoid ambiguity with the Flask `app` object/variable.

---

## 🎯 Target Project Structure

```
backend/
│
├── task_management/
│   ├── __init__.py        # create_app() factory
│   ├── config.py          # Config classes (env-based)
│   ├── extensions.py      # db, cors instances
│   ├── models/            # SQLAlchemy ORM models
│   ├── routes/            # Blueprints / API endpoints
│   ├── services/          # Business logic layer
│   └── utils/             # Shared helper functions
│
├── instance/               # Instance-relative config, local files
├── tests/                   # Test suite
├── logs/                     # Application logs
├── run.py                     # Dev server entry point
├── requirements.txt            # Python dependencies
└── README.md                    # This file
```

---

## 📊 Generation Progress Tracker

| Order | File                          | Status         | Purpose                                                   |
|-------|-------------------------------|----------------|-------------------------------------------------------------|
| 1     | `requirements.txt`            | ⬜ Not started | Pin project dependencies                                    |
| 2     | `.env.example`                 | ⬜ Not started | Template for required environment variables                 |
| 3     | `run.py`                        | ⬜ Not started | Entry point that calls `create_app()` and runs dev server   |
| 4     | `task_management/__init__.py`    | ⬜ Not started | Application factory (`create_app()`), extension init, blueprint registration |
| 5     | `task_management/config.py`       | ⬜ Not started | Config classes reading from environment variables           |
| 6     | `task_management/extensions.py`    | ⬜ Not started | Shared extension instances (`db`, `cors`)                    |
| 7     | `task_management/models/`           | ⬜ Not started | SQLAlchemy ORM models (MySQL)                                |
| 8     | `task_management/services/`          | ⬜ Not started | Business logic layer                                         |
| 9     | `task_management/routes/`             | ⬜ Not started | Blueprints and API endpoints                                  |
| 10    | `task_management/utils/`               | ⬜ Not started | Shared helper functions                                        |

Legend: ✅ Complete · 🟡 In progress · ⬜ Not started

> Each row will be flipped to ✅ and given a one-line "what it does /
> what it depends on" note the moment that file is generated.

---

## 🧭 Rules Governing This Refactor

- Application Factory Pattern with `create_app()`.
- SQLAlchemy ORM, MySQL-compatible.
- Flask-CORS enabled.
- Configuration via environment variables (no hard-coded secrets).
- Python 3.12+, PEP8, type hints, minimal necessary code.
- **One file generated per step** — no file is generated until
  explicitly requested, and every prior file is assumed correct.

---

## ▶️ Next Recommended File

`requirements.txt`
