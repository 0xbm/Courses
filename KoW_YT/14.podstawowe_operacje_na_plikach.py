# plik = open("14.test.txt", "w")

plik = open("14.test.txt", "a")

if plik.writable():
    plik.write(input("Wprowadz tekst: ") + "\n")

plik.close()
'''
plik = open("14.test.txt", "r")
if plik.readable():
    print("Zawartosc pliku:")
    #tekst = plik.readlines()
    #print(tekst)
    for l in tekst:
        print(l)

plik.close()
'''
