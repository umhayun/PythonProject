##함수(Function)
# : 프로그램에서 사용할 기능을 미리 정의해서 구현한 것
# (또 다른 의미의 프로그램 내의 작은 프로그램)

#python의 함수 정의(생성)
#def 함수 이름([인자 list]):
#    함수 기능 정의1
#    함수 기능 정의2
#    함수 기능 정의3
#    ...

# - 함수 사용에 있어서 설명이 필요한 경우, 함수 내부에 주석으 사용하여 기술(여러줄 주석)
# - 함수를 만들 때에 함수의 기능을 바로 알 수 있는 이름으로 정의 권장
# - 미리 만들어 놓은 함수를 호출 시에는, "함수이름([인자...])"로 호출
# - 정의 생성된 함수의 반환값이 있는 경우, "return" 명령어 사용
# -  함수에 반환값이 있을 수도 있고, 없을 수도 있다. 있는 경우 return사용
#     없는 경우 "return"은 함수 종료
# - 함수에 필요하면 인자값을 전달할 수 있다. 전달된 인자값은 함수 정의시에 만든 
#   "매개변수"에 그 값이 저장된다. 이후에 함수 정의부에서 해당 내용 가지고 구동

#예제1] 사용자가 입력한 값을 출력하는 함수 구현
'''
def pr():
    txt=input("입력값 : ")
    print()
    print("입력한 내용은 : ", txt)
#함수 호출
pr()
'''
# 실습 - 입력값을 받아서 사칙연산하는 프로그램 함수를 사용.
#   그 함수의 이름은 calc()로 구현해 보세요
#   (메인에서 calc()호출하면 모든 동작이 가능하도록 설정)
''' 
def calc():
    while True:
        calc=input("계산식 입력하세요 : ")
        if '+' in calc:
            num1,num2=calc.split('+')
            num1=int(num1)
            num2=int(num2)
            print("계산 결과 : ",num1+num2)
        elif '-' in calc:
            num1,num2=calc.split('-')
            num1=int(num1)
            num2=int(num2)
            print("계산 결과 : ",num1-num2)
        elif '*' in calc:
            num1,num2=calc.split('*')
            num1=int(num1)
            num2=int(num2)
            print("계산 결과 : ",num1*num2)
        elif '/' in calc:
            num1,num2=calc.split('/')
            num1=int(num1)
            num2=int(num2)
            print("계산 결과 : ",num1/num2)
        else:
            print("수식이 잘못되었습니다. 다시 입력해주세요!")
        sel=input("계속 하시겠습니까?")
        if sel=='n':
            break

calc()
'''
# 예제2] 함수의 인자값 사용 - 사용자가 입력한 값을 출력하는 함수 구현
# 사용자로부터 입력받은 값을 인자값으로 처리하는 함수.
'''
# 함수 정의
def pr2(str1):
    print("입력한 내용은 : ",str1)
    
#메인
txt=input("입력 : ")
print()
pr2(txt)
'''
# 실습 - 입력값을 받아서 사칙연산하는 플그램 함수를 사용하여 동작하게 만드세요.
#       함수명음 "calc([문자열인자값])"으로 사용하세요.
'''
def calc(calc):
    if '+' in calc:
        num1,num2=calc.split('+')
        num1=int(num1)
        num2=int(num2)
        print("계산 결과 : ",num1+num2)
    elif '-' in calc:
        num1,num2=calc.split('-')
        num1=int(num1)
        num2=int(num2)
        print("계산 결과 : ",num1-num2)
    elif '*' in calc:
        num1,num2=calc.split('*')
        num1=int(num1)
        num2=int(num2)
        print("계산 결과 : ",num1*num2)
    elif '/' in calc:
        num1,num2=calc.split('/')
        num1=int(num1)
        num2=int(num2)
        print("계산 결과 : ",num1/num2)
    else:
        print("수식입력이 잘못되었습니다\n 다시 입력해주세요!")
    
#메인
while True:
    txt=input("계산식 입력하세요 : ")
    calc(txt)
    sel=input("계속 하시겠습니까? (y/n) : ")
    if sel=='n':
        break
print("계산기 프로그램 종료")
'''

# 예제3] 함수의 인자값 사용 - 사용자가 입력한 값을 출력하는 함수 구현
#       사용자로부터 입력받은 값을 인자값으로 처리하는 함수
#       함수에 return을 사용하여 반환값 처리 예제

#함수 정의
'''
연산 결과 후에 반환값을 전달하는 함수
def pr3(str1):
    
    str1="입력한 문자열 : "+str1
    return str1
#메인
txt=input("입력 : ")
print()
pr_rs=pr3(txt)
print(pr_rs)
'''
#실습] 위의 내용을 토대로 계산 결과를 반환값으로 처리하는 함수로 변환
'''
def calc(calc):
    if '+' in calc:
        num1,num2=calc.split('+')
        num1=int(num1)
        num2=int(num2)
       return num1+num2
    elif '-' in calc:
        num1,num2=calc.split('-')
        num1=int(num1)
        num2=int(num2)
        return num1-num2
    elif '*' in calc:
        num1,num2=calc.split('*')
        num1=int(num1)
        num2=int(num2)
        return num1*num2
    elif '/' in calc:
        num1,num2=calc.split('/')
        num1=int(num1)
        num2=int(num2)
        return num1/num2
    else:
        return 0
    
#메인
while True:
    txt=input("계산식 입력하세요 : ")
    result=calc(txt)
    if result:
        print("계산 결과는 :" ,result)
    else:
        print("수식입력이 잘못되었습니다\n 다시 입력해주세요!")
    sel=input("계속 하시겠습니까? (y/n) : ")
    if sel=='n':
        break
print("계산기 프로그램 종료")
'''
# 두 수에 대한 한번의 계산식을 입력받아서 결과를 출력하는 코드를 이용
# 다음과 같이 코딩을 해보세요!!
#     - 사용자가 계산식 입력. 이것을 이용해서 처리
#     - calc()가 인자값으로 두 정수와 계산식(기초 : +,-,*,/)을 인자로 받아 처리하는 함수 만들어 동작시키세요
def calc(num1,num2,giho):
    if '+' in giho:
       return num1+num2
    elif '-' in giho: 
        return num1-num2
    elif '*' in giho:
        return num1*num2
    elif '/' in giho:
        return num1/num2
    else:
        return 0
    
#메인
while True:
    txt=input("계산식 입력하세요 : ")
    if '+' in txt:
        su1,su2=txt.split('+')
        su1=int(su1)
        su2=int(su2)
        giho="+"
    elif '-' in txt:
        su1,su2=txt.split('-')
        su1=int(su1)
        su2=int(su2)
        giho="-"
    elif '*' in txt:
        su1,su2=txt.split('*')
        su1=int(su1)
        su2=int(su2)
        giho="*"
    elif '/' in txt:
        su1,su2=txt.split('/')
        su1=int(su1)
        su2=int(su2)
        giho="/"
    else:
        print("수식입력이 잘못되었습니다\n 다시 입력해주세요!")
    result=calc(su1,su2,giho)   #함수 호출
    if result!=0:
        if type(result) is not float:
            print("계산 결과는 : ",result)
        else:
            print("계산 결과는 : {:.2f}".format(result))
    sel=input("계속 하시겠습니까? (y/n) : ")
    if sel=='n':
        break
print("계산기 프로그램 종료")
