import numpy as np


# an integer, a float, a string, a dictionary, a list, a tuple, a set and a boolean.
np_array = np.array([
    1,
    1.01,
    "Hello There",
    {"Un":"Dico"},
    [1,2,3],
    (True, 2, '3'),
    {"un", "set"},
    True
], dtype=object)

for i in np_array:
    print(type(i))