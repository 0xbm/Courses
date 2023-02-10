class Czlowiek:
    imie = "Michal"

    def przedstawSie(self):
        return "Witam, mam na imie " + self.imie


obiekt = Czlowiek()
print(obiekt.imie)
print(obiekt.przedstawSie())
obiekt2 = Czlowiek()
obiekt2.imie = "Adrian"
print(obiekt2.przedstawSie())


class Czlowiek:
    imie = "Michal"

    def przedstawSie(self, powitanie="Czesc"):
        return powitanie + ", mam na imie " + self.imie


obiekt3 = Czlowiek()
print(obiekt3.imie)
print(obiekt3.przedstawSie())
obiekt4 = Czlowiek()
obiekt4.imie = "Adrian"
print(obiekt4.przedstawSie())


class Czlowiek:
    def __init__(self, imie, wiek):
        self.wiek = wiek
        self.imie = imie

    def przedstawSie(self, powitanie="Czesc"):
        return powitanie + ", mam na imie " + self.imie + " i lat " + str(self.wiek)


obiekt5 = Czlowiek("Michal", 37)
print(obiekt5.imie)
print(obiekt5.przedstawSie())
obiekt6 = Czlowiek("Macias", 37)
obiekt6.imie = "Adrian"
print(obiekt6.przedstawSie())
