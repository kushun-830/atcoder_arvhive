x = int(input())
yokin = 100
ans = 1

while True:
    yokin = yokin * 1.01 // 1

    if yokin >= x:
        break

    ans = ans + 1

print(ans)