from application import app, db
from flask import request, jsonify
from application.models import Film

def format_film(film):
  return {
    'title':film.title,
    'release_year':film.release_year,
    'genre':film.genre,
    'director':film.director
  }

@app.route('/')
def main_page():
  return '<p>Welcome to the Film API</p>'

@app.route('/films', methods=['GET'])
def index():
  films = Film.query.all()
  film_list = []
  for film in films:
   film_list.append(format_film(film))
  return {'films': film_list}

@app.route('/films/<id>', methods=['GET'])
def get_film(id):
  film = Film.query.filter_by(id=id).first()
  return format_film(film)

@app.route('/films', methods=['POST'])
def create_film():
  data = request.json
  film = Film(data['title'],data['release_year'],data['director'],data['genre'])
  db.session.add(film)
  db.session.commit()
  return jsonify( id=film.id,title=film.title,release_year=film.release_year,genre=film.genre,director=film.director)

@app.route('/films/<id>', methods=['DELETE'])
def delete_film(id):
  film = Film.query.filter_by(id=id).first()
  db.session.delete(film)
  db.session.commit()
  return 'Film Deleted'

@app.route('/films/<id>', methods=['PATCH'])
def update_film(id):
  film = Film.query.filter_by(id=id).first()
  data = request.json
  film.title = data['title']
  film.release_year = data['release_year']
  film.director = data['director']
  film.genre = data['genre']
  db.session.commit()
  updatedFilm = film
  return format_film(updatedFilm)