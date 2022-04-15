'''
튜플(tuple)
: 리스트와 비슷한 자료형으로 튜플 안에 다양한 형태의 값을 사용할 수 있음.
(형식)
튜플변수명=(value1,value2,value3,...)
리스트와 튜플의 차이점
1. 리스트는 "[]"를 사용하지만, 튜플은 "()"를 사용한다.
2. 리스트는 그 값을 생성, 삭제 수정이 가능하지만
    튜플은 그 값을 바꿀 수 없음(중요)
3. 튜플은 멤버(요소)의 값이 1개인 경우 반드시 뒤에 ","를 붙여야 한다.
    ex)tu=(1,), tu=(1)(x)
4. 튜플은 가장 외각에 있는 ()는 생략 가능
tu=10,20,30
튜플의 인덱싱
: 튜플도 리스트와 같이 인덱싱을 통해서 값에 접근
인덱스값 (+) :  0  1  2  3  4  5  6  7  8  
인덱스값 (-) : -9 -8 -7 -6 -5 -4 -3 -2 -1
  튜플       : (1, 2, 3, 4, 5, 6, 7, 8, 9)
  
튜플의 슬라이싱(slicing)
 : 튜플의 특정 범위의 값에 접근하기 위한 방법으로 리스트와 동일하게 사용
'''

# 예제1] 튜플의 정의 및 사용
tu=(1,2,3,4,5)
print(type(tu))
print(tu[0])    #1
print(tu[4])    #5
print(tu[-1])   #5
print(tu[:3])   #(1,2,3)
print(tu[3:])   #(4,5)

tu1='문자열',100,123.456    #괄호 생략 가능
print(tu1,type(tu1))
tu2=(10)
print(tu2,type(tu2))
tu3=(10,)
print(tu3,type(tu3))
tu1=10,20,30
tu2=40,50,60
tu1=tu1+tu2
print(tu1)
tu3=tu1[2:]
print(tu3) 
# packing과 unpacking
# : 튜플과 같은 자료형으로 묶어 사용하는 것 packing,
# 반대로 묶여진 튜플과 같은 자료형을 나눠서 사용하는것 unpacking

# ex) (1,2),(3,4)
# packing => pack=((1,2),(3,4))
# unpacking=>a,b=pack #a=(1,2), b=(3,4)

a,b,c=10,20,30  #unpacking
pack=10,20,30
a,b,c=pack
print(a,b,c)
list=[100,200,300]
a,b,c=list
print(a,b,c)
st='abc'
a,b,c=st
print(a,b,c) 

# 튜플의 함수
# - index(value) : 튜플에 있는 값에 해당하는 멤버의 인덱스 값 반환
# - count(value) : 튜플에 있는 값의 개수 반환

#예제4
tu=(100,200,'함수',100,'개수')
print(tu.index(200))  #1
print(tu.index(100))  #0
print(tu.count(100))  #2

# (문제)
# 1. numbers=(10,20,30,40,50,60,70)
# 위 튜플 자료에서 30과 40을 따로 num1,num2 변수에 할당
numbers=(10,20,30,40,50,60,70)
idx1=numbers.index(30)
idx2=numbers.index(40)
num1=numbers[idx1]
num2=numbers[idx2]
print(num1,num2)

# 2. menu=(('칼국수',6000),('비빔밥',5500),('돼지국밥',7000))
# 위 자료를 다음 양식처럼 출력
menu=(('칼국수',6000),('비빔밥',5500),('돼지국밥',7000))
for x in range(len(menu)):
  print(f'{menu[x][0]}- {menu[x][1]}원')

# [Tuple 종합 문제]
# 1. 여러개의 값을 패킹시킨 후 저장되어 있는 값을 빼내어 출력하시오(5개 값 저장)
# (Tuple의 값을 리스트에 저장하시오. 단 , len함수 이용)
tu=(200602,'화요일','python',31.5,6000)
list=[]
for x in range(len(tu)):
      list.append(tu[x])
print(list)
# 2.아래와 같이 출력하시오 
# ---------------------------
#   (Tuple)        (List)
#   회사정보  :   삼성전자
#   제품명    :   Galaxy
#   가격정보  :   100원
#   출시일    :   미정
# ---------------------------

tu='회사정보','제품명','가격정보','출시일'
list=['삼성전자','Galaxy','100원','미정']
print('(Tuple)\t\t(List)')
for x in range(len(tu)):
      print(f'{tu[x]}   :   {list[x]}')

# 3.위에서 출력한 내용을 업데이트 하시오.
# [단, Index,Insert, Remove 함수를 전부 사용]
# 가격:100->110
# 출시일 : 미정->이번달 말
price=list.index('100원')
out=list.index('미정')
list.remove('100원')
list.insert(price, '110원')
list.remove('미정')
list.insert(out, '이번달 말')

print(list)