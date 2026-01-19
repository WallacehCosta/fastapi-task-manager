# TaskFlow API

A RESTful API built with **FastAPI** that implements user authentication and task management using **JWT**, **SQLAlchemy**, and **PostgreSQL**.  
This project was developed as a backend portfolio piece, focusing on clean architecture, security, and best practices.

![API-DOCS](public/swagger.png)

---

## Features

- User registration and authentication (JWT)
- Secure password hashing with bcrypt
- OAuth2 Password Flow
- Protected routes with Bearer Token
- Task creation and management
- PostgreSQL database with SQLAlchemy ORM
- Interactive API documentation with Swagger (/docs)

---

## Tech Stack

- **Python**
- **FastAPI**
- **SQLAlchemy**
- **PostgreSQL**
- **JWT (python-jose)**
- **Passlib (bcrypt)**
- **Uvicorn**

---

## Environment Variables

Create a `.env` file based on `.env.example`:

```console
DATABASE_URL=postgresql://user:password@localhost:5432/taskflow
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

> **Do not commit your `.env` file.**

---

## Running the Project

1. Create and activate a virtual environment
2. Install dependencies:

```console
pip install -r requirements.txt
```

3. Run the server:

```console
uvicorn main:app --reload
```

4. Open:


```console
http://127.0.0.1:8000/docs
```


---

## Authentication Flow

1. Register a user (`/auth/register`)
2. Login to obtain an access token (`/auth/login`)
3. Use the token as:
```console
Authorization: Bearer <access_token>
```
4. Access protected endpoints (e.g. task creation)

---

## Purpose

This project was created to demonstrate:
- Backend fundamentals
- Secure authentication flows
- API design with FastAPI
- Clean and maintainable code structure

---

## License

MIT License

