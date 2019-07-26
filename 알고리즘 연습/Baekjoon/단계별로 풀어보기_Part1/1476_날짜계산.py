# 준규 E, S, M

# 1 <= E <= 15
# 1 <= S <= 28
# 1 <= M <= 19

# 1 == 1, 1, 1
# 15 == 15, 15 ,15
# 16 == 1, 16, 16

# 문제풀이 : https://webolutions.tistory.com/125


E, S, M = map(int, input().split())
year = 1

while True:
    if (year - E) % 15 == 0 and (year - S) % 28 == 0 and (year - M) % 19 == 0:
        break
    year += 1

print(year)

