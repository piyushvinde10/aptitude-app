# 🧠 AptitudeIQ — Online Aptitude Test Platform

![Python](https://img.shields.io/badge/Python-3.12-blue?style=flat-square&logo=python)
![Flask](https://img.shields.io/badge/Flask-3.x-black?style=flat-square&logo=flask)
![SQLite](https://img.shields.io/badge/SQLite-Database-lightblue?style=flat-square&logo=sqlite)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple?style=flat-square&logo=bootstrap)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

> A full-stack web application for conducting online aptitude tests. Admins manage questions and monitor student performance. Students register, take tests, and track their results — all in one place.

---

## 📸 Screenshots

| Login Page | Student Dashboard | Admin Dashboard |
|---|---|---|
| ![login](#) | ![student](#) | ![admin](#) |

> Replace `#` with actual screenshot links after deploying.

---

## ✨ Features

### 🎓 Student
- Register and login securely
- Take aptitude tests with multiple-choice questions
- View score instantly after submission
- Track full result history with grades and percentages

### 🛠️ Admin
- Auto-created on first run via `.env` config
- Add and delete aptitude questions
- View all registered students
- Monitor all student results and performance grades

---

## 🏗️ Project Structure

```
aptitude_app/
│
├── app/
│   ├── __init__.py          # App factory — initializes Flask & extensions
│   ├── models.py            # Database models: User, Question, Result
│   └── routes/
│       ├── __init__.py
│       ├── auth.py          # Register, Login, Logout
│       ├── student.py       # Dashboard, Take Test, Results
│       └── admin.py         # Admin Dashboard, Questions, Students
│
├── app/templates/
│   ├── base.html            # Base layout with navbar
│   ├── auth/
│   │   ├── login.html
│   │   └── register.html
│   ├── student/
│   │   ├── dashboard.html
│   │   ├── take_test.html
│   │   ├── result.html
│   │   └── my_results.html
│   └── admin/
│       ├── dashboard.html
│       ├── add_question.html
│       ├── manage_questions.html
│       ├── view_results.html
│       └── view_students.html
│
├── .env                     # 🔒 Secret credentials (never pushed to GitHub)
├── .env.example             # Template for teammates
├── .gitignore
├── config.py                # App configuration
├── requirements.txt         # All dependencies
└── run.py                   # Entry point — starts app & creates admin
```

---

## 🗄️ Database Models

### `User`
| Field | Type | Description |
|---|---|---|
| id | Integer | Primary key |
| username | String | Unique username |
| email | String | Unique email |
| password | String | Hashed password |
| role | String | `student` or `admin` |

### `Question`
| Field | Type | Description |
|---|---|---|
| id | Integer | Primary key |
| question_text | String | The question |
| option_a/b/c/d | String | Four choices |
| correct_option | String | `a`, `b`, `c`, or `d` |

### `Result`
| Field | Type | Description |
|---|---|---|
| id | Integer | Primary key |
| score | Integer | Marks obtained |
| total | Integer | Total marks |
| user_id | ForeignKey | Links to User |

---

## ⚙️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python 3.12, Flask |
| Database | SQLite + Flask-SQLAlchemy |
| Auth | Flask-Login, Flask-Bcrypt |
| Frontend | Jinja2, Bootstrap 5, Bootstrap Icons |
| Config | python-dotenv |

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/aptitude-app.git
cd aptitude-app
```

### 2. Create Virtual Environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac / Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
```bash
# Windows
copy .env.example .env

# Mac / Linux
cp .env.example .env
```

Now open `.env` and fill in your values:
```env
SECRET_KEY=your-secret-key-here
ADMIN_USERNAME=admin
ADMIN_EMAIL=admin@example.com
ADMIN_PASSWORD=yourpassword
```

### 5. Run the App
```bash
python run.py
```

✅ The app will:
- Create all database tables automatically
- Create the admin account from your `.env` file
- Start the server at `http://127.0.0.1:5000`

---

## 🔐 Default Credentials

| Role | Email | Password |
|---|---|---|
| Admin | From your `.env` file | From your `.env` file |
| Student | Register at `/register` | Set during registration |

---

## 📍 Routes Overview

| URL | Method | Description | Access |
|---|---|---|---|
| `/` | GET | Redirects based on role | All |
| `/register` | GET, POST | Student registration | Public |
| `/login` | GET, POST | Login page | Public |
| `/logout` | GET | Logout | Logged in |
| `/student/dashboard` | GET | Student home | Student |
| `/student/take_test` | GET, POST | Take the test | Student |
| `/student/result` | GET | View test result | Student |
| `/student/my_results` | GET | Full result history | Student |
| `/admin/dashboard` | GET | Admin home | Admin |
| `/admin/add_question` | GET, POST | Add a question | Admin |
| `/admin/manage_questions` | GET | View/delete questions | Admin |
| `/admin/view_results` | GET | All student results | Admin |
| `/admin/view_students` | GET | All students | Admin |

---

## 🔒 Security Features

- Passwords are hashed using **Bcrypt** (never stored as plain text)
- Session management via **Flask-Login**
- Admin routes protected with a custom `@admin_required` decorator
- Secret credentials stored in `.env` (excluded from GitHub via `.gitignore`)
- Students cannot access admin pages and vice versa

---

## 👥 Contributing & Team Setup

Each team member should:

1. Clone the repo
2. Create their own `.env` file from `.env.example`
3. Run `python run.py` — admin is auto-created from their `.env`
4. Never commit the `.env` file

```bash
# After making changes, push to GitHub:
git add .
git commit -m "your message here"
git push
```

---

## 📦 Requirements

```
flask
flask-sqlalchemy
flask-login
flask-bcrypt
python-dotenv
```

Install all at once:
```bash
pip install -r requirements.txt
```

Generate `requirements.txt` (after installing packages):
```bash
pip freeze > requirements.txt
```

---

## 📈 Future Improvements

- [ ] Add timer for tests
- [ ] Add categories/subjects for questions
- [ ] Add email verification on registration
- [ ] Export results as PDF
- [ ] Add leaderboard for students
- [ ] Deploy to cloud (Render / Railway / Vercel)

---

## 📄 License

This project is licensed under the **MIT License** — feel free to use, modify, and distribute.

---

## 🙌 Acknowledgements

Built with ❤️ using Flask, SQLAlchemy, and Bootstrap 5.

---

> Made by **[Your Name]** · [GitHub](https://github.com/YOUR_USERNAME)