from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Define your database model here
# Example: class Item(db.Model):

class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    artist = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    album = db.Column(db.Integer, nullable=False)
    

    def __repr__(self):
        return f'<Song {self.song}>'