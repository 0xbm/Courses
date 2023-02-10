print("1 sposob *****")


def decorator(func):  # nazwa funkcji ktora bedzie udekorowana
    def wrapper():
        print("------------")
        func()
        print("------------")

    return wrapper


def hello():
    print("Hello World")


hello2 = decorator(hello)
hello2()


print("2 sposob ******")


@decorator  # nazwa funkcji ktora bedzie udekorowana
def witaj():
    print("Witaj Swiecie")


witaj()
print("***")
hello3 = decorator(witaj)
hello3()
print("***")
hello4 = witaj
hello4()
print("***")
hello()
