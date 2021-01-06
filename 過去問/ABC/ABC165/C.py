import itertools
n, m, q = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(q)]

A = list(itertools.combinations_with_replacement(range(1, m + 1), n))
ans = 0

for i in range(len(A)):
    tmp = 0
    for j in range(q):
        if A[i][T[j][1] - 1] - A[i][T[j][0] - 1] == T[j][2]:
            tmp = tmp + T[j][3]
    ans = max(ans, tmp)

print(ans)