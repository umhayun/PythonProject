#count(value): 특정 값의 개수 출력
lst1=[1,2,3,2,5,6,2,8]
su=lst1.count(2)
print(lst1)
print("2의 값을 가진 멤버의 개수 : ",su)

#index:특정 값의 인덱스 값을 반환
lst1=[1,2,3,2,5,6,2,8]
idx=lst1.index(2,4)  # 4번째 이후에 2 인덱스 찾기
print("idx값 확인 :",idx)

# reverse() : 리스트 멤버의 순서 반전(정렬 x)
lst1=[9,10,3,2,6,1,7,8,4,5]
print("reverse사용 전 : ",lst1)
lst1.reverse()
print("reverse사용 후 : ",lst1)

#sort(): 리스트 정렬 함수
#   - 오름차순: reverse=False (생략:기본값)
#   - 내림차순: reverse=True
lst1.sort()
print("lst1 오름차순 정렬 : ",lst1)
hi=lst1.sort(reverse=True)
print("lst1 내림차순 정렬 : ",lst1)

#사용시 주의사항
# 1. 숫자 형식 또는 문자 형식은 분리해서 정렬
# 2. 정수와 실수는 같은 숫자이기 때문에 정렬 가능.
# 3. 정렬된 리스트를 새롭게 만들고 싶은 경우, sorted() 사용
lst2=sorted(lst1)
print(lst1,id(lst1),'\n',lst2,id(lst2))
lst3=sorted("I am a student".split())
print(lst3)
lst4=sorted("I am a student".split(),key=str.lower)
print(lst4)

# ** split() 문자열을 분리하는 함수
# : "()"안에 아무것도 넣어주지 않으면, 공백(스페이스,탭,엔터 등)을 
# 기준으로 문자열을 나누어 사용함. 만약 split(';')을 사용하면, ';'을
# 기준으로 문자열을 나누겠다는 의미

# Copy 기능
# - shallow copy : 서로 다른 변수가 같은 위치에 있는 데이터를 가르키는 경우
# - deep copy : 두개의 변수가 별도의 공간을 가리키는 경우

#ex) shallow copy 
list1=[1,2,3,4,5]
list2=list1
print('list1의 값 : ',list1,'\tlist1의 주소값',id(list1))
print('list2의 값 : ',list2,'\tlist2의 주소값',id(list2))

#ex) deep copy
list1=[1,2,3,4,5]
list2=list(list1) # list()는 새로운 리스트 생성 매서드
print('list1의 값 : ',list1,'\tlist1의 주소값',id(list1))
print('list2의 값 : ',list2,'\tlist2의 주소값',id(list2))

#복사기능을 제공하는 copy모듈 불러서 사용
import copy
list1=[1,2,3,4,5]
list=copy.deepcopy(list1)   #deepcopy
list3=list1                 #shallow copy


#문제1
list=[30,20,10]
list.append(40)
print(list)
list.pop(3)
print(list)
list.sort()
print(list)
list.reverse()
print(list)

#문제2
list=[30,20,10]
a=list.index(10)
print("10인덱스 : ",a)
list.insert(2, 200)
print(list)
list.remove(200)
print(list)
list.extend([555,666,555])
print(list)
b=list.count(555)
print("555의 개수 : ",b)



# 2차(원) 리스트
# : 리스트 안에 멤버 중에 리스트가 존재하는 경우 사용되는 방식
# 리스트 안에 있는 리스트 멤버에 대한 참조 방식
# ex) 2차 리스트 변수 값 참조
aa=[[1,2,3,4],      #aa[0]
    [5,6,7,8],      #aa[1]
    [9,10,11,12]]   #aa[2]
    #aa리스트의 멤버의 개수  : 3
print(len(aa))      #3

for x in range(len(aa)):
    for y in range(len(aa[x])):
        print(aa[x][y],end='\t')
    print()


#예제 2] 2차 리스트 생성 및 출력
ls_1=[];ls_2=[];value=1
#2차 리스트 생성
for i in range(3):
    for j in range(4):
        ls_1.append(value)
        value+=1    
    ls_2.append(ls_1)
    ls_1=[]

#출력(읽기)
for x in range(len(ls_2)):
    for y in range(len(ls_2[x])):
        print(ls_2[x][y],end ='\t')
    print()


#문제1 numbers=[10,20,30,40,50,60,70]
#모두 더한 값
numbers=[10,20,30,40,50,60,70]
print("모든 원소값 합계",sum(numbers))
#문제2 1~45 중복 없이 6개 생성
from random import randint
list=[]
cnt=0
while True:
    ran=randint(1, 45)
    if ran not in list:
        list.append(ran)
        cnt+=1
        if cnt==6:
            break
    if ran in list:
        continue
print(list)








