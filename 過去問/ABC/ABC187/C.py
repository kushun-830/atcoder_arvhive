n = int(input())
array = set()
arrayEX = set()
for i in range(n):
    s = input()
    if s[0] != "!":
        array.add("!" + s)
    else:
        arrayEX.add(s)

arrayAND = array & arrayEX
arrayAND = list(arrayAND)

if len(arrayAND) == 0:
    print("satisfiable")
else:
    print(arrayAND[0][1:])