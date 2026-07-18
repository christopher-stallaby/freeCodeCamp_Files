class Movie:
    """Parent class representing a movie."""
    def __init__(self, title, year, director, duration):
        if title == '' or not title.strip():
            raise ValueError("Title cannot be empty")
        if year < 1895:
            raise ValueError("Year must be 1895 or later")
        if director == '' or not director.strip():
            raise ValueError("Director cannot be empty")
        if not (duration > 0):
            raise ValueError("Duration must be positive")
        self.title = title
        self.year = year
        self.director = director
        self.duration = duration

    def __str__(self):
        return f"{self.title} ({self.year}) - {self.duration} min, {self.director}"

class TVSeries(Movie):
    """Child class representing an entire TV series."""
    def __init__(self, title, year, director, duration, seasons, total_episodes):
        super().__init__(title, year, director, duration)
        if seasons < 1:
            raise ValueError("Seasons must be 1 or greater")
        if total_episodes < 1:
            raise ValueError("Total episodes must be 1 or greater")
        self.seasons = seasons
        self.total_episodes = total_episodes

    def __str__(self):
        return f"{self.title} ({self.year}) - {self.seasons} seasons, {self.total_episodes} episodes, {self.duration} min avg, {self.director}"
        
class MediaError(Exception):
    """Custom exception for media-related errors."""
    def __init__(self, message, obj):
        super().__init__(message)
        self.obj = obj

class MediaCatalogue:
    """A catalogue that can store different types of media items."""
    def __init__(self):
        self.items = []

    def add(self, media_item):
        if not isinstance(media_item, Movie):
            raise MediaError("Only Movie or TVSeries instances can be added", media_item)
        self.items.append(media_item)

    def __str__(self):
        if not self.items:
            return "Media Catalogue (empty)"
        movies = self.get_movies()
        series = self.get_tv_series()
        result = f"Media Catalogue ({len(self.items)} items):\n\n"
        if movies:
            result += "=== MOVIES ===\n"
            for i, movie in enumerate(movies, 1):
                result += f"{i}. {movie}\n"
        return result
    
    def get_movies(self):
        movie_list = []
        for item in self.items:
            if type(item) == Movie:
                movie_list.append(item)
        return movie_list
    
    def get_tv_series(self):
        series_list = []
        for item in self.items:
            if type(item) == TVSeries:
                series_list.append(item)
        return series_list

    
catalogue = MediaCatalogue()

try:
    movie1 = Movie("The Dark Knight", 2015, "Christopher Nolan", 208)
    catalogue.add(movie1)
    movie2 = Movie("Man of Steel", 2015, "Christopher Nolan", 175)
    catalogue.add(movie2)
    series1 = TVSeries("The Chosen", 2020, "Dallas Jenkins", 90, 7, 56)
    catalogue.add(series1)
    series2 = TVSeries("Doctor Who", 1963, "Stephen Moffat", 40, 75, 1500)
    catalogue.add(series2)
    print(catalogue)
except ValueError as e:
    print(f"Validation Error: {e}")
except MediaError as e:
    print(f"Media Error: {e}")
    print(f"Unable to add {e.obj}: {type(e.obj)}")