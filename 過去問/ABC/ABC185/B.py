n, m, t = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(m)]
batteri = n
ans = "Yes"

for i in range(m):
    if i == 0:
        batteri = batteri - T[i][0]
    else:
        batteri = batteri - (T[i][0] - T[i - 1][1])

    if batteri <= 0:
        ans = "No"
        break

    batteri = min(n, batteri + (T[i][1] - T[i][0]))

batteri = batteri - (t - T[m - 1][1])
if batteri <= 0:
    ans = "No"

print(ans)