###1.Create a  square matrix with random integer values(use randint()) and use appropriate functions to find:
import numpy as np
import numpy as nf
from numpy.linalg import eig
mat = np.random.randint(10, size=(3, 3))
array = nf.random.randint(10, size=(3, 3))
print(mat)

###  i) inverse
M_inverse = np.linalg.inv(mat)
print("inverse of the array")
print(M_inverse)

### ii) rank of matrix
rank = np.linalg.matrix_rank(mat)
print("Rank of the given Matrix ")
print(rank)

### iii) Determinant
det= np.linalg.det(mat)
print("determinant of the given Matrix ")
print(det)

### iv) transform matrix into 1D array
arr=mat.flatten()
print("transform matrix to array ")
print(arr)

###  v) eigen values and vectors
w,v=eig(array)
print('E-value:', w)
print('E-vector', v)