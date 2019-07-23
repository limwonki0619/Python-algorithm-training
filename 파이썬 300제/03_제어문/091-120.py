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


# 111 : 사용자로부터 문자 한 개를 입력 받고,
#       소문자일 경우 대문자로, 대문자 일 경우, 소문자로 변경해서 출력하라.

user = input()
if user.islower() == True:
    print(user.upper())
else:
    print(user.lower())


# 112 : 점수 구간에 해당하는 학점이 아래와 같이 정의되어 있다.
#       81~100 A, 61~80 B, 41~60 C, 21~40 D, 0~20 E
score = int(input('score:'))
83
if score > 80:
    print('grade is A')
elif score > 61:
    print('grade is B')
elif score > 41:
    print('grade is C')
elif score > 21:
    print('grade is D')
else:
    print('grade is E')


# 113 : 사용자로부터 달러, 엔, 유로, 또는 위안 금액을 입력받은 후
#       이를 원으로 변환하는 프로그램을 작성하라.
#       각 통화별 환율은 다음과 같다.
#       사용자는 100 달러, 1000 엔, 13 유로, 100 위안과 같이
#       금액과 통화명 사이에 공백을 넣어 입력한다고 가정한다.

price, money = input('입력:').split()

if money == '달러':
    print('{0:<10,.2f}'.format(int(price)*1167)+'원')  # {(인덱스):(정렬위치)(0개수)(천단위 콤마)(소수점 2자리 표시)}


# 114 : 사용자로부터 세 개의 숫자를 입력 받은 후 가장 큰 숫자를 출력하라.

num1 = int(input('input number1: '))
num2 = int(input('input number2: '))
num3 = int(input('input number3: '))

print(max(num1, num2, num3))


# 115 : 휴대폰 번호 앞자리에 따라 통신사는 아래와 같이 구분된다.
#       사용자로부터 휴대전화 번호를 입력 받고, 통신사를 출력하는 프로그램을 작성하라.

phone = input('휴대전화 번호 입력: ')

if phone[:3] == '011':
    print('당신은 SKT 사용자 입니다.')

tels = {'011': 'SKT', '016': 'KT', '019': 'LGU', '010': '알수없음'}

if phone[:3] == list(tels.keys())[0]:
    print('당신은 {0} 사용자 입니다.'.format(tels.get(list(tels.keys())[0])))
elif phone[:3] == list(tels.keys())[1]:
    print('당신은 {0} 사용자 입니다.'.format(tels.get(list(tels.keys())[1])))
elif phone[:3] == list(tels.keys())[2]:
    print('당신은 {0} 사용자 입니다.'.format(tels.get(list(tels.keys())[2])))
else:
    print('당신은 {0}는 사용자 입니다.'.format(tels.get(list(tels.keys())[3])))


# 116 : 우편번호는 5자리로 구성되는데, 앞의 세자리는 구를 나타낸다.
#       예를들어, 강북구의 경우 010, 011, 012 세 자리로 시작한다.

reg = input('우편번호: ')

if int(reg[2:3]) <= 2:
    print('강북구')
elif 3 <= int(reg[2:3]) <= 5:
    print('도봉구')
else:
    print('노원구')


# 117 : 주민등록번호 뒷 자리 7자리 중 첫째 자리는 성별을 나타내는데, 1, 3은 남자 2, 4는 여자를 의미한다.
#       사용자로부터 13자리의 주민등록번호를 입력 받은 후 성별 (남자, 여자)를 출력하는 프로그램을 작성하라.

iden = input('주민등록번호:')

if int(iden[7:8]) == 1:
    print('성별: 남자')
else:
    print('성별: 여자')

# 118 : 주민등록번호의 뒷 자리 7자리 중 두번째와 세번째는 지역코드를 의미한다.
#       주민 등록 번호를 입력 받은 후 출생지가 서울인지 아닌지 판단하는 코드를 작성하라

iden = input('주민등록번호:')

if '09' or '10' or '11' or '12' in int(iden[8:10]):
    print('서울이 아닙니다.')
else:
    print('서울입니다.')


# 119 : 주민등록번호는 13자리로 구성되는데 마지막 자리수는 주민등록번호의 유효성을 체크하는데 사용된다.
#       먼저 앞에서부터 12자리의 숫자에 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5를 차례로 곱한 뒤
#       그 값을 전부 더한다.
#       연산 결과 값을 11로 나누면 나머지가 나오는데 11에서 나머지를 뺀 값이
#       주민등록번호의 마지막 번호가 된다.

v = list(''.join(iden.split('-'))[:-1])
v

mul_value = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]

list(map(lambda x, y: x*y, v, mul_value))

11 - sum(storage)%11

