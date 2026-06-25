CMS — Corporate Management Portal

A full-stack Content Management System with a React.js frontend and Django REST Framework backend. Built as a team project, it allows users to create and manage dynamic websites, browse products, and handle cart operations through a clean, responsive interface.

---

# Repository Structure

```
CMS/
├── Websitebuilder/          # React.js frontend
└── Websitebuilderbackend/   # Django REST Framework backend
```

---

## Tech Stack

| Side | Technology |
|---|---|
| Frontend | React 18, Tailwind CSS, GSAP, React Router v6, Vite |
| Backend | Django, Django REST Framework, Python |
| Database | SQLite (Django ORM) |
| Auth | Django Session-based Authentication |
| Testing | Python test suite (8+ test files) |

---

## Features

- **Content Management** — Create, edit, and delete dynamic pages via WYSIWYG editor
- **Product Catalog** — Browse products with filtering, sorting, and detail views
- **Shopping Cart** — Add/remove items, update quantities, persistent cart state
- **Role-based Access** — Admin and user dashboards with permission-controlled routes
- **Authentication** — Secure login/logout with session management
- **REST API** — DRF-powered API consumed entirely by the React frontend
- **Responsive UI** — Mobile-first design with Tailwind CSS and GSAP animations

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Veer-ctrl/CMS.git
cd CMS
```

### 2. Start the Backend

```bash
cd Websitebuilderbackend

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Backend runs at: `http://127.0.0.1:8000`

### 3. Start the Frontend

```bash
cd Websitebuilder

npm install
npm run dev
```

Frontend runs at: `http://localhost:3000`

---

## Architecture

```
React Frontend  ──►  DRF REST API  ──►  Django ORM  ──►  SQLite DB
(Port 3000)          (Port 8000)
```

- Frontend makes API calls to the Django backend
- Backend handles all business logic, auth, and DB operations
- CORS configured to allow cross-origin requests between ports

---

## Team

| Name | Role |
|---|---|
| Veer | Backend, DRF APIs, DB schema, Testing |
| [Teammate] | Frontend, React components, UI/UX |

---

## License

This project is for educational purposes.
