# Flask Movie App Backend

This is a Flask-based backend application for a movie management system. The app supports user authentication, movie browsing, adding comments, and managing favorite movies.

---

## Features

### User Registration and Login:
- Register new users.
- Authenticate users with JWT token-based login.

### Movie Browsing:
- Retrieve a list of movies.
- View movie details.
- Search movies by title with pagination.

### Favorites Management:
- Add movies to favorites.
- Retrieve a user's favorite movies with filtering and sorting.
- Remove movies from favorites.

### Comments:
- Add comments to movies (requires authentication).
- Retrieve comments for a specific movie.

---

## Prerequisites

Make sure you have the following installed:
- **Python 3.7** or above
- **SQLite** (bundled by default with Python installations)

---

## Installation

```bash
git clone https://github.com/your-repo.git
cd your-repo
```

## Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate   # For Linux/Mac
```


## Install dependencies:

```bash 
pip install -r requirements.txt  # mention the libraries here
```

## Run the development server:
```bash
python app.py
```

* Access the API via http://127.0.0.1:5000.


Update the following configurations as required:
* SQLALCHEMY_DATABASE_URI: Set the database connection string (default is SQLite: sqlite:///database.db).
* JWT_SECRET_KEY: Set a secure secret key for JWT (default in the code: "07f68d6ff8accdc14850").

Example Requests

curl -X POST -H "Content-Type: application/json" -d '{"username": "prarthana", "email": "prarthana.desai2004@gmail.com", "password": "password123"}' http://127.0.0.1:5000/register

curl -X POST -H "Content-Type: application/json" -d '{"username": "prarthana", "password": "password123"}' http://127.0.0.1:5000/login

curl -X GET \
 http://127.0.0.1:5000/protected \
 -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTczMjg3Njg4OSwianRpIjoiNzc4ZWU4MDktNTMxZS00NjQ5LTkxYTUtNzRmMDc0M2ZlMDE5IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InByYXJ0aGFuYSIsIm5iZiI6MTczMjg3Njg4OSwiY3NyZiI6IjE5N2Q3NjBlLTc4MmMtNDJlNS1iMTNiLTE2ZTIyZjE4ZmRlYyIsImV4cCI6MTczMjg3Nzc4OX0.L8Jl_J0-BF94um3HTaUXoRN6FWFoU8PvsoEowwb3azo'

curl -X GET \
 http://127.0.0.1:5000/movies \
 -H 'Content-Type: application/json'

License
This project is licensed under the MIT License.