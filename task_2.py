class Movies: 
    def __init__(self, movies=None):
        if movies is None:
            self.movies = []
        else:
            self.movies = movies
    
    def add_movie(self, movie):
        self.movies.append(movie)
        return self.movies

class Comedy(Movies):
    def add_movie(self, movie):
        super().add_movie(movie)
        return f"Комедии: {self.movies}"

class Drama(Movies):
    def add_movie(self, movie):
        super().add_movie(movie)
        return f"Драмы: {self.movies}"


comedies = Comedy()
dramas = Drama()

# Вызываем методы
print(comedies.add_movie("Большой куш"))
print(dramas.add_movie("Оружейный барон"))