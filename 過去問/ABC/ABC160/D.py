n, x, y = map(int, input().split())
A = [2] * n

A[0] = 1
A[n - 1] = 1
A[x] = A[x] + 1
A[y - 1] = A[y - 1] + 1

for k in range(1, n):
    print(int(sum(A) / 2))
    for i in range(n):
        A[i] = A[i] - 1