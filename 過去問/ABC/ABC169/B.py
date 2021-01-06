n = int(input())
A = list(map(int, input().split()))

ans = 1
A.sort(reverse = True)
flag = True

if 0 in A:
    ans = 0
    flag = False

if flag:
    for i in range(n):
        ans = ans * A[i]
        if ans > 10 ** 18:
            ans = -1
            break

print(ans)