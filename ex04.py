import numpy as np


rng = np.random.default_rng(seed=888)


# one_dimensional = np.random.normal(0, 1, 100)
one_dimensional = np.random.randn(100)

two_dimensional = np.random.randint(1, 10 + 1, size=(8, 8))

three_dimensional = np.random.randint(1, 17 + 1, size=(4, 2, 5))

print(one_dimensional)
print(two_dimensional)
print(three_dimensional)