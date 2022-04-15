# 객체지향 프로그래밍
# 1. 클래스와 오브젝트
# 
# 클래스란? - 특정 대상을 지정하여 정의를 담고 있는 것
# - 실세계의 것을 모델링하여 속성(Attribute, 멤버 변수)와 동작(Method)를 갖는 데이터타입
# - 예로 학생이라는 클래스를 생성한다면, 학생을 나타내는 속성과 
#    학생이 행하는 행동을 함께 정의할 수 있음.
# - 즉, 다루고자하는 데이터와 데이터의 연산을 하나로 캡슐화하여 클래스로 표현가능
# - 모델링에서 중요시하는 속성에 따라서 클래스의 속성과 행동이 달라짐

a=[1,2,3,4,5]
#print(help(a))

# 객체(Object) - 클래스에 정의된 대로 개별적으로 구성되어 있는 
# 개별, 독립적 대상 의미
# - 클래스로 구성되어 구체화 된 내용 (객체-인스턴스)
# - 파이썬은 모든것(int, float,str,list,dict...etc)은 객체(인스턴스)
# - 시제로 class가 인스턴스화 되어 메모리에 상주하고 있는 상태 의미
# - class가 빵틀(설계도)등이라면, object(객체)는 실제로 빵틀에 찍어낸 빵 의미
# #

# Class 선언하기
# 객체를 생성하기 위해서 객체의 모체가 되는 class를 미리 선언해야 한다.
# 
# (형식)
# class[클래스명]:
#       변수선언(멤버변수 -속성)
#       def 생성자(인수):
#           명령문...
#       def 함수명(인수):
#           명령문...

# 예제)
# 클래스 선언
class Person:
    pass #클래스 저으이 나중에 만들기 위해서 pass사용
#객체 생성
bob=Person()
cathy=Person()

a=list()
b=list()
print(type(bob),bob)
print(type(cathy),id(cathy))
print(type(a),type(b))

## 클래스 생성자
# - 생성자, 클래스 인스턴스가 생성될 때 호출됨
# - __init__(self)가 기본으로 생성하게 된다. self가 인자 처음 오고,
#   이는 자신을 가리킴
# - 이름이 꼭self일 필욘느 없지만 관례적으로 self로 사용
# - 생성자는 해당 클래스에서 다루는 데이터를 정의할 수 있음
#   정의하는 데이터를 멤버변수, 속성이라고 부름#

class Person:
    def __init__(self):
        print(self,'is generated')
        self.name='홍길동'      #이름 속성
        self.age=18             #나이 속성
p1=Person()
p2=Person()
print(p1,p2)
p1.name='홍길자'
p2.age=25
print(p1.name,p1.age)
print(p2.name,p2.age)

## 생성자에게 인자값을 전달하여 속성값 부여하고 싶은 경우
class Person:
    def __init__(self,name,age=10):
        print(self,'is generated')
        self.name=name      #이름 속성
        self.age=age        #나이 속성
p1=Person('bob',30)
p2=Person('kate',20)
p3=Person('홍길동')
print(p1.name,p1.age)
print(p2.name,p2.age)
print(p3.name,p3.age)

# 문제 1] Calc_class라는 클래스 선언
# 속성값은 x,y로 두개 초기화 구현
# 생성자에서 x,y속성값을 받을 수 있게 생성
# 객체를 생성하여 해당값을 참조해서 확인해보세요

class Calc_class:
    def __init__(self,x,y):
        self.x=x
        self.y=y

c1=Calc_class(100,200)
print(c1.x,c1.y)

## method 정의
# 멤버함수라고도 부름. 해당 클래스의 object에서만 호출 가능
# 메서드는 객체 레벨에서 호출되며, 해당 객체의 속성에 대한 연산을 행함
# 호출은 객체.메서드()형태로 호출됨
class Calc_class:
    #클래스 변수 : 속성
    x=y=0
    #생성자 : 객체 생성시 동작 + 멤버변수 초기화
    def __init__(self, a, b):
        self.x=a
        self.y=b
    #클래스의 메서드(함수)
    def plus(self):
        p=self.x+self.y
        return p
    def minus(self):
        m=self.x-self.y
        return m

c=Calc_class(10,20)
print(c.x,c.y,"더하기연산 결과 : ",c.plus())
print(c.x,c.y,"빼기 연산 결과 : ",c.minus())

#예제1] 자동차 클래스 생성
class Car:
    #멤버 변수
    cc=0    #엔진 cc
    door=0  #문 개수
    carType=None #null
    #생성자
    def __init__(self,cc,door,carType):
        #멤버변수 초기화
        self.cc=cc
        self.door=door
        self.carType=carType
    def display(self):
        print('자동차는 %d cc이고, 문짝은 %d개 타입은 %s' %(self.cc,self.door,self.carType))

##객체 생성
car1=Car(2000,4,'승용차')
car2=Car(3000,5,'SUV')
car1.display()
car2.display()

## 소멸자(Destructor) : 생성자 반대 역할 __del()이라는 이름으로 제공
#객체 사용이 완료되었을 때 자동으로 실행, 객체를 메모리에서 소멸시키는 역할

# class muliply:
#     #생성자
#     def __init__(self, x,y):
#         self.x=x
#         self.y=y
#     #소멸자
#     def __del__(self):
#         del.self.x
#         del.self.y 
        
##self
# 파이썬에서 Method는 항상 첫번재 인자로 self전달
# self는 현재 해당 메서드가 호출되는 객체 자신을 가리킴
# C++/C#, Java에서는 이를 this에 해당
# 이름 꼭, self일 필요는 없지만 관례상 self사용

#예시
class Person:
    name=None
    age=0
    #생성자
    def __init__(self,name,age):
        print("self : ",self)
        self.name=name
        self.age=age
    def sleep(self):
        print(self.name,"은 잠을 잡니다.")
a=Person('Abram',100)
a.sleep()



