animals = ["dog", "cat", "parrot", "rabbit"]
numbers = [1, 5, 7, 8]

new = []
for i in numbers:
    if i > 3:
        new.append(i)
        continue
print(new)

print(list(filter(lambda x: x > 3, numbers)))


# for i in animals:
#     print(i)
#     if i > str.index>3:
#         break

print(animals.index("dog"))

nowa = []
for i in animals:
    nowa.append(len(animals[0]))
    nowa.append(len(animals[1]))
    nowa.append(len(animals[2]))
    nowa.append(len(animals[3]))
    break
# print(list(dict.fromkeys(nowa))) # usuniecie duplikatow
print(nowa[0])


for x in animals:
    if len(x) == nowa[0]:
        print(x)

for x in animals:
    if len(x) == 6:
        print(x)
