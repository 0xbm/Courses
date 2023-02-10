class Test:
    def __del__(self):
        print("Bye Class")


obj = Test()  # referencja 1
obj2 = obj  # referencja 2
print("Koniec")
lista = [obj2]
print("'Koniec' powinien wykonac sie jako pierwszy, nastepnie 'Bye Class'")
print("----------------")
del obj  # zbijanie referencji
del obj2  # zbijanie referencji
print("Koniec")
