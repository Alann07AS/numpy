import numpy as np

import itertools as it

data = '''
nan,-2.30,-4.59,-4.83,3.13,4.13,1.07,2.29,0.44,4.35
2.30,nan,3.57,-4.66,2.30,-3.24,3.63,0.41,-2.00,-0.77
4.59,-3.57,nan,1.47,1.15,-1.16,4.97,4.81,1.86,1.50
4.83,4.66,-1.47,nan,0.25,-1.90,-0.14,3.89,4.34,-1.42
-3.13,-2.30,-1.15,-0.25,nan,3.90,-2.73,1.23,-4.16,3.33
-4.13,3.24,1.16,1.90,-3.90,nan,-0.50,2.96,-2.69,-4.48
-1.07,-3.63,-4.97,0.14,2.73,0.50,nan,4.42,-1.35,-3.95
-2.29,-0.41,-4.81,-3.89,-1.23,-2.96,-4.42,nan,4.49,-0.40
-0.44,2.00,-1.86,-4.34,4.16,2.69,1.35,-4.49,nan,2.29
-4.35,0.77,-1.50,1.42,-3.33,4.48,3.95,0.40,-2.29,nan
'''

score_matrix = np.genfromtxt(data.splitlines(), delimiter=',')#, dtype=np.float32)
print(score_matrix)


# Get the number of teams
nb_teams = len(score_matrix)

teams = np.arange(0,nb_teams)

permuts_teams = it.permutations(range(nb_teams))
permuts_teams = np.array(list(permuts_teams)).reshape(-1, nb_teams//2, 2)
print(permuts_teams)


sum = score_matrix[permuts_teams[..., 0], permuts_teams[..., 1]]
print(sum)

sums = np.sum(sum[:]**2, axis=1)
print(sums)

best_set = permuts_teams[np.argmin(sums)].transpose()
print(best_set)