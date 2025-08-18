# 📝 Django To-Do List v1.5.0
[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-Latest-green.svg)](https://www.djangoproject.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Made with ❤️](https://img.shields.io/badge/Made%20with-%E2%9D%A4-red)](#)

A simple yet **clean and polished** To-Do List web application built with **Django** and **SQLite**.  
Now with **user authentication** — each user can register, log in, and manage their own tasks independently.

---
## 🚀 Live Demo

Check out the live version of this app v1.0 hosted on PythonAnywhere:  
👉 [Django To-Do App](https://hakku.pythonanywhere.com)

---
## ✨ Features

- 👤 **User Authentication** (Register & Login)
- 🔒 Each user sees **only their own tasks**
- ➕ Add new tasks easily  
- ✅ Mark tasks as complete  
- 🗑️ Delete tasks  
- 📂 Uses SQLite (default Django DB)  
- 🎨 Clean and responsive UI  
- 📱 Mobile-friendly for smartphones & tablets  
- 🔑 Secure configuration with `.env` file  

---

## 📸 Screenshots

<h3>Login Screen</h3>
<img src="screenshots/django app 00.png" alt="Main Page" width="600">
<h3>Registration page</h3>
<img src="screenshots/django app 01.png" alt="Main Page" width="600">
<h3>homescreen</h3>
<img src="screenshots/django app 02.png" alt="Main Page" width="600">
<h3>Add task page</h3>
<img src="screenshots/django app 2.png" alt="Main Page" width="600">
<h3>Completed Tasks page</h3>
<img src="screenshots/django app 5.png" alt="Main Page" width="600">
<h3>SmartPhone view</h3>
<img src="screenshots/django app 6.png" alt="Main Page" width="250">


---

## 🚀 Installation Guide

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/django-todo-list.git
cd django-todo-list
```


### 2️⃣ Create & Activate a Virtual Environment

Windows
```bash
python -m venv venv
venv\Scripts\activate
```

Mac/Linux
```bash
python3 -m venv venv
source venv/bin/activate

```

### 3️⃣ Install Dependencies

(Using Pipenv with Pipfile.lock)
```bash
pip install pipenv
pipenv install --ignore-pipfile
```

Or if using pip:
```bash
pip install django
pip install python-decouple
```

### 4️⃣ Create a .env File

Inside the project root:
'enter any key combinations in secret key'
```bash
SECRET_KEY="your-secret-key"
DEBUG=True
```

### 5️⃣ Run Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6️⃣ Start the Development Server
```bash
python manage.py runserver
```

Visit: http://127.0.0.1:8000/ 🎉


### 🛠 Tech Stack

Python (3.12.5)

Django (latest stable)

SQLite (default Django DB)

HTML, CSS (Custom styling)

### 🤝 Contributing

Fork the project

Create your feature branch (git checkout -b feature/AmazingFeature)

Commit your changes (git commit -m 'Add some AmazingFeature')

Push to the branch (git push origin feature/AmazingFeature)

Open a Pull Request

### 📜 License

This project is licensed under the MIT License — see the LICENSE file for details.
