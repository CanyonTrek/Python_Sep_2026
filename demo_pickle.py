#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO PRESERVE ONE Python
# Object to a file using the pickle module
"""
    DocString
"""
import pickle
import pprint
import gzip # But also we have bz2, tarfile, shutil

movies = { 'hema': ['finding nemo', 'dhurandhar', '83'],
           'kim': ['hot fuzz', 'the princess bride', 'up'],
           'george': ['project hail mary', 'iron man', 'Pirates of the caribbean'],
           'donald': ['lotr', 'the hobbit', 'project hail mary']
}

# with open(r"f:\labs\projects\Python_Sep_2026\movies.p", mode="wb") as fh_out:
with gzip.open(r"f:\labs\projects\Python_Sep_2026\movies.pgz", mode="wb") as fh_out:
    # pickle.dump(movies, fh_out, protocol=5) # Protocol (0=ASCII, 1-5=Binary)
    # pickle.dump(movies, fh_out, pickle.DEFAULT_PROTOCOL)  # Currently 4
    pickle.dump(movies, fh_out, pickle.HIGHEST_PROTOCOL)  # Currently 5

# with open(r"f:\labs\projects\Python_Sep_2026\movies.p", mode="rb") as fh_in:
with gzip.open(r"f:\labs\projects\Python_Sep_2026\movies.pgz", mode="rb") as fh_in:
    films = pickle.load(fh_in)

pprint.pprint(movies)
print("-" * 60)
pprint.pprint(films)