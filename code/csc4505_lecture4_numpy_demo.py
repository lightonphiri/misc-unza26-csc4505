"""
NumPy crash course: arrays, indexing, slicing, operations, matrix multiplication.
"""
import numpy as np

# 1D array
a = np.array([1, 2, 3, 4])
print("a =", a)

# 2D array
M = np.array([[1, 2, 3], [4, 5, 6]])
print("M =\n", M)

# Special arrays
zeros = np.zeros(5)
ones = np.ones((2, 3))
identity = np.identity(4)
lin = np.linspace(0, 1, 5)
ar = np.arange(0, 10, 2)

print("zeros:", zeros)
print("ones:\n", ones)
print("identity:\n", identity)
print("linspace:", lin)
print("arange:", ar)

# Indexing and slicing
arr = np.array([10, 11, 12, 13, 14])
print("arr[1:4] =", arr[1:4])

M2 = np.array([[0,1,2,3],
               [10,11,12,13],
               [20,21,22,23]])
print("M2[1:3, 1:3] =\n", M2[1:3, 1:3])

# Element-wise operations
x = np.array([1,2,3,4])
y = np.array([2,3,4,5])
print("x + y =", x + y)
print("x * y =", x * y)
print("x ** 2 =", x ** 2)

# Matrix multiplication
v = np.array([1,2,3])
M3 = np.arange(9).reshape(3,3)
print("v @ v =", v @ v)
print("M3 @ v =", M3 @ v)
print("M3 @ M3 =\n", M3 @ M3)

# Reshaping and transposing
g = np.arange(6).reshape(2,3)
print("g reshaped to 2x3:\n", g)
print("g.T (transpose):\n", g.T)
