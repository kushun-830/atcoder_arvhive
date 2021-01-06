n = int(input())
ans = 0

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

A = make_divisors(n)

for i in range(1, len(A)):
    if n % A[i] == 0:
        n = n // A[i]
        ans = ans + 1
    elif n < A[i]:
        break

print(ans)