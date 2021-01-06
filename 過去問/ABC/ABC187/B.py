n = int(input())
table = [list(map(int, input().split())) for _ in range(n)]
ans = 0

for i in range(n - 1):
    for j in range(i + 1, n):
        grad = (table[j][1] - table[i][1]) / (table[j][0] - table[i][0])
        if -1 <= grad <= 1:
            ans += 1

print(ans)