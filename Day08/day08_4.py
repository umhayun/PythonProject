## 획득자(getter), 지정자(setter), nonlocal
# 내부함수는 중첩함수에서 함수 클로저 역할도 하지만, 함수내 자료를 외부로 획득하거나
# 자료를 수정하는 역할도 한다. 이런 내부 함수들을 획득자(getter), 지정자(setter)라고 부르며
# 역할과 필요 요건은 다음과 같다.

# 획득자 함수 : 함수 내부에 생성한 자료를 외부로 반환하는 함수로 반드시 return  명령 가진다.
# 지정자 함수 : 함수 내부에 생성한 자료를 외부에서 수정하는 함수로 반드시 매개변수를 가진다.
#               만약 외부함수에서 생성된 자료를 수정할 경우 해당변수에 nonlocal명령어를 쓴다.

# (형식)
# def 외부함수():
#     변수명=값
#     def 내부함수():
#         nonlocal 변수명
 
# 예시) 획득자와 지정자 함수, 그리고 nonlocal명령어를 이용하여 외부함수에서 생성한 자료를
# 외부에서 획득하고, 수정하는 예문

#함수 정의
def main_func(num):
    num_val=num             #자료 생성
    def getter():           #획득자 함수 ---return
        return num_val
    def setter(value):      #지정자 함수 인수 필요
        nonlocal num_val    #nonlocal명령어  
        num_val=value
    return getter,setter    #함수 클러저 반환

#함수 호출
getter,setter=main_func(100)    #num생성
print('num=',getter())
setter(200)
print('set이후 num=',getter())

#함수 장식자(decoration)는 기존 함수 시작부분과 종료부분에 기능을 장식하여 추가해주는 별도의 함수
#즉, 현재 실행되는 함수를 파라미터로 받아서 꾸며줄 내용과 함께
#해당함수를 감싸주는 함수 (Wrapping function)

# (형식)
# @ 함수 장식자     => 사전에 만들어 있어야 함. @wrapping함수명
# def 함수명():
#     함수 실행문

# wrapper 함수
def wrap(func):     #함수를 받음
    def decorated():
        print('반가워요~~~~~~~')    #시작 부분에 삽입
        func()                      #인수로 넘어온 함수 실행
        print('반가웠어~~~~~~~~')   #종료부분에 삽입
    return decorated                #클로저 함수 반환

#장식자 적용할 함수 선언
@wrap
def hello():
    print('hi','홍길동~~')
#함수 호출
hello()

#재귀함수(Recursive Function)
# 함수 내부에서 자신의 함수를 반복적으로 호출하는 함수 

# 재귀함수는 반복적으로 호출하기 때문에 반드시 함수내에 반복 탈출(exit) 조건 필수,
# 재귀함수는 반복적으로 변수를 조금씩 변경하여 연산을 수행하는 알고리즘에서 이용됨

#ex)팩토리얼 계산 등

#예제) 카운트->1~n까지 정수를 count(카운트)하는 과정 

#재귀함수 정의

def Counter(n):
    if n==0:
        print(n,'종료')
        return 0    #종료 조건
    else:
        print(n,end=' ')
        Counter(n-1)    #재귀함수 호출

print('n=0',Counter(0))     #n=0 0
Counter(5)

#예제)누적합
#1~n까지 정수를 카운트한 값을 누적하여 반환하는 경우

#재귀함수 정의
def Adder(n):
    if n==1:        #종료 조건
        return 1
    else:
        result=n+Adder(n-1)     #재귀 호출
        print(n,end=' ')        #스택영역 n=5 -> 2 3 4 5
        return result
re=Adder(5)
print(re)