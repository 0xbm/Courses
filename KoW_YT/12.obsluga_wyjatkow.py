x = 12
y = 0
'''
try:
    print(x / y)
    print("Linijka po")
except ZeroDivisionError:
    print("Nie dziel przez 0! Podaj inna wartosc")
except TypeError:
    print("Blad typow danych")

print("Dalesz intrukcje ... ")
'''

try:
    lista = [3]
    print(lista[1])
    #print(x+"!")
    print(x / y)
    print(x+4)
except (ZeroDivisionError, TypeError, IndexError):
    print("Wystpial 1 z 3 bledow ZDE/TE/IE!")
except:
    print("Inny blad!")
#finally:
#    print("FINALLY! Wykonam sie i tak!")

print("Dalesz intrukcje ... ")

# finally wykonuje sie ZAWSZE
# dodaj hash do 16,17 linii kodu , powinien wykonac sie blad ZDE
# odhashuj 18 linie, zahashuj 16 i 17 to powinien pojawic sie INNY BLAD (24 linijka)
