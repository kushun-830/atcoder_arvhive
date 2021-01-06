n, m = map(int, input().split())

ans = int(n * (n - 1) / 2) + int(m * (m - 1) / 2)

print(ans)


"""n, m = map(int, input().split())
ans = 0

if n >= 2:
    ans = ans + int(n * (n - 1) / 2)

if m >= 2:
    ans = ans + int(m * (m - 1) / 2)

print(ans)
"""