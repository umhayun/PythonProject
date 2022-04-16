## python의 모듈 밑 패키지의 사용
# 모듈이란 ? 함수, 변수,클래스들을 모아놓은 파일
# (모듈은 만들어 놓은 다른 파이썬 프로그램에서 불러와서 사용 가능)
# 
# 모듈 만드는 방법 : *.py 확장자를 이용하여 만들 수 있음.
# 
# 모듈을 불러오는 방법 : import 명령어를 사용하여 모듈을 불러와 사용
# (표준 라이브러리를 불러와 사용할때에는 import 사용함.)
# 
# #

# 시간과 관련있는 모듈들...
import datetime,time
  
# datetime 모듈은 시간에 대해서 가공된 정보 처리
s=datetime.datetime.now()   #현재 시간 알아오는 함수
print(s)
t=time.localtime()
print(t)
print(t.tm_year)
print(t.tm_mday)
'''
start=time.time()
print(start)
time.sleep(5)   #5초멈추고 end실행
end=time.time()
print(end)
'''
# 모듈 불러와 사용하기
# (형식1)
# import 모듈명 =>모듈 내에 있는 모든 함수, 클래스, 변수 호출
# 
# 사용할 때 =>모듈명.함수(변수,클래스)
# #
import calc
a=100
b=200
c=10

sum=calc.Sum(a,b)
sub=calc.Sub(a,b)
mul=calc.Mul(a,c)
div=calc.Div(b,a)

print(sum,sub,mul,div)

calc.Result=(sum+sub)-int((mul/div))
print('((a+b)+(b-a))-int((a*c)/(b/a))=',calc.Result)

#(형식2)
# from모듈 import *
# =>모듈 내에 있는 모든 변수, 함수와 클래스 호출
# 모듈에 있는 내용을 사용할 경우 : 함수(변수, 클래스 )명 그대로 사용
from calc import *
a=10
b=20
c=30
sum=Sum(a,b)
sub=Sub(a,b)
mul=Mul(a,c)
div=Div(b,a)
print(sum,sub,mul,div)
Result=sum+sub+mul+div
print(Result)