# ProClientProject

A Django REST Framework API for managing clients and projects with JWT authentication and MySQL database.

---
## Table of Contents

- [Project Overview]  
- [Features]  
- [Tech Stack]  
- [Setup and Installation]  
- [Configuration] 
- [Running the Project]  
- [API Endpoints] 
- [Authentication]      

---

## Project Overview

This project provides a RESTful API to manage clients and their projects. Users can register, authenticate using JWT tokens, create clients, assign projects, and manage project users.

---

## Features

- User registration and JWT-based authentication  
- CRUD operations for Clients and Projects  
- Assign multiple users to projects  
- Nested serializers for detailed client and project views  
- MySQL database integration  

---

## Tech Stack

Backend: Python, Django, Django REST Framework

Authentication: djangorestframework-simplejwt (JWT)

Database: MySQL (via mysqlclient)  

---

## Setup and Installation

1. **Clone the repository**

```bash
git clone https://github.com/Prachi1416/ProClientProject.git
cd ProClientProject
```

2. **Create and activate a virtual environment**

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

3. **Install dependencies**

```bash
- pip install djangorestframework
- pip install mysqlclient
- pip install djangorestframework-simplejwt
```

4. **Configure MySQL database**

- Create a MySQL database named `ProClient_DB`.
- Update `ProClientProject/settings.py` with your database credentials:

```python
DATABASES = {
    'default': {
        'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ProClient_DB',
        'USER': 'root',
        'PASSWORD': 'root',
    }
}
```

---

## Running the Project

1. **Apply migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

2. **Run the development server**

```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`

---

## API Endpoints

| Endpoint                  | Method        | Description                        |
|---------------------------|---------------|------------------------------------|
| `/signup/`                | POST          | Register a new user                |
| `/token/`                 | POST          | Obtain JWT access and refresh token|
| `/clients/`               | GET           | List all clients                   |
| `/clients/`               | POST          | Create a new client                |
| `/clients/<pk>/`          | GET           | Retrieve client details            |
| `/clients/<pk>/`          | PUT/ PATCH    | Update client                      |
| `/clients/<id>/`          | DELETE        | Delete client                      |
| `/clients/<id>/projects/` | POST          | Create a project under a client    |
| `/projects/`              | GET           | List projects assigned to the user |

---
## Authentication

- Use the `/token/` endpoint to obtain JWT tokens by sending username and password.
- Include the access token in the `Authorization` header for protected endpoints:

```
Authorization: Bearer <access_token>
```

---

