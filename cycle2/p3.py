import numpy as np
print("an uninitialized array")
x=np.empty([2, 2])
print(x)
print("array with all elements as 1,")
y=np.full((2, 2), 1)
print(y)
print("all elements as 0")
z=np.full((2, 2), 0)
print(z)
