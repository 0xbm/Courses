import re

if re.match("^ko.$", "kotttt"):
    print("Dopasowano")
else:
    print("Nie dopasowano")

if re.match("ko.", "kotttt"):
    print("Dopasowano")
else:
    print("Nie dopasowano")

if re.match("[A-Z]o.", "Kot"):
    print("Dopasowano")
else:
    print("Nie dopasowano")

if re.match("^[A-Za-z]o.$", "kot"):
    print("Dopasowano")
else:
    print("Nie dopasowano")

if re.match("^[A-Za-z]o.$", "kotek"):
    print("Dopasowano")
else:
    print("Nie dopasowano")

if re.match("^[^A-Za-z]o.$", "-ot"):
    print("Dopasowano")
else:
    print("Nie dopasowano")

if re.match("^[Rr]o.[-=+][0-9][0-9][0-9][0-9]$", "rok-1000"):
    print("Dopasowano")
else:
    print("Nie dopasowano")
