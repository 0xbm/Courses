import numpy as np

print("int16,int32,int64")
array_a = np.array([32766, 32767, 32768])
print(array_a)
print(array_a.dtype, "\n")

array_b = np.array([32766, 32767, 32768], dtype=np.int16)
print(array_b)
print(array_b.dtype, "\n")

array_c = np.array([-1, 0, 1], dtype=np.int16)
print(array_c)
print(array_c.dtype, "\n")

print("uint16,uint32,uint64")
array_d = np.array([-1, 0, 1], dtype=np.uint16)
print(array_d.dtype)
