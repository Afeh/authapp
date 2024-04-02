# AuthApp

AuthApp is a simple and secure authentication system built with modern web technologies.


## Features

- User registration and authentication
- Password hashing and verification
- Password reset
- Session management
- Email OTP verification
- JSON Web Token (JWT) authentication
- RESTful API design
- OAuth 2.0 with Google


# Installation/Project Setup
To install and run AuthApp, follow these steps:

## Clone the repository:
git clone https://github.com/Afeh/authapp.git

## Install dependencies

1. Install Python 3.12.2
```bash
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.12.2
```

2. Install Python 3.12-venv
```bash
sudo apt install python3.12-venv
```

3. Create Virtual Environment
```bash
cd authapp
python3.12 -m venv venv
```

4. Activate Virtual Environment
```bash
source venv/bin/activate
```

5. Install Requirements
```bash
pip install -r requirements.txt
```

6. Run Migrations
```bash
python manage.py migrate
```

7. Create Superuser
```bash
python manage.py createsuperuser
```

8. Run Server
```bash
python manage.py runserver
```
