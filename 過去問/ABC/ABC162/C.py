from math import gcd

k = int(input())
ans = 0

for i in range(1, k + 1):
    for j in range(1, k + 1):
      tmp = gcd(i, j)

      for l in range(1, k + 1):
          ans = ans + gcd(tmp, l)

print(ans)