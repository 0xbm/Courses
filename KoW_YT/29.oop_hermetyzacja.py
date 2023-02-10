print("1 przyklad: ")


class Test:
    _lista = []

    def dodaj(self, arg):
        self._lista.append(arg)

    def zdejmij(self):
        if len(self._lista) > 0:
            return self._lista.pop(len(self._lista) - 1)
        else:
            return


obj = Test()
obj.dodaj("A")
obj.dodaj("B")
obj.dodaj("C")
obj._lista.append("X")  #
print(obj.zdejmij())
print(obj._lista)  #

print("2 przyklad: ")


class Test2:
    __lista = []

    def dodaj(self, arg):
        self.__lista.append(arg)

    def zdejmij(self):
        if len(self.__lista) > 0:
            return self.__lista.pop(len(self.__lista) - 1)
        else:
            return


obj = Test2()
obj.dodaj("A")
obj.dodaj("B")
obj.dodaj("C")
obj._Test2__lista.append("X")
print(obj.zdejmij())
print(
    obj._Test2__lista
)  # nie powinno byc dostepu do tej listy, nawet z poziomu wywolania listy z klasy
