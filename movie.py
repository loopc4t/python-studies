class Movie:

    def __init__(self, title, year, language, rating):
        self.title = title
        self.year = year
        self.language = language
        self.rating = rating


my_favorite_movie = Movie("Stage Fright", 1987, "Italian", 3.5)
your_favorite_movie = Movie("Pride and Prejudice", 2005, "English", 4.8)
print("My favorite movie")
print(my_favorite_movie.title)
print(my_favorite_movie.year)
print(my_favorite_movie.language)
print(my_favorite_movie.rating)

print(f"\nYour favorite movie")
print(your_favorite_movie.title)
print(your_favorite_movie.year)
print(your_favorite_movie.language)
print(your_favorite_movie.rating)
