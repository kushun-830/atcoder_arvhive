x = int(input())
a = 2
b = 0
A = []
A.append(1 ** 5 - x)

while True:
    if (a + 1) ** 5 - a ** 5 > 10 ** 10:
        break
    A.append(a ** 5 - x)
    a = a + 1

while True:
    if b ** 5 in A:
        break
    elif -b ** 5 in A:
        b = -b
        break
    b = b + 1

a = int((x + b ** 5) ** 0.2)

print(a, b)