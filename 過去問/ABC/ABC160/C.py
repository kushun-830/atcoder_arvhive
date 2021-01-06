k, n = map(int, input().split())
A = list(map(int, input().split()))
T = [0] * n

A.sort()

for i in range(n):
    if abs(A[i] - A[i - 1]) <= k / 2:
        T[i] = abs(A[i] - A[i - 1])
    else:
        T[i] = k - abs(A[i] - A[i - 1])

print(k - max(T))