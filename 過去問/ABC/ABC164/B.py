a, b, c, d = map(int, input().split())

while True:
    c = c - b

    if c <= 0:
        ans = "Yes"
        break

    a = a - d

    if a <= 0:
        ans = "No"
        break

print(ans)