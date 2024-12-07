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
from sqlalchemy.pool import StaticPool

app = Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db?check_same_thread=False"

app.config["JWT_SECRET_KEY"] = "07f68d6ff8accdc14850"
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
    "poolclass": StaticPool,
    "connect_args": {"check_same_thread": False},
}
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {"connect_args": {"timeout": 30}}
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)


class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.id"), nullable=False)

    movie = db.relationship("Movie", backref="favorites")

    __table_args__ = (
        db.UniqueConstraint("user_id", "movie_id", name="unique_favorites"),
    )

    def __repr__(self):
        return f"<Favorite(user_id={self.user_id}, movie_id={self.movie_id})>"


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)

    favorites = db.relationship("Favorite", backref="user", lazy=True)

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

    favorited_by = db.relationship("Favorite", backref="favorited_movie", lazy=True)
    comments = db.relationship("Comment", backref="movie", lazy=True)

    def __repr__(self):
        return f"Movie('{self.title}', '{self.overview}')"


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __repr__(self):
        return f"Comment('{self.content}', '{self.timestamp}')"


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

    if not username or not password:
        return jsonify({"message": "Username and password are required"}), 400

    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"message": "User not found"}), 401

    if not user.check_password(password):
        return jsonify({"message": "Invalid password"}), 401

    user = User.query.filter_by(username=username).first()

    access_token = create_access_token(identity=username)
    return jsonify({"access_token": access_token, "username": username}), 200


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
            "poster": movie.poster or "/placeholder.jpg",
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
    movie = db.session.get(Movie, movie_id)
    if not movie:
        return jsonify({"error": "Movie not found"}), 404

    movie_details = {
        "id": movie.id,
        "title": movie.title,
        "overview": movie.overview,
        "poster": movie.poster,
        "release_date": movie.release_date,
    }
    return jsonify(movie_details), 200


@app.route("/movies/<int:movie_id>/comments", methods=["POST"])
@jwt_required()
def add_comment(movie_id):
    current_user_id = get_jwt_identity()

    if not current_user_id:
        return jsonify({"error": "Unauthorized. Please log in first."}), 401

    user = User.query.filter_by(username=current_user_id).first()

    print("User", user.id)

    movie = db.session.get(Movie, movie_id)
    if not movie:
        return jsonify({"error": "Movie not found"}), 404

    content = request.json.get("content")
    if not content or content.strip() == "":
        return jsonify({"error": "Comment content cannot be empty"}), 400

    try:
        comment = Comment(content=content, movie_id=movie.id, user_id=user.id)
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
    except Exception as e:
        db.session.rollback()
        print(f"Error adding comment: {str(e)}")
        return jsonify({"error": "Failed to add comment"}), 500


@app.route("/movies/<int:movie_id>/comments", methods=["GET"])
def get_comments(movie_id):
    movie = db.session.get(Movie, movie_id)
    if not movie:
        return jsonify({"error": "Movie not found"}), 404

    comments = Comment.query.filter_by(movie_id=movie.id).all()

    comment_list = []
    for comment in comments:
        user = db.session.get(User, comment.user_id)
        comment_list.append(
            {
                "id": comment.id,
                "content": comment.content,
                "timestamp": comment.timestamp,
                "user_id": comment.user_id,
                "username": user.username if user else "Unknown",
            }
        )

    return jsonify(comment_list), 200


@app.route("/favorites", methods=["POST"])
@jwt_required()
def add_to_favorites():
    current_user_id = get_jwt_identity()

    movie_id = request.json.get("movie_id")
    if not movie_id:
        return jsonify({"error": "Movie ID is required"}), 400

    user = User.query.filter_by(username=current_user_id).first()

    movie = db.session.get(Movie, movie_id)
    if not movie:
        return jsonify({"error": "Movie not found"}), 404

    existing_favorite = Favorite.query.filter_by(
        user_id=user.id, movie_id=movie_id
    ).first()
    if existing_favorite:
        return jsonify({"message": "Movie is already in favorites"}), 200

    favorite = Favorite(user_id=user.id, movie_id=movie_id)
    db.session.add(favorite)
    db.session.commit()

    return jsonify(
        {"message": f"'{movie.title}' has been added to your favorites!"}
    ), 201


@app.route("/favorites", methods=["GET"])
@jwt_required()
def get_favorites():
    current_user_id = get_jwt_identity()
    user = User.query.filter_by(username=current_user_id).first()

    if not user:
        return jsonify({"error": "User not found"}), 404

    search_query = request.args.get("search", "").strip().lower()
    sort_by = request.args.get("sort_by", "title")
    sort_order = request.args.get("order", "asc")

    favorites = Favorite.query.filter_by(user_id=user.id)

    if search_query:
        favorites = favorites.join(Movie).filter(Movie.title.ilike(f"%{search_query}%"))

    if sort_by == "title":
        favorites = favorites.join(Movie).order_by(
            Movie.title.asc() if sort_order == "asc" else Movie.title.desc()
        )
    elif sort_by == "release_date":
        favorites = favorites.join(Movie).order_by(
            Movie.release_date.asc()
            if sort_order == "asc"
            else Movie.release_date.desc()
        )

    favorites = favorites.all()

    favorite_list = [
        {
            "id": favorite.movie.id,
            "title": favorite.movie.title,
            "poster": favorite.movie.poster,
            "overview": favorite.movie.overview,
            "release_date": favorite.movie.release_date,
        }
        for favorite in favorites
    ]

    return jsonify(favorite_list), 200


@app.route("/favorites/<int:movie_id>", methods=["DELETE"])
@jwt_required()
def remove_favorite(movie_id):
    current_user_id = get_jwt_identity()
    user = User.query.filter_by(username=current_user_id).first()

    if not user:
        return jsonify({"error": "User not found"}), 404

    favorite = Favorite.query.filter_by(user_id=user.id, movie_id=movie_id).first()

    if not favorite:
        return jsonify({"error": "Movie not found in favorites"}), 404

    try:
        db.session.delete(favorite)
        db.session.commit()
        return jsonify({"message": "Movie removed from favorites"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Failed to remove movie from favorites"}), 500


@app.route("/movies/search", methods=["GET"])
def search_movies():
    query = request.args.get("q", "").strip()
    page = int(request.args.get("page", 1))
    per_page = int(request.args.get("per_page", 20))
    offset = (page - 1) * per_page

    if not query:
        return jsonify({"message": "Search query (q) is required"}), 400

    movies = (
        Movie.query.filter(Movie.title.ilike(f"%{query}%"))
        .offset(offset)
        .limit(per_page)
        .all()
    )

    total_movies = Movie.query.filter(Movie.title.ilike(f"%{query}%")).count()

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
            "poster": movie.poster or "/placeholder.jpg",
            "release_date": movie.release_date,
        }
        for movie in movies
    ]

    response = {
        "movies": movie_list,
        "total_pages": total_pages,
        "current_page": page,
        "per_page": per_page,
        "total_results": total_movies,
    }

    return jsonify(response), 200


with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True, threaded=False)