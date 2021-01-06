s = input()
ans = "Yes"

if s != s[::-1]:
    ans = "No"

s1 = s[0:int((len(s) - 1) / 2)]
if s1 != s1[::-1]:
    ans = "No"

print(ans)

"""s = input()
l = int(len(s))
ans = "Yes"

for i in range(int((l - 1) / 2)):
    if s[i] != s[-1 - i]:
        ans = "No"

half = int((l - 1) / 2)
s1 = s[0:half]
s2 = s[half + 1:]

if half % 2 == 0:
    for i in range(int(half / 2)):
        if s1[i] != s1[-1 - i]:
            ans = "No"
        if s2[i] != s2[-1 - i]:
            ans = "No"
else:
    for i in range(int((half - 1) / 2)):
        if s1[i] != s1[-1 - i]:
            ans = "No"
        if s2[i] != s2[-1 - i]:
            ans = "No"

print(ans)"""

