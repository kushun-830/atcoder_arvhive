n, m = map(int, input().split())
A = list(map(int, input().split()))
ans = 0

for i in range(n):
    if A[i] >= sum(A) / (4 * m):
        ans = ans + 1

if ans >= m:
    print("Yes")
else:
    print("No")