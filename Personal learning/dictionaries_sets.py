#dictionaries used to store key-value pairs
my_favorite_book = {
    "title": "The Subtle Art of Not Giving a Fuck",
    "author": "Mark Manson",
    "publication year": "2016" }
my_favorite_book['publication_year'] = 2025
print(my_favorite_book)

#sets do not allow duplicate values, great to keep track of unique ellements
#sets are unordered -elements are not retrieved in the same order that are added
my_favorite_movies = {"Gossip Girls", "Notebook", "1+1", "Suits", "Interstellar"}
my_favorite_movies.add("Fast and Furios")
my_favorite_movies.remove("Gossip Girls")
print(my_favorite_movies)
 