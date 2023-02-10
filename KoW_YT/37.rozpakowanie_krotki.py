a, b = (2, 5)
print(a)
print(b)

x = 10
y = 20
x, y = y, x
print("x:", x, "y:", y)

start, *wszytsko, koniec = (1, 2, 3, 4, 5, 6, 7)
print(start)
print(wszytsko)
print(koniec)

print("")
listToStr = " ".join(map(str, wszytsko))
print(listToStr)
print("")
