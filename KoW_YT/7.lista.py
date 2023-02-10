zmienna = 1
lista = []

lista.append(zmienna)
print(lista)
lista.append("bator")
print(lista)
print(lista[1])
lista[1] = "batorski"
print(lista)
print(lista + ["batorska"])
print(lista)
print("Ilosc elementow w liscie: ", len(lista))

# Using iteration list
for i in lista:
    print(i)
[print(i) for i in lista]


# Using list comprehension
list = [1, 3, 5, 7, 9]
new_list = [x for x in list]
print(new_list)

print([i for i in list])

# Methods
lista.append("f")
print(lista)

lista.append(["g", "h", "i"])
print(lista)
print(lista[0])
print(lista[3])

lista.insert(1, "michal")
print(lista)

print("Ilosc: ", lista.count("g"))
print("Ilosc: ", lista.count("f"))

print("Index: ", lista.index("f"))
lista.remove(1)
lista[3].remove("g")
del lista[3][0]
print(lista)

L = ["a", ["bb", "cc", "dd"], "e"]
L[1].remove("cc")
print(L)

lista2 = [1, 20, 35, -5, 0]
print("Min: ", min(lista2))
print("Max: ", max(lista2))
lista2.sort()
print(lista2)
lista2.reverse()
print(lista2)
lista2.clear()
print(lista2)
