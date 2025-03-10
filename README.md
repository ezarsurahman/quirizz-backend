# Quirizz Backend
A backend application using Django for RISTEK Recruitment that focuses on the Quirizz application.

## Tech Stack
- Django
- Django REST Framework
- SQLite (or PostgreSQL for production)

## Getting Started
Quick guide on how to get started with this project.

## Prerequisites
- Python (>= 3.8)
- pip
- Git
- PostgreSQL (optional, for production)

## Installation

### Clone the repository
```bash
git clone https://github.com/your-username/quirizz-backend.git
```
### Move into the directory
```
cd quirizz-backend
```
### Create a virtual environment
```
python -m venv env
```
### Activate the virtual environment
On macOS and Linux:
```
source env/bin/activate
```
On Windows:
```
.\env\Scripts\activate
```
### Install all dependencies
```
pip install -r requirements.txt
```

### Apply migrations
on macOS or Linux: use `python3`
```
python3 manage.py makemigrations
python3 manage.py migrate
```
on Windows : use `python`
```
python manage.py makemigrations
python manage.py migrate
```

### Run the application
on macOS and Linux:
```
python3 manage.py runserver
```
on Windonws:
```
python manage.py runserver
```
## API Endpoints
Here are some of the main API endpoints available in this project:

#### Quiz
- GET /api/quiz/ - List all quizzes
- POST /api/quiz/ - Create a new quiz
- GET /api/quiz/:id/ - Retrieve a specific quiz
- PUT /api/quiz/:id/ - Update a specific quiz
- DELETE /api/quiz/:id/ - Delete a specific quiz
#### Questions
- GET /api/questions/ - List all questions
- POST /api/questions/ - Create a new question
- GET /api/questions/:id/ - Retrieve a specific question
- PUT /api/questions/:id/ - Update a specific question
- DELETE /api/questions/:id/ - Delete a specific question
#### Submission
- POST /api/quiz/<quiz_id>/submit/ - Submit answers for a quiz