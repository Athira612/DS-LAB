# Reconstruct SVD
from numpy import array
from numpy import diag
from numpy import dot
from scipy.linalg import svd

# define a matrix
A = array([[1, 2,1], [3, 4,2], [5, 6,4]])
print(A)
# SVD
U, s, VT = svd(A)
print(U)
print(s)
print(VT)
Sigma=diag(s)
B=U.dot(Sigma.dot(VT))
print(B)
