N, M = map(int,(input().split()))
table = [input().split() for l in range(M)]
ans = 0
array1 = []
array2 = []
array3 = []
keta1 = -1
keta2 = -1
keta3 = -1
s1 = 0
s2 = 0
s3 = 0
for k in range(M):
    for j in range(2):
        table[k][j] = int(table[k][j])

for k in range(M):
    if table[k][0] == 1:
        if (N != 1 and table[k][1] == 0) or (not(table[k][1] in array1) and s1 == 1):
            keta1 = -1
        else:
            keta1 = table[k][1]
        s1 = 1
        array1.append(table[k][1])

    elif table[k][0] == 2:
        if not(table[k][1] in array2) and s2 == 1:
            keta2 = -1
        else:
            keta2 = table[k][1]
        s2 = 1
        array2.append(table[k][1])
    else:
        if not(table[k][1] in array3) and s3 == 1:
            keta3 = -1
        else:
            keta3 = table[k][1]
        s3 = 1
        array3.append(table[k][1])

if s1 != 1:
    keta1 = 1
if s2 != 1 or M == 0:
    keta2 = 0
if s3 != 1 or M == 0:
    keta3 = 0
if N == 1 and M == 0:
    keta1 = 0

if keta1 == -1 or keta2 == -1 or keta3 == -1:
    ans = -1
elif N == 3:
    ans = keta1 * 100 + keta2 * 10 + keta3
elif N == 2:
    ans = keta1 * 10 + keta2
else:
    ans = keta1

print(ans)