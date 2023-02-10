for i in range(0, 11):
    print(i)

print("----------")
lista = []

for i in range(0, 11):
    lista.append(i)
print(lista)

print("----------")


def gen():
    i = 0
    while i < 11:
        yield i
        i += 1


print(list(gen()))


print("----------")
lista = []

for i in range(0, 11):
    if i % 2 == 0:
        lista.append(i)
print(lista)

print("----------")


def gen():
    i = 0
    while i < 11:
        if i % 2 == 0:
            yield i
        i += 1


print(list(gen()))


for i in gen():
    print(i)
