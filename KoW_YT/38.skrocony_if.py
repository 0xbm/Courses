print("Prawda") if 5 > 5 else print("Nieprawda")

a = "Prawda" if 10 % 2 == 0 else "Nieprawda"
print(a)

for i in range(10):
    if i > 5:
        break  # jak zmienisz na `continue` to wyprintuje Koniec
else:
    print("Koniec")


try:
    a = 5 / 5
except ZeroDivisionError:
    print("Blad")
else:
    print("KONIEC")
