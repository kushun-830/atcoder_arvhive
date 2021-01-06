N = int(input())
n = 0

if N % 2 == 0:
    n = N / 2
else:
    n = (N + 1)/2

print(int(n))