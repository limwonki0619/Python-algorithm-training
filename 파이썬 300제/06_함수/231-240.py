# 231 : "비트코인" 문자열을 화면에 출력하는 print_coin() 함수를 정의하라.

def print_coin():
    print('bitcoin')

# 232 : 231번에서 정의한 함수를 호출하라.
print_coin()


# 233 : 231번에서 정의한 함수를 100번호출하라.
for i in range(100):
    print_coin()

# 234 : "비트코인" 문자열을 100번 화면에 출력하는 print_coins() 함수를 정의하라.
#        한 라인에 하나씩 "보트코인" 문자열을 출력한다.

def print_coin():
    for i in range(100):
        print('bitcoin')

print_coin()


# 235 : 아래의 에러가 발생하는 이유에 대해 설명하라.

hello()  # 함수생성을 먼저한 후 함수를 호출해야한다.
def hello():
    print("Hi")


# 236 : 아래 코드의 실행 결과를 예측하라.
def message() :
    print("A")
    print("B")

message()
print("C")
message()
# 'A', 'B', 'C', 'A, 'B'


# 237 : 아래 코드의 실행 결과를 예측하라. (읽기 어려운 코드의 예입니다.)

print("A")

def message() :
    print("B")

print("C")
message()

# A C B



# 238 : 아래 코드의 실행 결과를 예측하라. (읽기 어려운 코드의 예입니다.)
print("A")
def messages1():
    print("B")
print("C")
def messages2():
    print("D")

messages1()
print("E")
messages2()

# A C B E D


# 239 : 아래 코드의 실행 결과를 예측하라.
def message1():
    print("A")

def message2():
    print("B")
    message1()

message2()

# B A

# 240 : 아래 코드의 실행 결과를 예측하라.

def message1():
    print("A")

def message2():
    print("B")

def message3():
    for i in range(3):
        message2()
        print("C")
    message1()

message3()

# B C B C B C A

