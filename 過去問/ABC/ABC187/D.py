n = int(input())
table = [list(map(int, input().split())) for _ in range(n)]

sumAOKI = 0
for i in range(n):
    sumAOKI += table[i][0]
    table[i][1] += table[i][0]

table = sorted(table, reverse = True, key = lambda x: x[0] + x[1])

sumTAKAHASHI = 0
for i in range(n):
    sumAOKI -= table[i][0]
    sumTAKAHASHI += table[i][1]
    if sumTAKAHASHI > sumAOKI:
        print(i + 1)
        break