## 변수의 범위
# 변수를 특정지역에서만 사용되는 지역변수(블럭내 사용)와
# 지역에 상관없이 전 영역에서 사용되는 전역변수로 분류. (변수의 스코프-범위)
# 특정영역(블럭)은 함수 또는 블럭(if,for,while 등) 등을 의미함.
# 전역변수 - global, 지역변수 - local
# 
# 
# 

#예제1, 전역변수의 영역: 블럭에서만 동작해요
#global 변수, 전역 변수
var2=2
#함수 정의
def func(arg):
    var1=1
    print(var1,var2,arg)
    
#메인
func(var2)
#print(var1) #함수 func 블럭 내에 선언된 변수 - 함수가 종료되면서 사라짐.

#예제2, 블록에서 전역변수 사용
#global 변수, 전역 변수
var2=2
#함수 정의
def func(arg):
    global var2 #전역변수 var2
    var2=10      #w전역변수 var2=10
    print(var2,arg+2)
    
#메인
print(var2)
func(var2)
#func()함수 실행후 var2변경
print(var2)

#함수 또는 블럭에서 변수명으로 데이터 접금시 우선순위 : 가까운 local->global
#예제3
#예제1
#global 변수, 전역 변수
var2=2
#함수 정의
def func(arg):
    global var2 #전역변수 var2
    var2=10      #w전역변수 var2=10
    var1=1
    print(var2,arg)
    def func2(var2):
        var2=1
        print("func2:",var2,arg,var1)
    func2(var2)
    
#메인
func(var2)
print(var2)
print("="*20)
## 중첩 함수
# 중첩함수란, 함수 내부에 또 다른 함수가 내장된 형태.
# 내부 함수를 포함함 함수를 외부함수라고 표현한다.
##
# (형식)
# def 외부함수(인수) :
#       함수정의문1
#       def 내부함수(인수):
#           함수정의문(내부)1
#           return 값
#       return 내부함수
# 파이썬의 중첩함수는 외부함수나 내부함수를 변수에 저장할 수 있다.
# 이런 특성을 가지는 함수를 일급함수(First class Function)이라고 한다.
# 특히, 내부 함수는 외부함수의 return 명령문을 이용하여 반환하는 형태의 함수를
# 클리저(Function clour)라고 한다.
# 특징은 외부함수가 종료되어도 내부함수에서 선언된 변수가 
# 메모리에서 소멸하지 않는 상태로 내부함수를 사용할 수 있다. 
# #

def a():
    print('a함수')
    def b():
        print('b함수')
    return b

b=a()   #외부함수 호출 : a함수
b()     #내부함수 호출 : b함수


###
data=list(range(1,101))
def outer_func(data):
    dataSet=data #data로 받은 값을 dataSEt
    #inner
    def tot():
        tot_val=sum(dataSet)
        return tot_val
    def avg(tot_val):
        avg_val=tot_val/len(dataSet)
        return avg_val
    return tot,avg #inner반환

#메인
#외부함수 호출 : data생성
tot,avg=outer_func(data)    #tot,avg=tot,avg(outer_func()의 return값)
#내부함수 호출
tot_val=tot()   #outer_func내에 있는 tot()함수
print("tot=",tot_val)
avg_val=avg(tot_val)
print("avg=",avg_val)

##역할
# 외부함수 : 함수에서 사용할 자료를 만들고, 내부함수를 포함하는 역할
# 내부함수 : 외부함수에서 만든 자료를 연산하고 작업하는 역할 담당
# 
# #

'''
#[Quiz]
디폴트 매개변수를 이용한 요금 구하는 프로그램 만들기.
기본 요금은 500원 환승이 없거나 환승 1회까지는 기본요금.
1회를 초과하는 환승의 경우 환승 1회마다 요금 2배씩 증가
ex)환승 2회인 경우 :1000원, 환승 3회인 경우 : 2000원
장거리는 10000원
1.환승안함
2.환승함    
3.장거리
<<*함수화 하여 작업하세요>> -->요금 계산하는 함수, 화면에 표시하는 함수
함수 처리시 목적지에 대한 내용도 입력받아서 처리하세요!!
'''
#함수정의 : 혼자풀기
# def bus(c1):
#     fee_val=500
#     def fee(choice):
#         if choice<=5:
#             for i in range(1,choice):
#                 fee_val=fee_val*2 
#         elif choice>5:
#             fee_val=10000       
#         return fee_val   
#     def prn(fee_val):
#         print("요금 : ",fee_val)
#     return fee,prn


# #메인
# while True:
#     print("1. 환승안함 \n2. 환승함 \n3. 장거리 ")
#     choice=int(input("환승 횟수 : "))
#     fee,prn=bus()
#     fee_val=fee(choice)
#     prn(fee_val)
    
#     sel=input("계속 하시겠습니까? (y/n) : ")
#     if sel=='n':
#         break

# 함수 정의 : 선생님풀이
def transfer(dest,su=1,won=500):
    for i in range(1,su):
        won*=2
        if won>=10000:
            won=10000
    return "{}까지 요금 : {:,}원 입니다.".format(dest,won)

def display():
    dest=""
    su=0
    num=int(input('1. 환승안함 \n2. 환승함 \n3. 장거리 '))
    dest=input('목적지 입력: ')
    if num==1:
        result=transfer(dest)
    elif num==2:
        su=int(input('환승 횟수 : '))
        result=transfer(dest,su)
    elif num==3:
        result=transfer(dest,1,10000)
    else:
        print('메뉴선택 잘못되었습니다.')
        return
    print(result)

display()

        