class Movie:
    def __init__(self, id, name, genre):
        self.id = id
        self.name = name
        self.genre = genre       

    def dump(self):
        return {
            "movieId": self.id,
            "name": self.name,
            "genre": self.genre,
        }

    