class Czlowiek:
    def __init__(self, imie):
        self.imie = imie

    def przedstaw(self):
        print("Nazywam sie/init/ " + self.imie)

    @classmethod
    def nowy_czlowiek(cls, imie):
        print("JO//CM " + imie)
        return cls(imie)

    @staticmethod
    def przywitaj(arg, foo):
        print("Witaj/SM/ " + arg + " " + str(foo))
        # return "Witaj/SM/ " + arg


obj = Czlowiek("Michal")
obj.przedstaw()

cz1 = Czlowiek.nowy_czlowiek("Agata")
cz1.przedstaw()

Czlowiek.nowy_czlowiek("Macias")

Czlowiek.przywitaj("Ziomek", 11)
# Czlowiek.nowy_czlowiek("Ziomek")
# Czlowiek.nowy_czlowiek("Agata")
