n, k = map(int, input().split())
A = list(map(int, input().split()))

#T = [0] * (n + 1)
T = [1]

for i in range(1, n + 1):
    if A[T[i - 1] - 1] in T:
        last = i
        break
    else:
        T.append(A[T[i - 1] - 1])

start = T.index(A[T[last - 1] - 1])

if k <= last:
    print(T[k])
else:
    print(T[start + (k - start) % (last - start)])