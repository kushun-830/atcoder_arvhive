N, A, B = map(int, input().split())

S = N // (A + B)
n = N - S * (A + B)

if n >= A:
  n_a = A
else:
  n_a = n

print(S * A + n_a)
