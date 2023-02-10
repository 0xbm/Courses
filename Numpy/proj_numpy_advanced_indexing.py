import numpy as np
from numpy import matrix, matrixlib

array_a = np.arange(0, 100, 5)
print(array_a)
print(array_a.size)

array_a_reshape = array_a.reshape(4, 5)
print(array_a_reshape)

# negative indexing
print(array_a_reshape[:, -1])

# boolean indexing
array_a_above_50 = array_a_reshape[array_a_reshape >= 50]
print(array_a_above_50)

# python slice
print(array_a_above_50[0 : len(array_a_above_50) : 2])

# slice of a  row
print(array_a_reshape[:, 0:5:2])

print(np.where(array_a_reshape > 50, array_a_reshape, -1))
print(np.where(array_a_reshape > 50, array_a_reshape * 2, -1))

# 1st challange
# neg index with last 3 col
print(array_a_reshape[:, -1:-4:-1])

# 2nd challenge
# values between 20 and 75
between_25_and_75 = np.logical_and(array_a_reshape > 20, array_a_reshape < 75)
result = array_a_reshape[between_25_and_75]
print(result)
