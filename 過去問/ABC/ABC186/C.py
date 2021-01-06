n = int(input())
ans = 0

for i in range(1, n + 1):
    i_str = str(i)
    i_oct = str(oct(i))
    if "7" not in i_str and "7" not in i_oct:
        ans = ans + 1

print(ans)