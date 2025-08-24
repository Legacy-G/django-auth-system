# Django Authentication System 🛡️

A clean and customizable user authentication system built with Django. This project includes login, signup, logout, and modal-based UI interactions using Bootstrap 5.

## 🚀 Features

- User registration with validation
- Login and logout functionality
- Modal-based forms for seamless UX
- AJAX checks for username and email availability
- Bootstrap 5 styling for responsive design
- Django messages framework for feedback alerts

## 📦 Tech Stack

- **Backend**: Django 5.x
- **Frontend**: HTML, Bootstrap 5
- **Database**: SQLite (default, easily swappable)
- **Languages**: Python, HTML

## 📁 Project Structure
```
authsystem/
├── authentication/ # App for auth views and templates
│ ├── templates/
│ │ └── authentication/
│ │ ├── login.html
│ │ ├── signin.html
│ ├── views.py
│ ├── urls.py
├── templates/
│ ├── index.html
│ ├── landingpage.html
├── manage.py
├── db.sqlite3
```


## ⚙️ Setup Instructions

1. Clone the repo:
   ```bash
   git clone https://github.com/Legacy-G/django-auth-system.git
   cd django-auth-system

2. Create and activate a virtual environment
   ```bash
    python -m venv env
    source env/bin/activate  # On Windows: env\Scripts\activate

3. Install dependencies:
   ```bash
   pip install -r requirements.txt

4. Run migrations:
   ```bash
   python manage.py migrate

5. Start the server:
   ```bash
   python manage.py runserver

9. Visit http://127.0.0.1:8000/ to view the landing page.


🧪 Testing
Try registering a new user via the Signin modal

Login using the Login modal

Check for validation messages and modal transitions

📌 To-Do
Add password reset functionality

Integrate email verification

Improve accessibility and ARIA compliance

📄 License
This project is open-source under the MIT License.


