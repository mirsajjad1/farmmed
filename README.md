# FarmMed

FarmMed is a Pharmacy Management System built with Django.

## Features

- Authentication System
- Role-based Access
- Medicine Management (CRUD)
- POS Sales System
- Sales History
- Dashboard Analytics
- Profit Calculation
- Low Stock Alerts

## Tech Stack

- Django
- SQLite
- Bootstrap 5
- Django Crispy Forms

## Installation

```bash
git clone <repo-url>
cd farmmed

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate
python manage.py runserver