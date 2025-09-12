"""
Program for If statement in Python
"""

movies = ["Indian", "Gilli", "Anjathe", "Thuppakki"]
print("original list:", movies)
# Sort the list values
movies.sort()
print("sorted list:", movies)

# Create a new list with all movie names in lowercase
lowercase_movies = [movie.lower() for movie in movies]
print("lowercase movies:", lowercase_movies)
if "thuppakki" in lowercase_movies:
    print("Thuppakki is in the list!")
