# 1 PRZYKLAD - funckja lambda zamiast normalnej funkcji

mnozenie = lambda x: x * x
print(mnozenie(5))


def razy(x):
    return x * 2


print(razy("michal"))

# 2 PRZYKLAD
print((lambda x, y: x + y)(2, 3))

# 3 PRZYKLAD
strin = "ja-ty-ona"
wyn = lambda string: string.upper()[::-1]
print(wyn(strin))


# 4 PRZYKLAD z zastosowaniem filter
ages = [10, 20, 25, 33, 44, 55, 66, 77, 88, 99, 100]

print(list(filter(lambda x: x > 50, ages)))
