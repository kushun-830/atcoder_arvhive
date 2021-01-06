n, m = map(int, input().split())
A = list(map(int, input().split()))

if n >= sum(A):
    print(n - sum(A))
else:
    print(-1)