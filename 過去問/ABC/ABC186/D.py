n = int(input())
A = list(map(int, input().split()))
A.sort()
ans = 0
diff = 0

for i in range(1, n):
    diff = (A[i] - A[i - 1]) * i * (n - i)
    ans = ans + diff

print(ans)