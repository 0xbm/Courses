import numpy as np

array_a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])

array_b = array_a.reshape(2, 8)  # the result of multiplication must be 16 (16 values)
array_c = array_a.T
print("Reshape array_a to 2r and 8c:\n", array_b)
print("Reverse array_c - look at 6 line:\n", array_c.T)

print("------ EXERCISE (2r from array_c) ------)")
print("array_c:\n", array_c)

print("2rows from_array:\n", array_c[0], array_c[1])
print("------ EXERCISE (2nd col in array_a with negative index) ------)")
print("array_a:\n", array_a)
print("Second col:\n ", array_a[:, -3])
print("Third value from array_a (10):\n", array_a[2][1])
