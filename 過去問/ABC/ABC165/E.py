n, m = map(int, input().split())

if n % 2 == 1:
    for i in range(m):
        print(i + 1, n - i)
else:
    for i in range(m - 1):
        print(i + 1, n - i - 1)
    print(m, n - m - 1)