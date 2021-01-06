n = int(input())
ans = 0

for i in range(2, n + 1):
    ntmp = n
    while ntmp % i == 0:
        ntmp = ntmp // i

    if ntmp % i == 1:
        ans = ans + 1

print(ans)