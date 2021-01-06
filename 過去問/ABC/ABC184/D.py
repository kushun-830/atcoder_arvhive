a, b, c = map(int, input().split())
ans = []
p = 1
kaisuu = 0
zero = [a, b, c].count(0)

def coins(x, y, z, kakuritsu, kaisuu):
    global ansList
    if x == 100 or y == 100 or z == 100:
        ans.append(kakuritsu * kaisuu)
        return
    if x != 0:
        coins(x + 1, y, z, kakuritsu / (3 - zero), kaisuu + 1)
    if y != 0:
        coins(x, y + 1, z, kakuritsu / (3 - zero), kaisuu + 1)
    if z != 0:
        coins(x, y, z + 1, kakuritsu / (3 - zero), kaisuu + 1)

    return

coins(a, b, c, p, kaisuu)

print(sum(ans))