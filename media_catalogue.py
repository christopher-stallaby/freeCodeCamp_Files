class Movie:
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
    
class MediaCatalogue:
    def __init__(self):
        self.items = []

    def add(self, media_item):
        self.items.append(media_item)

    def __str__(self):
        if not self.items:
            return "Media Catalogue (empty)"
        result = f"Media Catalogue ({len(self.items)} items):\n\n"
        for index, item in enumerate(self.items, start=1):
            result += f"{index}. {item}\n"
        return result
    
catalogue = MediaCatalogue()

try:
    movie1 = Movie("The Dark Knight", 2015, "Christopher Nolan", 208)
    catalogue.add(movie1)
    movie2 = Movie("Man of Steel", 2015, "Christopher Nolan", 175)
    catalogue.add(movie2)
    print(catalogue)
except ValueError as e:
    print(f"Validation Error: {e}")