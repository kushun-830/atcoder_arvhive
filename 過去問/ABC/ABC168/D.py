n, m = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(m)]

root = [[False for j in range(n)] for i in range(n)]
ans = [0] * (n - 1)

for i in range(m):
    root[T[i][0] - 1][T[i][1] - 1] = True
    root[T[i][1] - 1][T[i][0] - 1] = True

num = 1
tmp = [0]

while True:
    for k in range(len(tmp)):
        for i in range(n):
            if root[tmp[k]][i] == True:
                tmp1.append(i)

    i = i + 1

    if i == 3:
        break
