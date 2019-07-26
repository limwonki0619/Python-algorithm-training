# https://www.acmicpc.net/problem/10871

N, X = map(int, input().split())
num = input().split()

for i in num:
    if int(i) < X:
        print(i, end=' ')
    else:
        continue