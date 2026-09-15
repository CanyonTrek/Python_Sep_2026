#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO 
""" 
    DocString
"""
import pprint
# Created a multi-dimensional dictionary of lists
movies = { 'hema': ['finding nemo', 'dhurandhar', '83'],
           'kim': ['hot fuzz', 'the princess bride', 'up'],
           'george': ['project hail mary', 'iron man', 'Pirates of the caribbean'],
}

# Grow a dict..
movies['donald'] = ['lotr', 'the hobbit', 'project hail mary']

# Shrink a dict..
# del movies['george'] # Deletes Georges key+values from dict
# movies.pop('george') # Deletes Georges key+values from dict
# movies.popitem() # Removes the last key+value pair from dict

# Access a dictionary of lists
pprint.pprint(movies)
print("-" * 50)
print(f"Kim's favourite movies are: {movies['kim']}")
print(f"Kim's favourite movies are: {movies.get('kim')}")
print(f"Hema's favourite movie is {movies['hema'][0]}")

print("-" * 50)
# ITERATE through the dict keys using dict.keys()
for name in movies.keys():
    print(f"{name} likes the following movies: {movies[name]}")

print("-" * 50)
# ITERATE through the dict values using dict.values()
for films in movies.values():
    print(f"Recommended films: {films}")

print("-" * 50)
# ITERATE through the dict key+values using dict.items()
for name, films in movies.items():
    print(f"{name} LOVES these films {films}")