x, y = map(int, input().split(' '))

week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

sum_days = 0
for i in range(x - 1):  # 전 달 까지의 일 수, 시작이 1월달 부터
    sum_days += month[i]
sum_days += y  # x달까지의 일 수 + x달의 날짜 == 현재까지의 일 수

print(week[sum_days % 7])
