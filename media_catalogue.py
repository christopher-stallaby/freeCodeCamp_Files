class Movie:
    def __init__(self, title, year, director, duration):
        self.title = title
        self.year = year
        self.director = director
        self.duration = duration

    def __str__(self):
        return f"{self.title} ({self.year}) - {self.duration} min, {self.director}"
    

movie1 = Movie("The Dark Knight", 2015, "Christopher Nolan", 208)
print(movie1)