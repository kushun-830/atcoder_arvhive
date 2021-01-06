import itertools
n, m, x = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(n)]

A = list(range(1, n + 1))
M = [0] * m
ans = -1

for i in range(1, n + 1):

    if i == 1:
        tmp = A
    else:
        tmp = list(itertools.combinations(range(1, n + 1), i))
    for j in range(len(tmp)):
        flag = True
        if i == 1:
            tmp1 = [0]
        else:
            tmp1 = [0] * len(tmp)

        if i == 1:
            for l in range(m):
                M[l] = T[tmp[j] - 1][l + 1]
        else:
            for ii in range(i):
                for l in range(m):
                    M[l] = M[l] + T[tmp[j][ii] - 1][l + 1]

            for jj in range(len(tmp1)):
                for k in range(m):
                    if M[k] < 10:
                        flag = False
                        break
                    tmp1[jj] = tmp1[jj] + T[k][0]

                if i == 1 and flag == False:
                    ans = -1
                    break
                elif i == 1 and flag == True:
                    ans = tmp1[jj]
                elif flag == True:
                    ans = min(ans, tmp1[jj])
                M = [0] * m

print(ans)