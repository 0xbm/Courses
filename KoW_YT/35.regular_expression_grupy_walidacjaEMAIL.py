import re

wynik = re.match(r"^(Hello) (Wo(rld))+$", "Hello World")

if wynik:
    print("Dopasowane")
    print(wynik.group())
    print(wynik.group(0))
    print(wynik.group(1))
    print(wynik.group(2))
    print(wynik.group(3))
    print(wynik.groups())
else:
    print("Nie dopasowane")

print("---------")

wynik1 = re.match(r"^(He(?P<first>ll)o)(World)+$", "Hello World World World")

if wynik1:
    print("Dopasowane")
    print(wynik.group())
    # print(wynik.group(0))
    # print(wynik.group(1))
    # print(wynik.group(2))
    # print(wynik.group(3))
    # print(wynik.groups())
    # print(wynik.group("first"))
else:
    print("Nie dopasowane")
