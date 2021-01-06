a, b, n = map(int, input().split())
ans = 0

if b == 1:
    ans = 0
else:
    ans = (a * min(n, (b - 1)) / b) // 1 - a * ((min(n, (b - 1)) / b) // 1)

print(int(ans))