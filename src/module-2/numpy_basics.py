"""
Introduction to NumPy - Fundamentals
"""

import numpy as np

# Creating arrays
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)

# 2D array
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d)

# Array from range
arr_range = np.arange(0, 10, 2)
print(arr_range)

# Array of zeros
arr_zeros = np.zeros((3, 3))
print(arr_zeros)

# Array of ones
arr_ones = np.ones((2, 4))
print(arr_ones)

# Array of evenly spaced values
arr_linspace = np.linspace(0, 10, 5)
print(arr_linspace)

# Random array
arr_random = np.random.rand(3, 3)
print(arr_random)

# Array attributes
print(arr2d.shape)
print(arr2d.dtype)
print(arr2d.size)
print(arr2d.ndim)

# Indexing
print(arr1[0])
print(arr1[-1])
print(arr1[1:4])

# 2D indexing
print(arr2d[0, 1])
print(arr2d[1, :])
print(arr2d[:, 2])

# Slicing
print(arr2d[0:2, 1:3])

# Reshaping
arr_reshape = arr1.reshape(5, 1)
print(arr_reshape)

# Flattening
arr_flat = arr2d.flatten()
print(arr_flat)

# Concatenation
arr_concat = np.concatenate([arr1, np.array([6, 7, 8])])
print(arr_concat)

# Stacking
arr_stack = np.vstack([arr2d, np.array([[10, 11, 12]])])
print(arr_stack)

# Element-wise operations
arr_add = arr1 + 10
print(arr_add)

arr_mult = arr1 * 2
print(arr_mult)

arr_square = arr1**2
print(arr_square)

# Array operations on 2D arrays
arr_sum = arr2d + arr2d
print(arr_sum)

# Broadcasting
arr_broadcast = arr1 + np.array([100])
print(arr_broadcast)

# Comparison operations
arr_comparison = arr1 > 2
print(arr_comparison)

# Boolean indexing
arr_filtered = arr1[arr1 > 2]
print(arr_filtered)

# Statistical functions
print(np.sum(arr1))
print(np.mean(arr1))
print(np.std(arr1))
print(np.min(arr1))
print(np.max(arr1))

# Axis-wise operations
print(np.sum(arr2d, axis=0))
print(np.sum(arr2d, axis=1))
print(np.mean(arr2d, axis=0))

# Matrix operations
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

# Element-wise multiplication
print(matrix1 * matrix2)

# Matrix multiplication
print(np.dot(matrix1, matrix2))

# Transpose
print(matrix1.T)

# Linear algebra
determinant = np.linalg.det(matrix1)
print(determinant)

# Inverse
inverse = np.linalg.inv(matrix1)
print(inverse)

# Eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(matrix1)
print(eigenvalues)
print(eigenvectors)

# Solving linear equations (Ax = b)
A = np.array([[3, 1], [1, 2]])
b = np.array([9, 8])
x = np.linalg.solve(A, b)
print(x)

# Unique elements
arr_unique = np.unique(np.array([1, 2, 2, 3, 3, 3]))
print(arr_unique)

# Sorting
arr_unsorted = np.array([3, 1, 4, 1, 5, 9, 2, 6])
arr_sorted = np.sort(arr_unsorted)
print(arr_sorted)

# Argmax and argmin
print(np.argmax(arr1))
print(np.argmin(arr1))

# Where
arr_where = np.where(arr1 > 3, arr1 * 10, arr1)
print(arr_where)

# Clip
arr_clip = np.clip(arr1, 2, 4)
print(arr_clip)
