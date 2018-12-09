# Auth-Role demo

## Overview
This project run on Django REST Framework (DRF).

## Requirements
This tool run on Python 3.7 or above

## Installation
Run the following commands in terminal:

1. run the following command to install the dependencies
```bash
pip install -r requirements.txt
```
2. Sync the SQL Lite database for the first time.
```bash
python manage.py migrate
```
3. Create sample data to test authentication and role.
```bash
python manage.py dbseed --users
```

## Database design
![alt text](design.PNG "Logo Title Text 1")

list of roles used in the project
```python
STUDENT = 1
TEACHER = 2
SECRETARY = 3
SUPERVISOR = 4
ADMIN = 5
ROLE_CHOICES = (
  (STUDENT, 'student'),
  (TEACHER, 'teacher'),
  (SECRETARY, 'secretary'),
  (SUPERVISOR, 'supervisor'),
  (ADMIN, 'admin'),
)
```

## APIs
The APIs of project locates in apis folder. Use [Postman](https://www.getpostman.com/) for tests