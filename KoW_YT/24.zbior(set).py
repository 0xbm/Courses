liczby1 = {0, 1, 2, 4}
print(liczby1)
slowa = set(["a", "b", "c"])
print(slowa)

liczby1.add(3)
print(liczby1)
liczby1.remove(0)
print(liczby1)
print(1 in liczby1)
print("55" in liczby1)

liczby1 = {0, 1, 2, 3, 4, 5}
liczby2 = {3, 5, 6, 7}
print("Suma zbiorow: ")
print("1 wynik:")
print(liczby1 | liczby2)
print("2 wynik:")
liczby4 = {*liczby1, *liczby2}
print(liczby4)

liczby3 = (liczby1, liczby2)
print(liczby3[0])
print("Liczby powatarzajace sie:")
print(liczby1 & liczby2)
print("Iloczyn dwoch zbiorow:")
print(liczby1 - liczby2)
print(liczby2 - liczby1)

print("Zbiory bez czesci wspolnych:")
print(liczby1 ^ liczby2)

print("Dodatkowo jedna z metod : difference")
print(liczby1.difference(liczby2))
