## 함수 인자 기본값(default) 설정
#default란? 입력 인자값이 없는 경우에 기본적으로 적용되어지는 값을 의미함

# 형식)
# def 함수이름(param1,param2=1):
#       함수정의문1
#       함수정의문2

# 이렇게 정의된 함수가 있는 경우, param2는 기본값으로 '1'을 가지고 있는 것임.
# 즉, 인자값으로 param2에 전달되지 않아도 기본값으로 '1'을 가진다.

#예제4] 함수 인자의 기본값 설정(인자1)
def pr4(par1=10):
    print(par1)
#메인
pr4(10)
pr4(20)
pr4(3)
pr4() 

# 인자를 2개 가진 경우(모두 default인 경우)
def pr5(par1=10,par2=20):
    print(par1,par2)
#메인
pr5(100,200)        #100 200
pr5(100)            #100 20
pr5(200)            #200 20
pr5(par2=200)       #10 200
pr5()               #10 20

# 인자가 2개 이상, 기본값 1인 경우
def pr6(par1,par2=20):
    print(par1,par2)
    
pr6(100,200)        #100 200
pr6(100)            #100 20
pr6(200)            #200 20
#pr6()               #TypeError: 인자는 반드시 전달되어야 한다.

#인자의 기본값이 맨 앞에 있는 경우...
#def pr7(par1=10, par2):     #SyntaxError : 기본값 뒤에는 일반인자 존재 x
#    print(par1,par2)

#[Quiz]
# 1. 짝, 홀수를 구분하는 함수를 작성해 주세요.
# 함수
def odd(num):
    if num%2==0:
        print('짝수 입니다.')
    else:
        print('홀수 입니다.')
#메인
num=int(input('숫자 입력 : '))
odd(num)
# 2. '3'의 배수를 판별하는 함수를 작성해 주세요.
def multi(n):
    if n%3==0:
        return True
    else:
        return False
n=int(input('2. 정수 입력 : '))
if multi(n):
    print('3의 배수입니다.')
else:
    print('3의 배수가 아닙니다.')
# 3. 계산기를 입력,출력, 연산 기능으로 나눠서 실행되게 작성해주세요.
#   입력=>계산처리=>출력
def cal(n1,giho,n2):
    if giho=='+':
        return n1+n2
    elif giho=='-':
        return n1-n2
    elif giho=='*':
        return n1*n2
    elif giho=='/':
        return n1/n2
def Output(n1,n2,giho,result):
    print(f'{n1}{giho}{n2}={result}')
def Input():
    n1=int(input('숫자 1번 : '))
    giho=input('기호 입력 : ')
    n2=int(input('숫자 2번 : '))
    result=cal(n1,giho,n2)
    Output(n1,n2,giho,result)
Input()
# 4. 거꾸로 수를 반환하는 함수 계산, 출력 기능으로 나눠서 작성
#   ex) 123=>321
def rever(num):
    tmp,su=0,0
    while True:
        tmp=num%10
        num=num//10
        su=(su+tmp)*10
        if not num:
            return su//10
def display():
    a=int(input('3자리수 이상입력 : '))
    rs=rever(a)
    print(f'변환전 : {a}, 변환 후 {rs}')
display()
# 5. 친구이름 관리를 함수로 기능을 나눠서 작성해주세요.
    # (1. 친구 목록보기,
    #  2. 친구 추가,
    #  3. 친구 삭제,
    #  4. 친구 수정,
    #  0. 종료)
def fr_list(list):
    if list!=[]:
        print(list)
    else:
        print('등록친구 없음')
def fr_add(list):
    list.append(input('추가할 친구 이름 : '))
def fr_change(list):
    name=input('수정할 이름 : ')
    if name in list:
        idx=list.index(name)
    else:
        print('친구가 없습니다.')
        return
    new=input('새 이름을 입력하세요 : ')
    list[idx]=new
def fr_del(list):
    name=input('삭제할 이름 입력하세요 : ')
    if name in list:
        list.remove(name)
    else:
        print('이름이 존재하지 않습니다.')
def manage():
    a='''
    (1. 친구 목록보기,
     2. 친구 추가,
     3. 친구 삭제,
     4. 친구 수정,
     0. 종료)
    '''
    list=[]
    while True:
        num=int(input('번호 입력 : '))
        if num==1:
            fr_list(list)
        elif num==2:
            fr_add(list)
        elif num==3:
            fr_del(list)
        elif num==4:
            fr_change(list)
        elif num==0:
            print('프로그램종료')
            break
        else:
            print('메뉴선택이 잘못되었습니다.')
manage()
# 문제) 알바 시급 프로그램 작성 (default 인자값 사용)
# 시급 : 8500원, 하루 8시간, 한달 30일 (기본값)
# 다음과 같이 출력되게 만드세요
# (출력 결과)
# <<시급계산프로그램>>
# 1. 기본급
# 2. 일한 날짜 입력
# 번호 입력 >>
def alba(day=30):
    time=8
    price=8500
    re=time*price*day
    return re
def display2():
    num=int(input('''<<시급계산프로그램>>
1. 기본급
2. 일한 날짜 입력
번호 입력 >> '''))
    while True:
        if num==1:
            result=alba()
        elif num==2:
            day=int(input('일한날짜 입력 : '))
            result=alba(day)
        elif num==0:
            break
        return print('월급 : ',result)
display2()
