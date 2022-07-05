import numpy as np
a=np.mat("1 0 2 3;2 3 1 0;1 -2 4 7")
b=np.mat("4 1 3 ;1 1 0 ;-1 2 3")
print(np.linalg.matrix_rank(a))