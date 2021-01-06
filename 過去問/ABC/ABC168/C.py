import math

a, b, h, m = map(int, input().split())

ancleA = 30 * h + 0.5 * m
ancleB = 6 * m

ancle = min(abs(ancleA - ancleB), 360 - abs(ancleA - ancleB))

ans = (a ** 2 + b ** 2 - 2 * a * b * math.cos(math.radians(ancle))) ** 0.5
print(ans)