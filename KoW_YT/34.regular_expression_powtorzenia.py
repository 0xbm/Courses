import re


if re.match("[A-Z][a-z]$", "Ala"):
    print("Dopasowano")
else:
    print("Nie dopasowano")

if re.match("[A-Z][a-z]", "Ala"):
    print("Dopasowano")
else:
    print("Nie dopasowano")

if re.match("^[A-Z][a-z]", "Ala"):
    print("Dopasowano")
else:
    print("Nie dopasowano")

if re.match("^[A-Z][a-z]*$", "Alaaaaaa"):
    print("Dopasowano")
else:
    print("Nie dopasowano")

if re.match("^[A-Z]+$", "A"):
    print("Dopasowano")
else:
    print("Nie dopasowano")

if re.match("^[A-Z][a-z]+$", "A"):
    print("Dopasowano")
else:
    print("Nie dopasowano")

if re.match("^[A-Z][a-z]?[A-Z]$", "All"):
    print("Dopasowano")
else:
    print("Nie dopasowano")

if re.match("^[A-Z][a-z]a{1,2}[a-z]{,10}$", "Alaabam"):
    print("Dopasowano")
else:
    print("Nie dopasowano")
