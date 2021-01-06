n, x =map(int, input().split())
s = input()
ans = x

for i in range(len(s)):
    if s[i] == "x":
        ans = max(0, ans - 1)
    else:
        ans = ans + 1

print(ans)