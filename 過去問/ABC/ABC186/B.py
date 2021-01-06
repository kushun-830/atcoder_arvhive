h, w = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(h)]
ans = 0
minimum = 100

for i in range(h):
    for j in range(w):
        minimum = min(minimum, T[i][j])

for i in range(h):
    for j in range(w):
        ans = ans + (T[i][j] - minimum)

print(ans)