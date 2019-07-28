t = int(input())
# n, *score = list(map(int, input().split()))

# rate = 0
# for i in score:
#     if i > sum(score) / len(score):
#         rate += 1 / len(score) * 100
# print('{:.3f}%'.format(rate))

# rate = sum([1 / len(score) * 100 for i in score if i > sum(score) / len(score)])
# print('{:.3f}%'.format(rate))

# result = []
# for i in range(t):
#     n, *score = list(map(int, input().split()))
#     result.append(sum([1 / len(score) * 100 for i in score if i > sum(score) / len(score)]))
#     print('{:.3f}%'.format(result[i]))

result = []
for i in range(t):
    n, *score = list(map(int, input().split()))
    print('{:.3f}%'.format(sum([1 / len(score) * 100 for i in score if i > sum(score) / len(score)])))



