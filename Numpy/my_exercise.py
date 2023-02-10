import numpy as np

print("1.Zrob macierz 5x5")
print("2.Wybierz liczbe 25")
print("3.Wybierz liczbe 13")
print("4.Odwroc macierz o 90 stopni")
print("5.Wyswietl ile jest wierzy i ile kolumn \n")
print("6.Wyswietl liczby w 2 kolumnie")
print("7.Wyswietl liczby w 4 wierszu")

array_a = np.array(
    [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25],
    ]
)
print("1.\n", array_a)
print("2.\n", array_a[-1][-1])
print("3.\n", array_a[2][2])
print("4.\n", array_a.T)
print("5.\n", array_a.reshape(5, 5))
print("6.\n", array_a[:, 1])
print("7.\n", array_a[3:4])
