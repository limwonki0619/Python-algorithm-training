# 121 : 아래 for 문에서 print 문은 몇 번 호출 되는가?

for var in ["가", "나", "다", "라"]:
     print(var)  # 4번


# 122 : 아래 코드의 실행 결과를 예측하라.

for var in ["사과", "귤", "수박"]:
    print(var)  # 사과, 귤, 수박

# 123 : 아래 코드의 실행 결과를 예측하라.

for var in ["사과", "귤", "수박"]:
    print(var)             # 사과 -- 귤 -- 수박 --
    print("--")

# 124 : 아래 코드의 실행 결과를 예측하라.

for var in ["사과", "귤", "수박"]:
    print(var)  # 사과 귤 수박 --
print("--")

# 125 : menu 리스트에는 판매중인 메뉴가 저장돼 있다.
#       아래와 같이 화면에 출력하라.

menu = ["김밥", "라면", "튀김"]
for var in menu:
    print('오늘의 메뉴:')

# 126 : portfolio에는 보유중인 주식 목록이 저장돼 있다. 아래와 같이 화면에 출력하라.

portfolio = ["SK하이닉스", "삼성전자", "LG전자"]
for por in portfolio:
    print(por, '보유중')

# 127 : 다음과 같이 애완 동물 리스트가 있을 때 애완 동물의 이름과 애완 동물의 글자수를 출력하라.
pets = ['dog', 'cat', 'parrot', 'squirrel', 'goldfish']

for pet in pets:
    print(pet ,len(pet))

# 128 : 다음과 같이 판매가가 저장된 리스트가 있을 때 부가세가 포함된 가격을 화면에 출력하라.
#       단 부가세는 10원으로 가정한다.

prices = [100, 200, 300]

for pv in prices:
    print(int(pv + (pv / 10)))


# 129 : prices 리스트에는 가격정보가 문자열로 저장돼 있다.
#       prices 리스트에 저장된 모든 데이터를 파이썬 숫자 형으로 변환 후 화면에 출력하라.

prices = ["129,300", "1,000", "2,300"]

for price in prices:
    print(int(price.replace(',','')))

# 130 : menu 리스트에는 음식이름이 뒤집혀 저장돼 있다.
#       이를 읽기 좋게 뒤집어서 아래와 같이 출력하라.

menus = ["면라", "밥김", "김튀"]

for menu in menus:
    print(menu[::-1])


# 131 : my_list에는 네 개의 데이터가 저장되어 있다.
#       첫 번째 데이터를 제외하고 나머지 데이터를 한 라인에 하나씩 출력하라.

my_list = ["가", "나", "다", "라"]

for list in my_list[1:]:
    print(list)

for list in my_list:
    if list == '가':
        continue
    else:
        print(list)


# 132 : my_list의 데이터 중에서 홀수 번째 위치의 값을 화면에 출력하라.

my_list = [1, 2, 3, 4, 5, 6]

for odd in my_list[::2]:
    print(odd)


# 133 : my_list의 데이터 중에서 짝수 번째 위치의 값만을 화면에 출력하라.

my_list = [1, 2, 3, 4, 5, 6]

for even in my_list[1::2]:
    print(even)


# 134 : my_list의 데이터를 아래와 같이 역방향으로 출력하라.

my_list = ["가", "나", "다", "라"]

for reverse in my_list[::-1]:
    print(reverse)


# 135 : my_list에서 음수를 출력하라

my_list = [3, -20, -3, 44]

for nag in my_list:
    if nag < 0:
        print(nag)

# 136 : my_list에서 3의 배수를 출력하라.

my_list = [3, 100, 23, 44]

for multiple in my_list:
    if multiple % 3 == 0:
        print(multiple)

# 137 : my_list에서 세 글자 이상의 문자를 화면에 출력하라

my_list = ["I", "study", "python", "language", "!"]

for text in my_list:
    if len(text) >= 3:
        print(text)

# 138 : my_list에서 5보다 크고 10보다 작은 수를 화면에 출력하라

my_list = [3, 1, 7, 10, 5, 6]

for num in my_list:
    if 5 < num < 10:
        print(num)

# 139 : my_list에서 10보다 크고 20 보다 작으면서 3의 배수일 경우 화면에 출력하라

my_list = [13, 21, 12, 14, 30, 18]

for num2 in my_list:
    if 10 < num2 < 20 and num2 % 3 == 0:
        print(num2)

# 140 : my_list에서 3의 배수이거나 4의 배수를 화면에 출력하라

my_list = [3, 1, 7, 12, 5, 16]

for num3 in my_list:
    if num3 % 3 == 0 or num3 % 4 == 0:
        print(num3)

# 141 : my_list 에서 대문자만 화면에 출력하라.

my_list = ["A", "b", "c", "D"]

for upper in my_list:
    if upper.isupper() == True:  # 1 : True
        print(upper)

# 142 : my_list 에서 소문자만 화면에 출력하라.

for lower in my_list:
    if lower.islower() == True:  # bool(1) : True
        print(lower)


# 143 : 문자열의 upper() 메서드는 문자열을 대문자로 변경하고, lower() 메서드는 소문자로 변환한다.
#       리스트의 문자를 대문자는 소문자로, 소문자는 대문자로 변환하라.

my_list = ["A", "b", "c", "D"]

for text in my_list:
    if text.islower() == True:
        print(text.upper(), end='')
    else:
        print(text.lower(), end='')

# 144 : 파일 이름이 저장된 리스트에서 확장자를 제거하고 파일 이름만 화면에 출력하라. (힌트: split 메서드를 사용)

file_list = ['hello.py', 'ex01.py', 'ch02.py', 'intro.hwp']

for file in file_list:
    extension = file.split('.')[0]
    print(extension)


# 145 : 파일 이름이 리스트에 저장되어 있을 때 확장자가 *.h인 파일을 출력하라.

filenames = ['intra.h', 'intra.c', 'define.h', 'run.py']

for file in filenames:
    if '.h' in file:
        print(file)

# 모범답안
for file in filenames :
    if file.split('.')[1] == "h" :
        print(file)

# 146 : 파일 이름이 리스트에 저장되어 있을 때 확장자가 .h나 .c인 파일을 화면에 출력하라.

filenames = ['intra.h', 'intra.c', 'define.h', 'run.py']

for file in filenames :
    extension = file.split('.')[1]
    if extension == "h" or extension == "c" :
        print(file)

# 모범답안
# endswith 메서드에 튜플로 여러개의 확장자를 전달할 수 있습니다.

for file in filenames :
    if file.endswith(("h", "c")) :
        print(file)

# 147 : my_list에서 양수만 new_list 이름의 리스트에 저장하라.

my_list = [3, -20, -3, 44]

new_list = []
for num4 in my_list:
    if num4 > 0:
        new_list.append(num4)

print(new_list)


# 148 : my_list 에서 대문자만을 upper_list에 저장하라.

my_list = ["A", "b", "c", "D"]

new_list = []
for upper in my_list:
    if upper.isupper() == True:
        new_list.append(upper)
print(new_list)


# 149 : my_list의 값을 sole_list에 저장하라. 단, 중복된 값은 제거한다.

my_list = [3, 4, 4, 5, 6, 6]

sole_list = []
for num5 in my_list :
    if num5 not in sole_list:
        sole_list.append(num5)

print(sole_list)


# 150 : 내장 함수를 사용하지 않고 반복문을 사용해서 my_list에 저장된 모든 수의 합를 출력하라
my_list = [3, 4, 5]

accumulate = 0
for i in my_list:
    accumulate += i

print(accumulate)