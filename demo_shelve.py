#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO PRESERVE ONE Python
# Object to a file using the pickle module
"""
    DocString
"""
import shelve

movies = { 'hema': ['finding nemo', 'dhurandhar', '83'],
           'kim': ['hot fuzz', 'the princess bride', 'up'],
           'george': ['project hail mary', 'iron man', 'Pirates of the caribbean'],
}

tv_series = { 'hema': ['wednesday', 'cobra kai'],
              'kim': ['taskmaster', 'the traitors'],
              'george': ['breaking bad', 'yellowstone'],
}

books = { 'hema': 'matilda',
          'kim': 'the gruffalo',
          'george': 'GOT',
}

with shelve.open(r"f:\labs\projects\Python_Sep_2026\movies.db") as db:
    db['movies'] = movies
    db['tv_series'] = tv_series
    db['books'] = books

with shelve.open(r"f:\labs\projects\Python_Sep_2026\movies.db") as db:
    print(f"Kim's favourite films are: {db['movies']['kim']}")
    print(f"George's favourite tv series is: {db['tv_series']['george'][0]}")
    print(f"Hema's ultimate book is: {db['books']['hema']}")


