krotka = (2,4,8,16,32,64,128)
print(krotka[0])
print(krotka[6])
print(krotka)

print("Krotka ma", len(krotka), "argumentow")
print("Elementow:", krotka.count(2))
print("Index:", krotka.index(64))

print("\nWycinki:") # Slice
print(krotka[0])
print(krotka[0:3])
a = krotka[3:6]
print(a)
print(krotka[-4:-2])
print(krotka[0:7:2])
print(krotka[:3])
print(krotka[::-1])
