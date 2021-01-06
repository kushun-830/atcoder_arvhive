n, m = map(int, input().split())
H = list(map(int, input().split()))
T = [list(map(int, input().split())) for _ in range(m)]

ans = [1] * n

for i in range(m):
    if H[T[i][0] - 1] > H[T[i][1] - 1]:
        ans[T[i][1] - 1] = 0
    elif H[T[i][0] - 1] < H[T[i][1] - 1]:
        ans[T[i][0] - 1] = 0
    else:
        ans[T[i][0] - 1] = 0
        ans[T[i][1] - 1] = 0

print(ans.count(1))