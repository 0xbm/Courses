print(";".join(["a","b","c"]))

print("Witaj Swiecie".replace("Witaj", "Czesc"))
print("To jest zdanie".startswith("To jex"))
print("To jest zdanie".startswith("To jes"))
print("To jest zdanie".endswith("zdani"))
print("TO" in "To jest zdanie")
print("To jest zdanie".upper())
print("To jest zdanie".lower())

print("-----------")

lista = [10,20,26,36,40]
lista2 = [10,20,25,35,40]

if all([i % 2 == 0 for i in lista]):
    print("Wszystkie parzyste")

if any([i % 2 == 0 for i in lista2]):
    print("Chociaz 1 parzysta")

for i in enumerate(lista):
    print(i)
print(type(i))

for i in enumerate(lista):
    print(i[0]+1, "-", i[1])
