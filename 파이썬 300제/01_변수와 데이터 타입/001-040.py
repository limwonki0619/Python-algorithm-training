# 001 : 화면에 Hello World 문자열을 출력하라.
print('hello World')

# 002 : 화면에 Mary's cosmetics을 출력하라. (중간에 '가 있음에 주의.)
print("Mary's cosmetics")

# 003 : 화면에 아래 문장을 출력하라. (중간에 "가 있음에 주의.)
print("""신씨가 소리질렀다. "도둑이야".""")

# 004 : 화면에 "C:\Windows"를 출력하라.
print("""C:\\Windows""")

# 005 : 다음 코드를 실행해보고 \t와 \n의 역할을 설명하라.
print("안녕하세요. \n만나서\t\t반갑습니다.")  # \n : 줄바꿈 \t : tab

# 006 : print 함수에 두 개의 단어를 입력한 예제이다. 아래 코드의 출력 결과를 예상하라.
print ("오늘은", "일요일")
# 오늘은 일요일

# 007 : print() 함수를 사용하여 다음과 같이 출력하라.
# naver;kakao;sk;samsung
print('naver', 'kakao', 'sk', 'samsung', sep=";")

# 008 : print() 함수를 사용하여 다음과 같이 출력하라.
# naver/kakao/sk/samsung
print('naver', 'kakao', 'sk', 'samsung', sep="/")

# 009 : 다음 코드를 수정하여 줄바꿈이 없이 출력되도록 하라.
# print("first");print("second")
print("first", end='');print("second", end='')

# 010 : string 문자열의 길이를 구하여라.
string = "dk2jd923i1jdk2jd93jfd92jd918943jfd8923"
len(string)


# 011 : 다음 코드의 실행결과를 예상하라.
a = "3"
b = "4"
print(a + b)
# 34


# 012 : 변수 s와 t에는 각각 문자열이 바인딩 되어있다.
s = "hello"
t = "python"

# 두 변수를 이용하여 아래와 같이 출력하라.
# 실행 예:
# hello! python
print(s+'!', t)


# 013 : 아래 코드의 실행 결과를 예상하라.
print("Hi" * 3)
# HiHiHi


# 014 : 화면에 '-'를 80개 출력하라.
print('-'*80)


# 015 : 변수에 다음과 같은 문자열이 바인딩되어 있다.
t1 = 'python'
t2 = 'java'

# 변수에 문자열 더하기와 문자열 곱하기를 사용해서 아래와 같이 출력하여라.
# 실행 예:
# python java python java python java python java

print((t1 +' '+ t2+' ') * 4)


# 016 : LG전자 주식을 10주 보유하고 있습니다.
# 금일 종가 20,000원일 경우 총 평가 금액을 화면에 출력하라.

print('{0:<6,}'.format(20000*10)+'원')

# 017 : 아래 코드의 실행 결과를 예측하라.
# 2 + 2 * 3
# 8


# 018 : 아래 변수에 바인딩된 값의 타입을 판별하라
a = "132"
type(a)
# str

# 019 : 문자열 '720'을 정수형으로 변환하라.
num_str = '720'
print(int(num_str), type(int(num_str)))

# 020 : 정수 100을 문자열 '100'으로 변환하라.
num = 100
print(str(num), type(str(num)))


# 021 : letters가 바인딩하는 문자열에서 첫번째와 세번째 문자를 출력하라.
lang = 'python'
print(lang[0], lang[2])
print(lang[0:3:2])


