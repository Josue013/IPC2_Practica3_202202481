from Movie import Movie 
import json

class Movie_DAO:
    def __init__(self):
        self.movies = []
        self.id_counter = 1

    # Funcion para agregar nuevas peliculas
    def new_movie(self, name, genre):
        for movie in self.movies:
            if movie.name == name:
                return False
        new=Movie(self.id_counter, name, genre)
        self.movies.append(new)
        self.id_counter += 1
        return True
    '''
    # Funcion para devolver las peliculas en base a su genero
    def movies_by_genre(self, genre):
        return json.dumps([Movie.dump() for Movie in self.movies if Movie.genre == genre], indent=4 )
    '''

    # Función para devolver las películas en base a su género, incluyendo la película actualizada
    def movies_by_genre(self, genre):
        return json.dumps([Movie.dump() for Movie in self.movies if Movie.genre == genre], indent=4)
    
    

