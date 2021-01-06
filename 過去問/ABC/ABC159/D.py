


"""n = int(input())
A = list(map(int, input().split()))
ansList = []

for i in range(n):
    ans = 0

    if A[i] in A[0:i - 1] and i != 0:
        num = A.index(A[i])
        ans = ansList[num]
    else:
        At = A[:]
        At.pop(i)

        while At != []:
            lb = len(At)
            s = At[0]

            while s in At:
                At.remove(s)

            la = len(At)
            c = lb - la
            ans = int(ans + (c * (c - 1) / 2))

    ansList.append(ans)
    print(ans)"""