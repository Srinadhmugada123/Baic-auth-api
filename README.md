# 🔐 Django REST Basic Authentication API

A simple Django REST Framework project with APIView-based register, login, and logout endpoints using **Basic Authentication**.

## ⚙️ Features

- Register new users
- Login with username & password
- Logout (just a success message)
- Uses Django REST Framework `APIView`
- Basic Auth used (no token/JWT)

## 🔗 Endpoints

| Method | Endpoint         | Description        |
|--------|------------------|--------------------|
| POST   | `/api/register/` | Register user      |
| POST   | `/api/login/`    | Login credentials  |
| POST   | `/api/logout/`   | Logout user        |

## 🧪 How to Test

Use Postman or browser:
- Login with Basic Auth header
- Test protected routes
- No token or session stored

## 🚀 Setup

pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver


## 👨‍💻 Author

[Srinadh Mugada](https://github.com/Srinadhmugada123)
