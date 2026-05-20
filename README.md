# Blog

A Django blog application

## Requirements

- Python 3.12 or newer (required for Django 6)

## Setup

### 1. Create and activate a virtual environment

```bash
python -m venv venv
```

```bash
source venv/bin/activate
```

### 2. Install dependencies

```bash
pip install django
```

### 3. Apply database migrations

```bash
python manage.py migrate
```

This creates the SQLite database file (`db.sqlite3`).

### 5. Run the development server

```bash
python manage.py runserver
```

Open [http://127.0.0.1:8000/blogapp/](http://127.0.0.1:8000/blogapp/) in your browser.
