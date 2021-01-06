n, k = map(int, input().split())
L = [0] * n
for i in range(k):
    d = int(input())
    tmp = list(map(int, input().split()))

    for j in range(len(tmp)):
        if L[tmp[j] - 1] == 0:
            L[tmp[j] - 1] = 1

print(L.count(0))