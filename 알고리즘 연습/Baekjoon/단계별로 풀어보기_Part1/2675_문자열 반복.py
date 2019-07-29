T = int(input())

for i in range(T):
    rn, S = input().split()

    output = ''
    for k in list(S):
        output += k * int(rn)
    print(output)
