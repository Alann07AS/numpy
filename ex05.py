import numpy as np


arr1 = np.arange(1, 51)

print(arr1)

arr2 = np.arange(51, 101)

print(arr2)

carr = np.concatenate((arr1, arr2))

print(carr)


# array([[  1,  ... ,  10],
            # ...
    # [ 91,  ... , 100]])
reshape_carr = carr.reshape(10, 10)

print(reshape_carr)

