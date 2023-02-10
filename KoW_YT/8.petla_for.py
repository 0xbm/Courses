rodzina = ["mama", "tata", "agata", "michal"]

i = 0
while i < len(rodzina):
    print(rodzina[i])
    i += 1

# for jest petla obiektowa

for i in rodzina:
    print(i)

for y in range(10):
    print(y)

for z in range(1,10,3):
    print(z)

# list cpmprehension
print([i for i in rodzina])
