import numpy as np


a2d = np.ones((9,9), dtype=np.int8)
a2d[1:-1,1:-1] = 0
a2d[2:-2,2:-2] = 1
a2d[3:-3,3:-3] = 0
a2d[4, 4] = 1

# print(a2d)

array_1 = np.array([1,2,3,4,5], dtype=np.int8)
array_2 = np.array([1,2,3], dtype=np.int8)

print(
    array_1[:,np.newaxis] * array_2
)