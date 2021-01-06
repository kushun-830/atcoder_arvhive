n, k = map(int, input().split())
ans = 0

for i in range(k, n + 2):
    minValue = i * (i - 1) / 2
    maxValue = n * (n + 1) / 2 - (n - i) * (n - i + 1) / 2

    ans = (ans + (maxValue - minValue + 1)) % (10 ** 9 + 7)

print(int(ans))