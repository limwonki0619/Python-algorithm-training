num = int(input())
hs = 0

for i in range(1, num+1):
    if i <= 99:  # 1 ~ 99는 모두 등차수열
        hs += 1
    else:
        num_list = list(map(int, str(i)))  # 자릿수 분리
        if num_list[0] - num_list[1] == num_list[1] - num_list[2]:  # 등차수열 확인
            hs += 1
print(hs)

# 코드출처 : https://roseline124.github.io/algorithm/2019/03/29/Algorithem-baekjoon-1065.html
