def gen():
    i = 0
    while i < 5:
        # print(i)
        # return i
        yield i
        i += 1


print(list(gen()))
print("--------")
for i in gen():
    print(i)

print("--------")


def num():
    for i in range(0, 5):
        print(i)


print(num())

print("--------")
for i in range(0, 5):
    print(i)

print("--------")
i = 0
while i < 5:
    print(i)
    i += 1

print("--------")


def parzyste(x):
    i = 0
    while i <= x:
        if i % 2 == 0:
            yield i
        i += 1


print(list(parzyste(10)))

for i in parzyste(10):
    print(i)
