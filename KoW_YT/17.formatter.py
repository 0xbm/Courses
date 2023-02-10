lista = list(range(10))

print(lista)

nowa = [i * 2 for i in lista]
nowa2 = [i +2 for i in lista if i % 2 == 0]
print("Nowa : ", nowa)
print("Nowa2 : ", nowa2)

# Formatowanie String

argumenty = ["Seba", 24]
tekst = "Czesc, mam na imie {0} i mam {1} lat".format(argumenty[0],argumenty[1])
print(tekst)

argumenty = ["Radek", 31]
tekst2 = "Czesc, mam na imie {imie} i mam {wiek} lat".format(imie=argumenty[0],wiek=argumenty[1])
print(tekst2)

argumenty = ["Michal", 38]
tekst3 = f"Czesc, mam na imie {argumenty[0]} i mam {argumenty[1]}lat "
print(tekst3)
