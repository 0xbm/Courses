from random import randint

los = randint(1, 10)
odp = 11
i = 0
print("Zgadnij liczbe z przedzialu 1-10")

while odp != los:
    i += 1
    odp = int(input("Podaj liczbe: "))
    if odp > los:
        print("Niestety, wylsowana liczba jest mniejsza od Twojej")
    elif odp < los:
        print("Niestety, wylsowana liczba jest wieksza od Twojej")
print("Brawo, zgadles za ", i, " razem")
