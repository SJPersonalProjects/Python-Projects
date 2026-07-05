# Favorite Movies.

favorite_movies = []

while True:
    movie = input("Enter your favorite movie (q to quit): ")
    if movie.lower() == 'q':
        break

    favorite_movies.append(movie)

counter = 1
for item in favorite_movies:
    print(f"{counter}. {item}")
    counter += 1