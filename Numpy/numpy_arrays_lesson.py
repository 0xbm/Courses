import numpy as np

array_a = np.array([1, 2, 3, 4, 5])
print("Variable array_a: ", array_a)
print("4th value is: ", array_a[3])
print("Type of variable array_a: ", type(array_a))
print("Type of index 0 in variable array_a: ", type(array_a[0]))

print("Numbers of values/elements in variable array_a: ", array_a.shape)

array_b = np.array([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]])
print("Variable array_b: ", array_b)
print(
    "Numbers of values/elements in variable array_b: 2 ROWS and 5 COLUMNS ",
    array_b.shape,
)

print("------")
l = [1, 2, 3, 4, 5, "michael"]
print("Variable l (list): ", type(l))
print("Type of index 1 in variable l: ", type(l[1]))


print("------")
array_a = np.array([1, 2, 3, 4, 5, "michael"])
print(array_a)
print(type(array_a))
print(type(array_a[0]))  # every index change to STRING
print(array_a.shape)
print(type(array_a.shape))
print("------")
