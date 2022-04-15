# match~case 구문 : 파이썬 3.10.0 이후에 도입...
# 다른 언어의 switch~case구문과 같은 동작
# 예제1
'''
def num_chk(st):
    match st:
        case 1 :
            return '일'
        case 2 :
            return '이'
        case 3 : 
            return '삼'
        case _ :
            return '선택범위를 벗어났습니다.'

st=1
wh=num_chk(st)
print(wh)     
'''
#예제
'''
def alpha_chk2(chk):
    match chk:
        case 'a'|'A':
            return 'A'
        case 'b'|'B':
            return 'B'
        case 'c'|'C':
            return 'C'
        case _:
            return 'A~C이외의 알파벳'

alpha=input('A~C사이 알파벳 입력 : ')
print('입력한 알파벳은 :',alpha_chk2(alpha))
'''
# 연습 : 국가명을 입력받아 해당 국가 번호를 출력 함수 구현
# 01 -unitedstate 33-france, 34-spain, 81-japan,82-korea
#코드가 없는 경우에는 -1을 반환값으로 하는 getPhoneCode() 구현

#(ex) getPhoneCode('southkorea')->82(대소문자 구분x)
#math~case문 사용
'''
def getPhoneCode(country):
    match country:
        case 'unitedstate':
            return 1
        case 'france':
            return 33
        case 'spain':
            return 34
        case 'japan':
            return 81
        case 'southkorea':
            return 82
        case _:
            return -1

coun=input('나라이름 영어로 입력 : ')
country=coun.lower()
num=getPhoneCode(country)
print(country,'의 국가 번호는 ',num,'입니다.')
'''

# lambda 함수
# 익명 함수로 일시적으로 사용하는 함수 의미
# 사용은 함수가 생성된 곳에서 필요한 경우, 사용한후 버리는 함수
# (형식)
# lambda 인자리스트 : 표현식
# 예) lam=lambda x: x**2
#     print(lam(8))   =>출력결과 :64#
#       lam2=lambda x,y:x+y
#       print(lam2(2,5))=>출력결과 : 7
# 람다는 어디서든지 사용할 수 있는 임시 함수
lam=lambda x : x**2
print(lam(8))
lam2=lambda x,y: x+y
print(lam2(2,5))

#예제1) 다음과 같은 함수를 lambda로 표현

#함수
def swap(a,b):
    return b,a
a=100
b=200
print('swap전 : ',a,b)
a,b=swap(a,b)
print('swap후 : ',a,b)

lam3=lambda x,y: [y,x]
a=100
b=200
print('swap전 : ',a,b)
a,b=lam3(a,b)
print('swap후 : ',a,b)

#예제2
lam=lambda a: a*10
lam2=lambda a,b:a+b
noData=lambda : print("인자가 없는 lambda")
print(lam(10))
print(lam2(10,20))
noData()

#예제3]
def str_len(s):
    return len(s) 
print(str_len('goods'))
string=['bob','charles','alexander3','teddy']
#알파벳 순서로 정렬 =>string.sort(key='str_len') ->문자열의 길이를 기준
#string.sort(key=lambda s: len(s))
string.sort(key=str_len)
print(string)
string=['bob','charles','alexander3','teddy']
print(string)
string.sort(key=lambda s: len(s))
print(string)

# lamda가 유용하게 사용되는 3가지 대표적 함수
# filter : 특정 조건을 만족하는 요소만 남기고 필터링
# map: 각 원소를 주어진 수식에 따라 변경하여 새로운 리스트를 반환
# reduce : 차례대로 앞 2개의 원소를 가지고 연산, 연산결과가 또 다음 연산의 입력으로 
#       진행됨. 따라서 마지막까지 진행되며 최종 출력은 한개의 값만 남게됨

# filter(함수, 리스트)
# filter(function, iterable) -> 틀정 조건에 요소만 남기고 필터링
#                  리스트에 있는 내용을 함수에 대입하여 결과값 처리(True or False)

# 함수 - 짝수만 반환하는 함수 
def even(n):
    return n%2==0

print(even(3))      #False반환

nums =list(range(1,11))
print(nums)