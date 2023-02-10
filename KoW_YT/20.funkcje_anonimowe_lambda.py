print("1 sposob - dlugi")


def funkcja(f, liczba):
    return f(liczba + 1)


print(funkcja(lambda x: x * x, 3))

print("----------TEST---------")


def funkcja(f, litera):
    return f(litera)


print(funkcja(lambda x: x * 2, "michal "))


def funkcja(g):
    return g + g


print(funkcja("michal "))
print("----------TEST---------")

print("2 sposob - dlugi")


def kwadrat(x):
    return x * x


print(kwadrat(5))

print("3 sposob - dlugi")
wyn = (lambda x: x * x)(5)
print(wyn)
print((lambda x: x * x)(10))

print("4 sposob")
lam = lambda x: x * x
print(lam(15))
print(lam(5))

print("5 sposob")
lam2 = lambda x, y: x * y
print(lam2(3, 3))
print((lambda x, y: x * y)(2, 3))
