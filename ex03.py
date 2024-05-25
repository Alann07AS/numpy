import numpy as np


np_array = np.arange(1, 101)

odd_array = np_array[::2]
even_array = np_array[::-2]

np_array[1::3] = 0
# ou
# mask = (np_array+1)%3 == 0
# np_array[mask] = 0

print(odd_array)
print(even_array)
print(np_array)
