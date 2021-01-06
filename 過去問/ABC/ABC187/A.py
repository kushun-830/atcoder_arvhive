a, b = map(str, input().split())

if int(a[0]) + int(a[1]) + int(a[2]) >= int(b[0]) + int(b[1]) + int(b[2]):
    print(int(a[0]) + int(a[1]) + int(a[2]))
else:
    print(int(b[0]) + int(b[1]) + int(b[2]))