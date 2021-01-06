import math
l = int(input())

print(math.factorial(l - 1) // (math.factorial(l - 12) * math.factorial(11)))