s = input()
t = input()

ans = "Yes"

for i in range(len(s)):
    if s[i] != t[i]:
        ans = "No"
        break

print(ans)
