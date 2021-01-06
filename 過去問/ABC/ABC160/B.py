x = int(input())

fiveH = x // 500
print(fiveH * 1000 + (x - fiveH * 500) // 5 * 5)