class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Dog(Animal):
    def voice(self):
        print("How HOW How")


class Cat(Animal):
    def getVoice(self):
        print("Miau MIAU Miau")


class Wolf(Dog):
    def getVoice(self):
        print("Jestem wilkiem, ")
        super().voice()


dog = Dog("Reksio", 10)
print(dog.name)
print(dog.age)
dog.voice()
print(dog.name)

cat = Cat("Bury", 5)
cat.getVoice()

wolf = Wolf("Geralt", 55)
wolf.getVoice()
print(wolf.name)
