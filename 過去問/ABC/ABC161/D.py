k = int(input())
A = [0] * k
i = 0
j = 0
treat = [-1, 0, 1]

while i < k:
    if i < 9:
        A[i] = i + 1
        i = i + 1
    else:
        for l in range(3):
            if l == 0 and str(A[j])[-1] == "0":
                continue
            elif l == 2 and str(A[j])[-1] == "9":
                continue
            else:
                A[i] = int(str(A[j]) + str(int(str(A[j])[-1]) + treat[l]))
                i = i + 1

            if i == k:
                break
        j = j + 1

print(A[-1])