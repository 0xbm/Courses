import numpy as np

array_a = np.array([[1, 2, 3], [4, 5, 6]])
print("Variable array_a: ", array_a)
print(array_a.shape)
row = len(array_a)
col = len(array_a[0])
print(row, "rows and", col, "columns")

print("Number of elements array_a: ", array_a.size)

array_b = array_a.reshape(3, 2)
print("Change array_a (2r and 3c) to 3r and 2c \n", array_b)

array_c = array_a.T
print("Change array_a (2r and 3c) to 3r and 2c \n ", array_c)

print("Fist row is:", array_c[0])
print("Second col is:", array_c[:, 1])
print("First value in first row:", array_c[0][0])
