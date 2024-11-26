from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Define your database model here
# Example: class Item(db.Model):

class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artist = db.Column(db.String(100), nullable=False)
    title = db.Column(db.Text)
    length = db.Column(db.interger, nullable=False)
    genre = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.string, default=False)

    def __repr__(self):
        return f'<Fish {self.Fish}>'