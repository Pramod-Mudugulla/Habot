# Habot - Employee Management System

Habot is a robust backend API built with Django REST Framework for managing employee records. It features JWT-based authentication, automated health checks, and interactive API documentation.

## 🚀 Features

- **Employee Management**: Full CRUD (Create, Read, Update, Delete) operations for employee records.
- **Filtering**: Search and filter employees by department and role.
- **Authentication**: Secure access using JWT (JSON Web Tokens).
- **API Documentation**: Interactive Swagger/OpenAPI documentation.
- **Health Check**: Endpoint to monitor the system status.

## 🛠️ Tech Stack

- **Framework**: Django 6.x
- **API Engine**: Django REST Framework (DRF)
- **Authentication**: SimpleJWT
- **Docs**: drf-spectacular (Swagger UI)
- **Database**: SQLite (Default)

## 📦 Installation & Setup

### 1. Clone the Repository
```bash
git clone <repository-url>
cd Habot
```

### 2. Create a Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Migrations
```bash
python manage.py migrate
```

### 5. Start the Development Server
```bash
python manage.py runserver
```
The server will be available at `http://127.0.0.1:8000/`.

## 🔐 Authentication

This project uses JWT for authentication.

1.  **Obtain Token**: Send a POST request to `/api/token/` with `username` and `password`.
2.  **Use Token**: Include the access token in the `Authorization` header for protected requests:
    `Authorization: Bearer <your_access_token>`

## 📖 API Documentation

You can explore and test the API endpoints using the built-in Swagger UI:

- **Swagger UI**: [http://127.0.0.1:8000/api/docs/](http://127.0.0.1:8000/api/docs/)
- **Schema**: [http://127.0.0.1:8000/api/schema/](http://127.0.0.1:8000/api/schema/)

## 🧪 Running Tests

To run the automated test suite:
```bash
python manage.py test
```

## 🏥 Health Check

Check the system status at:
`GET /api/health/`