# 041 ~ 090 파이썬 기본 자료구조


# 041 : 2016년 11월 영화 예매 순위 기준 top3는 다음과 같다. 영화 제목을 movie_rank 이름의 리스트에 저장하라. (순위 정보는 저장하지 않는다.)
movie_rank = list(["닥터 스트레인지", "스플릿", "럭키"])


# 042 : 041의 movie_rank 리스트에 "배트맨"을 추가하라.
movie_rank.append("베트맨")  # 기존 변수에 요소가 (끝에)추가된다.


# 043 : movie_rank 변수에서 "슈퍼맨"을 "닥터 스트레인지"와 "스플릿" 사이에 추가하라.
movie_rank.insert(2, "슈퍼맨")  # 원하는 위치에 추가할 수 있다.


# 044 : movie_rank 리스트에서 '럭키'를 삭제하라
movie_rank.remove("럭키")
del movie_rank[3]  # 다른 방법


# 045 : movie_rank에서 '스플릿'과 '베트맨'을 삭제하라.
movie_rank.remove("스플릿")  # remove 메서드는 하나씩 제거
movie_rank.remove("베트맨")

del movie_rank[2:]  # del + slice로 한번에 지우기


# 046 : lang1과 lang2 리스트가 있을 때 lang1과 lang2의 원소를 모두 갖고 있는 langs 리스트를 만들어라.
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
langs = lang1 + lang2
print(langs)


# 047 : 다음 리스트에서 최댓값과 최솟값을 출력하라.
nums = [1, 2, 3, 4, 5, 6, 7]
print(max(nums), min(nums))


# 048 : 다음 리스트의 합을 출력하라.
nums = [1, 2, 3, 4, 5]
print(sum(nums))


# 049 : 다음 리스트에 저장된 데이터의 개수를 화면에 구하하라.
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]
len(cook)


# 050 : 다음 리스트의 평균을 출력하라.
nums = [1, 2, 3, 4, 5]
print(sum(nums)/len(nums))


# 051 : price 변수에는 날짜와 종가 정보가 저장돼 있다. 날짜 정보를 제외하고 가격 정보만을 출력하라.
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])


# 052 : 슬라이싱을 사용해서 홀수만 출력하라.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])


# 053 : 슬라이싱을 사용해서 짝수만 출력하라.
print(nums[1::2])


# 054 : 슬라이싱을 사용해서 리스트의 숫자를 역 방향으로 출력하라.
nums = [1, 2, 3, 4, 5]
print(nums[::-1])


# 055 : interest 리스트에는 아래의 데이터가 바인딩되어 있다.
#       interest 리스트를 사용하여 아래와 같이 화면에 출력하라.
#       출력 예 : 삼성전자 Naver (리스트 형태 X)

interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[0], interest[2])

# 056 : interest 리스트에는 아래의 데이터가 바인딩되어 있다.
#       interest 리스트를 사용하여 아래와 같이 화면에 출력하라.
#       출력 예 : 삼성전자 LG전자 Naver SK하이닉스 미래에셋대우 (리스트형태 X)

interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(' '.join(interest))


# 057 : 위의 interest 리스트에서 다음과 같이 출력하라
#       삼성전자/LG전자/Naver/SK하이닉스/미래에셋대우

print('/'.join(interest))


# 058 : 위의 interest 리스트를 join() 메서드를 통해 세로로 출력하라
print('\n'.join(interest))


# 059 : 회사 이름이 '/'로 구분되어 하나의 문자열로 저장되어 있다.
#       이를 interest 이름의 리스트로 분리 저장하라.

string = "삼성전자/LG전자/Naver"
interest = string.split("/")


# 060 : 059 심화
string2 = "삼성전자/LG전자/Naver/SK하이닉스/미래에셋대우"
interest2 = string.split("/")


# 061 : 다음 코드의 결괏값에 대해 예측하여라.
interest_0 = ['삼성전자', 'LG전자', 'SK Hynix']
interest_1 = interest_0
interest_1[0] = 'Naver'
print(interest_0)

# interest_1의 첫번쨰 값이 Naver로 변경됨. 리스트를 각기 다른 객체로 분리하고 싶다면,
# copy 메서드를 사용해야 한다.

# 설명 : interest_1 에 interest_0 리스트 전체를 대입하면,
# 리스트가 복사되는 것이 아니라, 새로운 이름이 하나더 추가됩니다.
# 즉, interest_0과 interest_1은 동일한 리스트를 가리키고 있게 됩니다.


# 062 : 다음 코드의 결과값에 대해 예측하여라.
interest_0 = ['삼성전자', 'LG전자', 'SK Hynix']
interest_1 = interest_0[:]  # copy 메서드와 함께 인덱싱으로 변수를 할당하면 다른 객체에 할당된다.
interest_1[0] = 'Naver'
print(interest_0)

# 리스트의 슬라이싱은 리스트를 복사 생성합니다. interest_0과 interest_1은 별도의 공간에 각각의 값이 저장되어 있습니다.
# 따라서, interest_1의 값을 수정해도 interest_0의 값이 변경되지 않습니다.


# 063 : my_variable 이름의 비어있는 튜플을 만들라.
my_varialbe = ()
print(type(my_varialbe))


# 064 : 다음 코드를 실행해보고 오류가 발생하는 원인을 설명하라.
t = (1, 2, 3)
# t[0] = 'a'   # tuple은 값을 변경할 수 없다.


# 065 : 숫자 1이 저장된 튜플을 생성하라.
tuple_1 = (1,)
print(tuple, type(tuple_1))


# 066 : 아래와 같이 t2에는 1, 2, 3, 4 데이터가 바인딩되어 있다.
#       t가 바인딩하는 데이터 타입은 무엇인가?
t2 = 1, 2, 3, 4  # 튜플
type(t2)


# 067 : 변수 t3에는 아래와 같은 값이 저장되어 있다.
#       변수 t3가 ('A', 'b', 'c') 튜플을 가리키도록 수정 하라.
t3 = ('a', 'b', 'c')
t4 = ('A', 'b', 'c')  # 튜플은 값을 변경할 수 없기 떄문에 새롭게 할당해야 한다.


# 068 : 다음 튜플을 리스트로 변환하라.
interest3 = ('삼성전자', 'LG전자', 'SK Hynix')
interest3 = list(interest3)
print(interest3, type(interest3))


# 069 : 위의 interest3 리스트를 튜플로 변경하라.
interest4 = tuple(interest3)  # 함수이름으로 변수명을 만들지 말자...


# 070 : 아래 코드의 실행 결과를 예측하라
my_tuple = (1, 2, 3)
a, b, c = my_tuple  # 튜플 언패킹으로 각각의 변수에 각각의 값이 할당된다.
print(a + b + c)    # 따라서 각각의 값을 모두 더하면 6이 출력된다.


# ***
# 071 : 다음과 같이 10개의 값이 저장된 scores 리스트가 있을 때,
#       start expression을 사용하여 좌측 8개의 값을 valid_score 변수에 바인딩하여라.

scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score, _, _ = scores

# 언패킹을 할 때, 다른 변수가 필요없다면, '_'(underscore)로 대체할 수 있다.

# 기본적으로 데이터 언패킹은 좌변의 변수와 우변 데이터 개수가 같아야 합니다.
# 하지만 star expression을 사용하면 변수의 개수가 달라도 데이터 언패킹을 할 수 있습니다.
# 튜플에 저장된 데이터 중에서 앞에 있는 두 개의 데이터만 필요할 경우 나머지 데이터의 언패킹 코드를 작성할 필요가 없습니다.


# 072 : 위의 scores 리스트에서 start expression을 사용하여 우측 8개의 값을 valid_score 변수에 바인딩하여라.
_, _, *vaild_score2 = scores


# 073 : 위의 scores 리스트에서 start expression을 사용하여 가운데 있는 8개의 값을 valid_score 변수에 바인딩하여라.
_, *valid_score3, _ = scores


# 074 : temp 이름의 비어있는 딕셔너리를 만들라.
temp = {}
print(type(temp))


# 075 : 다음 아이스크림 이름과 희망가격을 딕셔너리로 구성하라.

#       이름  희망가격
#       메로나  1000
#       폴라포  1200
#       빵빠레  1800

ice = dict(zip(['메로나', '폴라포', '빵빠레'], [1000, 1200, 1800]))
print(ice)


# 076 : 075 번의 딕셔너리에 아래 아이스크림 가격정보를 추가하라.
ice.update({'죠스바':1200, '월드콘':1500})  # 입력순대로 딕셔너리에 추가할 수 있다.
print(ice)


# 077 : 위의 딕셔너리에서 메로나 가격을 출력하라.
print(ice.get('메로나'))  # get 메서드는 해당하는 키의 값을 출력


# 078 : 위의 딕셔너리에서 메로나의 가격을 1300원으로 수정하라.
ice.update({'메로나':1300})
print(ice)


# 079 : 위의 딕셔너리에서 메로나를 삭제하라.
ice.pop('메로나')  # 딕셔너리의 키와 값을 삭제하는 방법 1
del ice['메로나']  # 방법 2

print(ice)


# 080 : 다음 코드에서 에러가 발생한 원인을 설명하라.
icecream = {'폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# icecream['누가바']

# 딕셔너리에 없는 키를 호출해서 에러가 발생함


# 081 : 아래의 표에서, 아이스크림 이름을 키값으로, (가격, 재고) 리스트를 딕셔너리의 값으로 저장하라.
# 딕셔너리의 이름은 inventory로 한다

inventory = dict({'메로나':[300, 20], '비비빅':[400, 3], '죠스바':[250, 100]})
inventory2 = dict(zip(['메로나', '비비빅', '죠스바'], [[300, 20], [400, 3], [250, 100]]))


# 082 : 위의 딕셔너리에서 메로나의 가격을 화면에 출력하라.
print(inventory.get('메로나')[0],'원')


# 083 : 위의 딕셔너리에서 메로나의 재고를 화면에 출력하라.
print(inventory.get('메로나')[1],'개')


# 084 : 위의 딕셔너리에 아래 데이터를 추가하라.
#       월드콘 500 7
inventory.update({'월드콘':[500, 7]})  # 업데이트시 {}나 [] 잊지말기
print(inventory)

# 085 : 다음의 딕셔너리에서 key값으로만 구성된 리스트를 생성하라.
icecream2 = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}

print(list(icecream2.keys()))  # dict_keys 타입은 list() 함수를 사용해서 리스트로 변경할 수 있다.


# 086 : 위의 딕셔너리에서 values 값으로만 구성된 리스트를 생성하라.
print(list(icecream2.values()))


# 087 : 위의 딕셔너리에서 아이스크림 판매 금액의 총합을 출력하라.
print(sum(icecream2.values()), '원')


# 088 : 아래의 new_product 딕셔너리를 087번의 icecream 딕셔너리에 추가하라.
new_product = {'팥빙수':2700, '아맛나':1000}

icecream2.update(new_product)
print(icecream2)


# 089 : 아래 두 개의 튜플을 하나의 딕셔너리로 변환하라.
#       keys를 키로, vals를 값으로 result 이름의 딕셔너리로 저장한다.

keys = ('apple', 'pear', 'peach')
vals = (300, 250, 400)

result = dict(zip(keys, vals))
print(result)


# 090 : date와 close_price 두 개의 리스트를 close_table 이름의 딕셔너리로 생성하라.
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]

close_table = dict(zip(date, close_price))
print(close_table)

