n, k = map(int, input().split())

if n > k:
    n = n - (n // k) * k

print(min(abs(n - k), n))