# CMS Backend

REST API backend for the Corporate Management Portal, built with Django REST Framework. Handles authentication, product management, cart operations, and content management — consumed by the React frontend.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Framework | Django, Django REST Framework |
| Language | Python |
| Database | SQLite (Django ORM) |
| Auth | Django Session-based Authentication |
| Testing | Python unittest (pytest-style test files) |

---

## API Modules

### Authentication
- `POST /api/auth/login/` — Login and start session
- `POST /api/auth/logout/` — End session
- `POST /api/auth/register/` — Register new user

### Content Management
- `GET /api/content/` — Fetch all content blocks
- `POST /api/content/` — Create new content
- `PUT /api/content/<id>/` — Update existing content
- `DELETE /api/content/<id>/` — Delete content

### Products
- `GET /api/products/` — List all products
- `GET /api/products/<id>/` — Get product detail
- `POST /api/products/` — Add product (Admin only)
- `PUT /api/products/<id>/` — Update product (Admin only)

### Cart
- `GET /api/cart/` — Get current user's cart
- `POST /api/cart/add/` — Add item to cart
- `PUT /api/cart/update/` — Update item quantity
- `DELETE /api/cart/remove/<id>/` — Remove item from cart

---

## Project Structure

```
Websitebuilderbackend/
├── builderbackend/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── src/
│   ├── auth/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── serializers.py
│   │   └── urls.py
│   ├── products/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── serializers.py
│   │   └── urls.py
│   ├── cart/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── serializers.py
│   │   └── urls.py
│   └── content/
│       ├── models.py
│       ├── views.py
│       ├── serializers.py
│       └── urls.py
├── test_api.py
├── test_blog_api.py
├── test_cart_functionality.py
├── test_cart_page_direct.py
├── test_complete_blog_flow.py
├── test_complete_flow.py
├── manage.py
└── requirements.txt
```

---

## Getting Started

### Prerequisites

- Python 3.x
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/Veer-ctrl/CMS.git
cd CMS/Websitebuilderbackend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser (for admin access)
python manage.py createsuperuser

# Start the server
python manage.py runserver
```

API runs at `http://127.0.0.1:8000/api/`

---

## Running Tests

```bash
# Run all tests
python manage.py test

# Run specific test file
python test_api.py
python test_cart_functionality.py
python test_complete_flow.py
```

---

## Environment Variables

Create a `.env` file in the backend root:

```env
DEBUG=True
SECRET_KEY=your_secret_key_here
ALLOWED_HOSTS=localhost,127.0.0.1
CORS_ALLOWED_ORIGINS=http://localhost:3000
```

---

## CORS Configuration

Since the React frontend runs on a different port, CORS is configured in `settings.py`:

```python
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]
```

---

## Team

| Name | Role |
|---|---|
| Veer | Backend, DRF APIs, DB Schema |
| [Teammate] | Frontend, React, UI |

---

## License

This project is for educational purposes.
