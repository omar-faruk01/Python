"""
First, the application must allow to add new movies to the collection;
• The application must allow users to view all the movies in their collection;
• The application must also allow users to find any particular movie by any of its attributes


-Enter 'a' to add a movie, 'l' to see your movie, 'f' to find a movie, and 'q' to quit:
-add movies
-see movies
-find a movie
-stop running the program

Task:
[x]: Decide where to store movies
[x]: What is the format of a movie
[x]: Show the user the main interface and get their input
[x]: Allow users to add movies
[x]: Show all their movies
[x]: Find a movie
[x]: Stop running the program when they type 'q'

"""


movies = []

"""

movie = {
'name': ...(str)
'director': ...(str)
'year': ...(str)

}

"""


def menu():
    user_input = input("Enter 'a' to add a movie, '1' to see your movie, 'f' to find a movie, and 'q' to quit: ")

    while user_input != 'q':
        if user_input == 'a':
            add_movie()
        elif user_input == 'l':
            show_movies(movies)
        elif user_input == 'f':
            find_movie()
        else:
            print("Unknown command, please try again.")

        user_input = input("\nEnter 'a' to add a movie, '1' to see your movie, 'f' to find a movie, and 'q' to quit: ")

def add_movie():
    name = input("Enter the name of movie: ")
    director = input("Enter the name of director: ")
    year = input("Enter the release year: ")

    movies.append({
        'name': name,
        'director': director,
        'year': year
    })


def show_movies(movies_list):
    for movie in movies_list:
        show_movies_details(movie)

def show_movies_details(movie):
    print(f"Name: {movie['name']}")
    print(f"Director: {movie['director']}")
    print(f"Release year: {movie['year']}")

def find_movie():
    find_by = input("What attribute of the movie are you looking for? ")
    looking_for = input("What are you searching for? ")

    found_movies = find_by_attribute(movies, looking_for, lambda x: x[find_by])

    show_movies(found_movies)

def find_by_attribute(items, expected, finder):
    found = []

    for i in items:
        if finder(i) == expected:
            found.append(i)

    return found


menu()
