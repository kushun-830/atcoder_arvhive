x, y, a, b, c = map(int, input().split())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
R = list(map(int, input().split()))
Pl = 0
Ql = 0
Rb = 0

P.sort(reverse = True)
Q.sort(reverse = True)
R.sort(reverse = True)

P = P[0:x]
Q = Q[0:y]

#while (P[-1 - Pl] < R[0 + Rb] or Q[-1 - Ql] < R[0 + Rb]):
#while (P[-1 - Pl] < R[0 + Rb] or Q[-1 - Ql] < R[0 + Rb]) and (Pl != len(P) or Ql != len(Q)):
while Pl != len(P) or Ql != len(Q):
    if Pl == len(P):
        if Q[-1 - Ql] < R[0 + Rb]:
            Q[-1 - Ql] = R[0 + Rb]
            Ql = Ql + 1
        else:
            break
    elif Ql == len(Q):
        if P[-1 - Pl] < R[0 + Rb]:
            P[-1 - Pl] = R[0 + Rb]
            Pl = Pl + 1
        else:
            break

    elif Q[-1 - Ql] >= P[-1 - Pl] and P[-1 - Pl] < R[0 + Rb]:
        P[-1 - Pl] = R[0 + Rb]
        Pl = Pl + 1
    elif P[-1 - Pl] > Q[-1 - Ql] and Q[-1 - Ql] < R[0 + Rb]:
        Q[-1 - Ql] = R[0 + Rb]
        Ql = Ql + 1

    else:
        break

    Rb = Rb + 1
    if Rb == len(R):
        break

print(sum(P) + sum(Q))