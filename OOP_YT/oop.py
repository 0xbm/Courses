class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def bark(self):
        print("bark")


d = Dog("Tom", 22)
# print(type(d))
d.bark()
d2 = Dog("Bill", 15)
# print(type(d2))
print(d2.get_name())
d.get_age()
dogs = ["Bob", "Dex"]
d3 = Dog(dogs, 6)
d3.get_age()

for i in dogs:
    print(d3.get_name())
    print(d3.get_age())
