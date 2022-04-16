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
filter_list=list(filter(even, nums))
print('함수 사용 : ',filter_list)

#lambda사용
filter2_list=list(filter(lambda n:n%2==0, nums))
print('람다 사용 : ',filter2_list)

# MAP : 특정 조건에 맞는 새로운 리스트 생성
# 주어진 리스트, 리스트의 제곱을 한 숫자 새로운 리스트

# map(func,iter1) : 각 멤버를 func으로 동작시킨 후에 새롭게 리스트 생성

nums=[2,4,6]
print(list(map(lambda n : n**2, nums)))

#reduce 함수 : functools 모듈 내에 존재
import functools
a=[1,2,3,5,8]
# 리스트 내에 모든 숫자의 합
print(functools.reduce(lambda x,y:x+y, a))


#문제] lambda로 사칙연산 계산

Sum=lambda x,y:x+y
Sub=lambda x,y:x-y
Mul=lambda x,y:x*y
Div=lambda x,y:x/y
while True:
    x=int(input("첫번째 수 : "))
    y=int(input("두번째 수 : "))
    giho=input('연산기호 : ')
    result=0
    match giho:
        case '+':
            result=Sum(x,y)
        case '-':
            result=Sub(x,y)
        case '*':
            result=Mul(x,y)
        case '/':
            result=Div(x,y)
    print(result)
    a=input('계속 하시겟습니까(o,x)')
    if a=='x':
        break