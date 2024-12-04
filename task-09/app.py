from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import (
    JWTManager,
    jwt_required,
    create_access_token,
    get_jwt_identity,
)
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["JWT_SECRET_KEY"] = "07f68d6ff8accdc14850"
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __repr__(self):
        return f"Comment('{self.content}', '{self.timestamp}')"
    
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = bcrypt.generate_password_hash(password).decode("utf-8")

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    overview = db.Column(db.Text, nullable=False)
    poster = db.Column(db.String(200), nullable=False)
    release_date = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Movie('{self.title}', '{self.overview}')"

@app.errorhandler(Exception)
def handle_global_error(e):
    print(f"Global Error: {str(e)}")

    return jsonify(
        {
            "message": "An unexpected error occurred. Please try again later.",
            "error": str(e),
        }
    ), 500

@app.route("/register", methods=["POST"])
def register():
    if (
        not request.json.get("username")
        or not request.json.get("email")
        or not request.json.get("password")
    ):
        return jsonify(
            {"message": "Missing required fields: username, email, password."}
        ), 400

    username = request.json.get("username")
    email = request.json.get("email")
    password = request.json.get("password")

    if User.query.filter_by(email=email).first():
        return jsonify({"message": "An account with this email already exists."}), 400

    if User.query.filter_by(username=username).first():
        return jsonify(
            {"message": "Username is already taken. Please choose another."}
        ), 400

    try:
        user = User(username, email, password)
        db.session.add(user)
        db.session.commit()

        return jsonify({"message": "User created successfully!"}), 201

    except db.DatabaseError as e:
        db.session.rollback()  # Roll back to maintain session consistency
        return jsonify({"message": "Error registering user."}), 500

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return jsonify({"message": "An unexpected error occurred."}), 500

@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username")
    password = request.json.get("password")

    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        access_token = create_access_token(identity=username)
        return jsonify({"access_token": access_token, "username": username}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401

@app.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    return jsonify({"message": "Hello, authenticated user!"}), 200

@app.route("/movies", methods=["GET"])
def get_movies():
    page = int(request.args.get("page", 1))
    per_page = int(request.args.get("per_page", 20))
    offset = (page - 1) * per_page
    movies = Movie.query.offset(offset).limit(per_page).all()
    total_movies = Movie.query.count()
    total_pages = (
        total_movies // per_page + 1
        if total_movies % per_page != 0
        else total_movies // per_page
    )

    movie_list = [
        {
            "id": movie.id,
            "title": movie.title,
            "overview": movie.overview,
            "poster": movie.poster,
            "release_date": movie.release_date,
        }
        for movie in movies
    ]

    response = {
        "movies": movie_list,
        "total_pages": total_pages,
        "current_page": page,
        "per_page": per_page,
    }

    return jsonify(response), 200

@app.route("/movies/<int:movie_id>", methods=["GET"])
def get_movie_details(movie_id):
    movie = Movie.query.get(movie_id)

    if not movie:
        return jsonify({"error": "Movie not found"}), 404

    comments = Comment.query.filter_by(movie_id=movie_id).all()

    movie_details = {
        "id": movie.id,
        "title": movie.title,
        "overview": movie.overview,
        "poster": movie.poster,
        "release_date": movie.release_date,
        "comments": [
            {
                "id": comment.id,
                "content": comment.content,
                "timestamp": comment.timestamp,
                "user_id": comment.user_id,
                "username": User.query.get(comment.user_id).username,
            }
            for comment in comments
        ],
    }

    return jsonify(movie_details)

@app.route("/movies/<int:movie_id>/comments", methods=["POST"])
@jwt_required()
def add_comment(movie_id):
    current_user_id = get_jwt_identity()

    if not current_user_id:
        return jsonify({"error": "Unauthorized. Please log in first."}), 401

    movie = Movie.query.get(movie_id)
    if not movie:
        return jsonify({"error": "Movie not found"}), 404
    print("Headers:", request.headers)
    print("Payload:", request.json)

    content = request.json.get("content")
    if not content or content.strip() == "":
        return jsonify({"error": "Comment content cannot be empty"}), 400

    comment = Comment(content=content, movie_id=movie.id, user_id=current_user_id)
    db.session.add(comment)
    db.session.commit()

    return jsonify(
        {
            "message": "Comment added successfully!",
            "comment": {
                "id": comment.id,
                "content": comment.content,
                "timestamp": comment.timestamp,
                "user_id": comment.user_id,
            },
        }
    ), 201

@app.route("/movies/<int:movie_id>/comments", methods=["GET"])
def get_comments(movie_id):
    movie = Movie.query.get(movie_id)
    if not movie:
        return jsonify({"error": "Movie not found"}), 404
    comments = Comment.query.filter_by(movie_id=movie.id).all()

    comment_list = []
    for comment in comments:
        user = User.query.get(comment.user_id)
        comment_list.append(
            {
                "id": comment.id,
                "content": comment.content,
                "timestamp": comment.timestamp,
                "user_id": comment.user_id,
                "username": user.username
                if user
                else "Unknown", 
            }
        )
    return jsonify(comment_list), 200

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)