#N行複数列の文字列複数を行列として入力
table = [input().split() for l in range(3)]
N = int(input())
array = [input() for i in range(N)]
bingo = ""

for k in range(3):
    for j in range(3):
        if table[k][j] in array:
            table[k][j] = 0

        table[k][j] = int(table[k][j])

for l in range(3):
    if table[l][0] + table[l][1] + table[l][2] == 0:
        bingo = "Yes"

for l in range(3):
    if table[0][l] + table[1][l] + table[2][l] == 0:
        bingo = "Yes"

if table[0][0] + table[1][1] + table[2][2] == 0 or table[2][0] + table[1][1] + table[2][0] ==0:
        bingo = "Yes"

if bingo == "":
    bingo = "No"

print(bingo)