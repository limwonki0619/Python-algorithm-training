# Unit 13. if 조건문으로 특정 조건일 때 코드 실행하기

# 13.1 if 조건문 사용하기 ------------------------------------------
# if 조건식:
#      코드(Indentation 중요)

x = 10
if x == 10:
    print("10입니다.")

# 13.1.3 if 조건문에서 코드를 생략하기
x = 10
if x == 10:
    pass  # TODO: x가 10일 때 처리가 필요함
# 파이썬에서는 if 다음 줄에 아무 코드도 넣지 않으면 에러가 발생하므로
# if 조건문의 형태를 유지하기 위해 pass를 사용합니다.
# 참고 : TODO는 해야 할 일 이라는 뜻으로 보통 주석에 넣는다.
# TODO, FIXME, BUG, NOTE 등 일관된 주석을 사용한다.

# 13.2 if 조건문과 들여쓰기 -----------------------------------------

x = 10

if x == 10:
    print('x에 들어있는 숫자는')
    print('10입니다.')  # 파이썬에서 들여쓰기는 공백4칸을 권장함.

# 13.3 중첩 if 조건문 사용하기 *** ----------------------------------
x = 15

if x >= 15:
    print('10이상입니다.')

    if x == 15:
        print('15입니다.')

    if x == 20:
        print('20입니다.')

# 13.4 사용자가 입력한 값에 if 조건문 사용하기
x = int(input())

if x == 10:
    print('10입니다.')

if x == 20:
    print('20입니다.')  # if문이 실행되지 않으면 결과도 없음

# 13.6 연습문제 : if 조건문 사용하기
x = 5

if x != 10:
    print('ok')

# 13.7 심사문제 : 온라인 할인 쿠폰 시스템 만들기

# 표준 입력으로 가격(정수)과 쿠폰 이름이 각 줄에 입력됩니다. Cash3000 쿠폰은 3,000원, Cash5000 쿠폰은 5,000원을 할인합니다.
# 쿠폰에 따라 할인된 가격을 출력하는 프로그램을 만드세요
# (input에서 안내 문자열은 출력하지 않아야 합니다).


price = int(input())
coupon = str(input())

if coupon == 'Cash3000':
    print(price - int(coupon[-4:]))

if coupon == 'Cash3000':
    print(price - int(coupon[-4:]))
