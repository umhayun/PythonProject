'''
랜덤함수
: 임의의 값(난수)을 출력하는 함수
난수는 생성된 임의의 값을 의미한다.

랜덤함수를 사용하기 위해서 모듈 사용 :random

모듈 사용 방법 : import [모듈명]
ex) import random   #랜덤 모듈 전체 로딩
or
ex) from [모듈] import [모듈에 있는 내용]
두 방식은 기능 사용방식 차이
1번은 모듈명.사용할값
2번은 사용할값만 사용

'''
# from random import random
# num=int(random()*10)
# num2=int(random()*10)+1
# print(num) # 0~9
# print(num2) # 1~10

#문제1 1~45까지의 임의 값 6개 출력
# for i in range(6):
#     n=int(random()*45)+1
#     print(n)

# 문제1] 1~100까지 랜덤 값을 6개 출력하는 코드 작성
from random import randint
for i in range(6):
    num=randint(1, 101)
    print(num, end=' ')
# 문제2] 1~100까지의 랜덤값 반복 출력 50 출력시 종료
while True:
    num=randint(1, 101)
    if num==50:
        print(f'\n{num}값 출력 종료')
        break
    print(num, end=' ')
# 문제3] 1~15까지 랜덤값 중복 없이 3개 생성 출력
emp=0
num1,num2,num3=0,0,0
while True:
    ran=randint(1, 16)
    if num1!=ran:
        num1=ran
        break
while True:
    ran=randint(1, 16)
    if num1!=ran and num2!=ran:
        num2=ran
        break
while True:
    ran=randint(1, 16)
    if num1!=ran and num2!=ran and num3!=ran:
        num3=ran
        break
print(num1,num2,num3)
  
#문제
#1~99랜덤값 중에 짝수 true,홀수 false
from random import randint
n2=randint(1,99)
print(n2)
if n2%2==0:
    print('True')
else:
    print('False')
    
    
# randrange() : 범위 내에 있는 임의 값 출력
# randrange(5,10,2) : 5~10사이 [5,7,9] 중하나 출력
# 
# #
'''
ASCII코드
미국표준문자 코드로 7bit(0~127)로 하나의 문자를 표현할 수 있음.
ASCII코드는 통신상 기본 문자 코드로 사용되고 있음.

(특징)
1. 프린트 가능한 문자 95자, 나머지 33개문자는 프린트가 불가능한 문자.
    프린트 가능한 문자의 시작 0X20(32)->"공백" 부터 시작 0x7e(126)까지
2. 숫자는 0x30(48)="0"에서부터 0x5A(57)="9"까지 값을 가진 10개의 코드
3. 영문 대문자는 0x41(65)=>"A"에서 0x5A(90)="Z"까지
4. 영문 소문자는 0x61(97)=>"a"에서 0x7A(122)="z"까지
5. ASCII코드는 문자나 숫자(정수)로 표현이 가능함.
숫자를 문자(ASCII)로 변경하는 함수 : chr()
()안에 코드값을 전달하면 그 값을 문자로 출력하는 함수
'''

print(chr(65))      #A
print(chr(0x41))    #A

#문제 5 'A'~'Z'까지의 임의 문자 3자리 출력
from random import randrange
for i in range(3):
    n3=randrange(65, 91)
    print(chr(n3),end=" ")
print() 
    
# random 모듈 내에 choice() 함수
# dice=[1,2,3,4,5,6]
# choice(dice)

import random
dice=[1,2,3,4,5,6]
st='hello world'
x=random.choice(st)
print("dice에서 출력된 값 : ",x)