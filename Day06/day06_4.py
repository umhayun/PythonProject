###알고리즘
'''
알고리즘이란, 어던 문제를 해결하기 위한 일련의 절차를 의미함.
프로그래밍이 논리적인 절차를 의미하는 로직을 기초로 삼고 있기 때문에 이를 통해서 문제 해결하는 것을
말함

알고리즘의 만족 조건 
- 입력 : 외부에서 제공되는 자료가 있을 수 있다.
- 출력 : 적어도 한가지 이상의 결과가 나올 수 있다.
- 명백성 : 각 명령들은 애매한 부분이 없이 간단 명료해야 한다.
- 유한성 : 반드시 종료 조건이 있어야 한다.
- 효과성 : 모든 명령들은 명백하고 실행가능한것이여야 한다.
'''

#최대값/최소값(max/min)
# : 전체 자료의 원소들 중에 큰 값과 가장 작은 값을 선별하는 기본 알고리즘

# 1. 입력 자료 생성
import random
dataset=[]
for i in range(10):
    r=random.randint(1, 100)
    dataset.append(r)
print(dataset)

# 2. 변수 초기화
vmax=vmin=dataset[0]

# 3. 최대 최소값 구하기
for i in dataset:
    if vmax<i:
        vmax=i
    if vmin>i:
        vmin=i
# 결과 출력
print("max=",vmax,'min=',vmin)

## 정렬(sort)
dataset=[3,5,1,2,4]
for i in range(0,len(dataset)-1):
    for j in range(i+1,len(dataset)):
        if dataset[i]>dataset[j]:
            tmp=dataset[i]
            dataset[i]=dataset[j]
            dataset[j]=tmp
    print(i,'번째',dataset)
    
##검색(search)
# 검색 알고리즘은 순차 검색과 이진검색(이분법)
dataset=[5,10,18,22,35,55,75,103]
value=int(input("검색할 값 입력 : "))

low=0       #스타트 위치
high=len(dataset)-1 #end의 위치
loc=0
state=False #상태 변수

while (low<=high):
    mid=(low+high)//2
    if dataset[mid]>value:  #중앙값이 찾는 값보다 클경우
        high=mid-1
    elif dataset[mid]<value:
        low=mid+1
    else: #찾은 경우
        loc=mid
        state=True
        break
if state:
    print(f"찾은 위치 : {loc}번째")
else:
    print("찾는 값이 없습니다.")
        