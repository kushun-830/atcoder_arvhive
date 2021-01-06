n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

i = max()
while A.length != B.length:
    if A[i] == B[i]:
        if A.length > B.length:
            A.pop(A)