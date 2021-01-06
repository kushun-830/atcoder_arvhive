n = int(input())
s = list(input())
ans = 0

def rest(a):
    if a == "R":
        return(["G", "B"])
    elif a == "G":
        return(["R", "B"])
    else:
        return (["R", "G"])

for i in range(n - 3):
    rest1 = rest(s[i])[0]
    rest2 = rest(s[i])[1]
    ans = ans + s[i + 1:].count(rest1) * s[i + 1:].count(rest2)

    j = i + 1
    k = 1
    while True:
        if (s[j] == rest1 and s[j + k] == rest2) or (s[j] == rest2 and s[j + k] == rest1):
            ans = ans - 1
        k = k + 1
        j = i + k
        if j + k > n - 1:
            break

print(ans)


"""n = int(input())
s = list(input())
ans = 0

def rest(a, b):
    if (a == "R" and b == "G") or (a == "G" and b == "R"):
        return("B")
    elif (a == "R" and b == "B") or (a == "B" and b == "R"):
        return("G")
    else:
        return("R")

for i in range(n - 3):
    for j in range(i + 1, n - 1):
        if s[i] != s[j]:
            parts = s[j + 1:]
            ans = ans + parts.count(rest(s[i], s[j]))

            if 2 * j - i < n:
                if s[2 * j - i] == rest(s[i], s[j]):
                    ans = ans - 1
    print(ans)

print(ans)"""