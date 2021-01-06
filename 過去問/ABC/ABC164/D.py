s = list(input())
ans = 0

for i in range(len(s) - 3):
    for j in range(i + 4, len(s) + 1):
        tmp = int("".join(s[i:j]))
        if tmp % 2019 == 0:
            ans = ans + 1

print(ans)