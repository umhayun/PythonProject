##인자값 처리 방식1 => 연속된 자료를 처리하는 함수의 인지 처리 방식
#예제
def pr8(a,b,c):
    print(a,b,c)
    
#메인
pr8(10,20,30)

# "*"를 이용하여 리스트 또는 튜플과 같은 자료를 연속된 인자값으로 처리
# 리스트 또는 튜플의 변수값을 받아서 "unpacking"하는 방식으로 인자 전달
x=[100,200,300]
y=[10,20]
z=1,2,3,4
pr8(*x)     #a,b,c[100,200,300] =>사용

# "*"를 이용하여 연속된 자료(리스트,튜플)에 데이터를 인자로 전달이 가능하나
# 인자의 개수와 전달되는 자료의 개수는 같아야 한다(**)

# 인자값 처리 방식 2 => 가변인자처리...
# - 고정인자 => 인자값을 반드시 정해진 값으로 1:1로 인자를 전해야 하는 인자 (일반)
# - 가변인자 => 인자값을 정해진 개수로 전달하지 않고, 가변적으로 전달가능한 인자

# 가변이자 설정은 함수 정의시에 매개변수(인자) 앞에 '*'을 사용한다.

# 전달된 인자 값들의 합을 구하는 예제
def sum_func(*par):
    result=0
    print(par,type(par))
    for su in par:
        result+=su
    return result

def dis():
    Sum=0
    Sum=sum_func()
    print(Sum)
    Sum=sum_func(10,20,30)
    print(Sum)
    Sum=sum_func(10,20,30,40,50)
    print(Sum)
dis()

##주의) 인자값 처리함에 있어 고정인자와 가변인자를 동시에 사용하는 경우,
# 고정인자를 먼저 처리하도록 한다.즉, 가변인자는 마지막에 사용되게 해야한다.

#"**"를 사용하는 경우는 딕셔너리에 대한 packing을 시도한다는 의미로 처리
#ex) 딕셔너리 자료형을 받아서 처리 함수
def dic_func(**par):
    print(par,type(par))
    for k in par:
        print(f'{k}:{par[k]}')
list=['test1','test2','test3','test4']
dic_func(피카츄='1마리',파이리='2마리',꼬부기='없음',라이칸=1)
dic={'sep':'-','end':'\n\ntest'}
print('test','test',**dic)      #sep과 end가 작동한것
print(*list,**dic)