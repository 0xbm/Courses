import numpy as np

# 3rows x 3columns
seq_a = [1, 2, 3]
seq_b = [4, 5, 6]
seq_c = [7, 8, 9]
seq_d = [10.5, 11.6, 12.7]
array_abc = np.array([seq_a, seq_b, seq_c, seq_d])
print(array_abc)
print(array_abc.shape)

print("------ EXERCISE:4 rows and 3 col ------")
array_d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10.5, 11.6, 12.7]])
print(array_d)
