from flask import Flask, jsonify, request
from flask_cors import CORS
from Movie_DAO import Movie_DAO
from flask.globals import request

movie_handler = Movie_DAO()
app = Flask(__name__)
CORS(app)


movie_handler.new_movie("El gato con botas: el ultimo deseo", "Animation")
movie_handler.new_movie("The Dark Knight", "Action")
movie_handler.new_movie("Spiderman", "Action")
movie_handler.new_movie("The Mitchells vs the Machines", "Animation")

@app.route('/')
def index():
    return "<h1> Hello from backend </h1>"

# Endpoint para agregar una película
@app.route("/api/new-movie", methods=['POST'])
def new_movie():
    
    name=request.json['name']
    genre=request.json['genre']
    if(movie_handler.new_movie(name, genre)):
        response = {
            "state": "perfect",
            "message": "Pelicula añadida correctamente"
        }
        return response
    else:
        response = {
            "state": "error",
            "message": "La pelicula ya existe"
        }
        return response

# Endpoint para obtener todas las películas por género
@app.route("/api/all-movies-by-genre/<genre>", methods=['GET'])
def movies_by_genre(genre):
    return movie_handler.movies_by_genre(genre)

# Endpoint para actualizar una película
@app.route("/api/update-movie", methods=['PUT'])
def update_movie():
    data = request.get_json()
    
    movie_id = data.get('movieId')
    name = data.get('name')
    genre = data.get('genre')
    
    if movie_id is None or name is None or genre is None:
        return jsonify({"message": "Falta información en la solicitud"}), 400

    print (movie_handler.movies)
    for movie in movie_handler.movies:
        if movie.id == movie_id:
            movie.name = name
            movie.genre = genre
            return jsonify({"message": f"La película '{name}' fue actualizada con éxito"})

    return jsonify({"message": f"No se encontró una película con ID"})


if __name__ == '__main__':
    app.run(threaded=True, port=5000, debug=True)



    '''
    data = request.get_json()
    movie_id = data.get('movieId')
    name = data.get('name')
    genre = data.get('genre')
    
    if movie_id is None or name is None or genre is None:
        return jsonify({"message": "Falta información en la solicitud"}), 400

    for movie in movie_handler.movies:
        if movie['movieId'] == movie_id:
            movie['name'] = name
            movie['genre'] = genre
            return jsonify({"message": f"La película '{name}' fue actualizada con éxito"})
    return jsonify({"message": f"No se encontró una película con ID {movie_id}"})
    '''