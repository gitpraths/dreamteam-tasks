from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    overview = db.Column(db.Text, nullable=False)
    poster = db.Column(db.String(200), nullable=False)
    release_date = db.Column(db.Integer, nullable=False)

def load_movie_data():
    with open("movie_data.json") as f:
        movie_data = json.load(f)
    for movie in movie_data:
        new_movie = Movie(
            title=movie["title"],
            overview=movie["overview"],
            poster=movie["poster"],
            release_date=movie["release_date"],
        )
        db.session.add(new_movie)
    db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        load_movie_data()