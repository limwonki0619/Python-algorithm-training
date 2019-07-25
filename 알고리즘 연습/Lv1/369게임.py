# 369게임

# 369게임은 여러명이 둘러앉아 숫자를 하나씩 돌아가며 말하다 숫자에 3,6,9가
# 포함도니 숫자가 되면 박수를 치는 게임이다.

# (이 때, 해당 숫자에 3,6,9가 여러개이면 박수를 개수만큼 쳐야한다.
# 예를들어 33, 36의 경우 박수를 두번 쳐야한다.)

# 게임이 끝난 숫자 N이 주어졌을 때, N 이전까지 박수를 친 횟수를 구하라.


user_input = input()

pop = 0
for i in range(1, int(user_input)+1):
    for k in list(str(i)):
        if '3' in str(k):
            pop += 1
        elif '6' in str(k):
            pop += 1
        elif '9' in str(k):
            pop += 1

print(pop)



