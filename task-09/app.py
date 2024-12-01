from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, jwt_required, create_access_token

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["JWT_SECRET_KEY"] = "07f68d6ff8accdc14850"
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)


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


@app.route("/register", methods=["POST"])
def register():
    username = request.json.get("username")
    email = request.json.get("email")
    password = request.json.get("password")

    user = User(username, email, password)
    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User created successfully!"}), 201


@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username")
    password = request.json.get("password")

    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        access_token = create_access_token(identity=username)
        return jsonify({"access_token": access_token}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401


@app.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    return jsonify({"message": "Hello, authenticated user!"}), 200


@app.route("/movies", methods=["GET"])
def get_movies():
    movies = Movie.query.all()
    movie_list = []
    for movie in movies:
        movie_data = {
            "id": movie.id,
            "title": movie.title,
            "overview": movie.overview,
            "poster": movie.poster,
            "release_date": movie.release_date,
        }
        movie_list.append(movie_data)
    return jsonify(movie_list), 200


with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)