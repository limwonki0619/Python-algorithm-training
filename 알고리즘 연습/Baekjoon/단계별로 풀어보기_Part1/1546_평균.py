n = int(input())
score = list(map(int, input().split()))
M = max(score)

# new_score = 0
# for i in score:
#     new_score += (i/M * 100) / len(score)

print('{:4.2f}'.format(sum([(i / M * 100) / len(score) for i in score])))

