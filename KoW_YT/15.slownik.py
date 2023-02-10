slownik = {1:"Poniedzialek", 2: "Wtorek", 7:"Niedziela"}

print(slownik)
print(slownik[1])
slownik[3]="Sroda"
slownik[4]= False
slownik[5]=5
print(slownik)
slownik["a"]= 1
print(slownik["a"])
print(slownik)

print(slownik.get(8, "Inny dzien"))

print("\nPętla: ")
for l in slownik.values():
    print(l)

print("\n-----")
print(slownik.pop(1))
print(slownik)
print(slownik.popitem())
