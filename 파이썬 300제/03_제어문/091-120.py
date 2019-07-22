# 091 ~ 120 파이썬 제어문

# ***
# 091 : 파이썬에서 True 혹은 False를 갖는 데이터 타입은 무엇인가?

# Boolean 데이터 타입

# True 값을 갖는 경우  :
# False 값을 갖는 경우 :



# 092 : 아래 코드의 출력 결과를 예상하라.
print(3 == 5 ) # False


# 093 : 아래 코드의 출력 결과를 예상하라.
print(3 < 5 )  # True


# 094 : 아래 코드의 결과를 예상하라
x = 4
print(1 < x < 5)  # True


# 095 : 아래 코드의 결과를 예상하라.
print((3 == 5 and 4 != 3)) # False and True : False


# 096 : 아래 코드에서 에러가 발행하는 원인에 대해 설명하라.
# print(3 => 4)  # 부등호가 먼저 나오고, =이 나와야 한다.


# 097 : 아래 코드의 출력결과를 예상하라.
# if 4 < 3:
#     print('Hello world')  # 아무것도 나오지 않는다. 논리값이 False이기 떄문.


# 098 : 아래 코드의 출력결과를 예상하라.
# if 4 < 3:
#    #  print("Hello World.")
# else:
#     print("Hi, there.")  # Hi, there.가 출력된다.


# 099 : 아래 코드의 출력 결과를 예상하라.
# if True:
#     print('1')
#     print('2')
# else:
#     print('3')
# print(4)  # 1, 2, 4가 출력된다.



# 100 : 아래 코드의 출력 결과를 예상하라.
# if True :
#     if False:
#         print("1")
#         print("2")
#     else:
#         print("3")
# else :
#     print("4")
# print("5")  # 3, 5가 출력된다.


# 101 : 사용자로부터 입력받은 문자열을 두 번 출력하라.
# 아래는 사용자가 "안녕하세요"를 입력한 경우의 출력 결과이다.
text = input()
print(text * 2)

# 102 : 사용자로부터 하나의 숫자를 입력받고, 입력받은 숫자에 10을 더해 출력하라.
num = int(input('숫자를 입력하세요:'))
print(num + 30)

# 103 : 사용자로부터 하나의 숫자를 입력받고 짝수/홀수를 판별하라.
num2 = int(input())
if num2 % 2 == 0:
    print('짝수')
else:
    print('홀수')


# 104 : 사용자로부터 값을 입력받은 후 해당 값에 +20을 더한 값을 출력하라. 단 값의 범위는 0~255로 가정한다.
#       255를 초과하는 경우 255를 출력해야 한다.
num3 = int(input())
if num3 <= 235:
    print('입력값:', num3)
    print('출력값:', num3 + 20)
else:
    print('입력값:', num3)
    print('출력값:', 255)


# 105 : 사용자로부터 하나의 값을 입력받은 후 해당 값에 20을 뺀 값을 출력하라.
#       단 값의 범위는 0~255이다. 0보다 작은 값이되는 경우 0을 출력해야 한다.
num4 = int(input())
if num4 >= 20:
    print('입력값: {0}  출력값: {1}'.format(num4, num4-20))
else:
    print('입력값: {0}  출력값: {1}'.format(num4, 0))

# 106 : 사용자로부터 입력받은 시간이 정각인지 판별하라.
time = input('현재시간:')

if '00' in time[-2:]:
    print('정각 입니다.')
else:
    print('정각이 아닙니다.')


# 107 : 사용자로 입력받은 단어가 아래 fruit 리스트에 포함되어 있는지를 확인하라.
#       포함되었다면 "정답입니다"를 아닐 경우 "오답입니다" 출력하라.
fa = input('좋아하는과일은? ')
fruit = ["사과", "포도", "홍시"]

if fa in fruit:
    print('정답입니다.')
else:
    print('정답이 아닙니다.')


# 108 : 투자 경고 종목 리스트가 있을 때 사용자로부터 종목명을 입력 받은 후
#       해당 종목이 투자 경고 종목이라면 '투자 경고 종목입니다'를
#       아니면 "투자 경고 종목이 아닙니다."를 출력하는 프로그램을 작성하라.

warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]

user_invest = input()

if user_invest in warn_investment_list:
    print('투자 경고 종목입니다.')
else:
    print('투자 경고 종목이 아닙니다.')


# 109 : 아래와 같이 fruit 딕셔너리가 정의되어 있다.
#       사용자가 입력한 값이 딕셔너리 키 (key) 값에 포함되었다면
#       "정답입니다"를 아닐 경우 "오답입니다" 출력하라.

fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
user_season = input('제가 좋아하는 계절은 ')

if user_season in fruit.keys():
    print('정답입니다.')
else:
    print('정답이 아닙니다.')


# 110 : 위의 딕셔너리에서 사용자가 입력한 값이 딕셔너리 값 (value)에
#       포함되었다면 "정답입니다"를 아닐 경우 "오답입니다" 출력하라.

user_fruit = input('좋아하는 과일은? ')

if user_fruit in fruit.values():
    print('정답입니다.')
else:
    print('오답입니다.')

