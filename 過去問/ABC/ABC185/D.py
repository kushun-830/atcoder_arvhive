import math
n, m = map(int, input().split())
array = list(map(int, input().split()))
array.sort()

if m == 0:
    ans = 1
elif n == m:
    ans = 0
else:
    min_dist = n
    if array[0] != 1:
        min_dist = array[0] - 1
    for i in range(1, m):
        if array[i] != array[i - 1] + 1:
            min_dist = min(array[i] - array[i - 1] - 1, min_dist)
    if array[m - 1] != n:
        min_dist = min(n - array[m - 1], min_dist)

    ans = 0
    if array[0] != 1:
        ans = math.ceil((array[0] - 1) / min_dist)
    for i in range(1, m):
        if array[i] != array[i - 1] + 1:
            ans = ans + math.ceil((array[i] - array[i - 1] - 1) / min_dist)
    if array[m - 1] != n:
        ans = ans + math.ceil((n - array[m - 1]) / min_dist)

print(ans)