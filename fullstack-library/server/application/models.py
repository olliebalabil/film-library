from application import db, app

app.app_context().push()

class Film(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(50), nullable=False)
  release_year = db.Column(db.Integer, nullable=False)
  director = db.Column(db.String(50), nullable=False)
  genre = db.Column(db.String(50), nullable=False)

  def __init__(self, title, release_year, director, genre):
    self.title = title
    self.release_year = release_year
    self.director = director
    self.genre = genre

  def __repr__(self):
    return f'{self.title} ({self.release_year}) is a {self.genre} film directed by {self.director}.'
  