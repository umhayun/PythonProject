'''
LIST
리스트 자료형이란?
- 데이터 목록을 다루는 자료형
- 리스트 정의 "[]"를 사용
- 리스트 안에는 어떤 종류의 자료형이든 상관 없이 저장 가능.

LIST 자료형의 기본 사용(정의)
(정의)
변수명=[]   #비어있는 리스트 선언
변수명=[V1,V2,V3...]
(V들은 타임 상관 없이 가능)

(list()를 이용한 리스트 생성)
변수명=list()
변수명=list("HELLO") #['H','E','L','L','O']
변수명=list(range(5)) #[0,1,2,3,4]
'''

#리스트 결합
list=[1,2,3,4]
list2=[5,6,7]
list3=list+list2
print(list3)

#리스트 반복
print(list2*3)      #[5,6,7,5,6,7,5,6,7]

list=list2+list3+list
#max() : 최댓값, min(): 최소값
print(max(list))    #최대
print(min(list))    #최소
print(sum(list))    #합
print(pow(4,2))     #제곱 (x,y) x의 y승

# 변수 선언, 3개의 정수를 입력받아 합을 출력 코딩

# list4=[]
# for i in range(3):
#     a=int(input('정수 : '))
#     list4.append(a)
# print(sum(list4))

## List 인덱싱
# : 인덱스 값을 이용한 참조 
list= [1, 2, 3, 4, 5, 6, 7, 8]
# 양의 index  0  1  2  3  4  5  6  7
# 음의 index -8 -7 -6 -5 -4 -3 -2 -1

# (-1) => 11111111 11111111 11111111 11111111
# (-2) => 11111111 11111111 11111111 11111110

print('list[]', list)
print('list[-1] :',list[-1])
print('list[-2] : ',list[-2])
print('list[-3] : ',list[-3])

# slicing 방식을 이용한 시퀀스 객체 (자료) 접근
# slicing 이란 ? 리스트와 같은 시퀀스 자료값들의 범위로 접근하기 위해서
#               사용하는 방법으로 시퀀스 자료의 일부를 잘라 새롭게 생성하는것

# (형식)
# 변수명[시작인덱스:끝인덱스]
# 변수명[시작인덱스:끝인덱스:증감값]
# ex)
list= [1,2,3,4,5,6]
#index 1 2 3 4 5 6
#     -1-2-3-4-5-6
print(list[0:3])    #[1,2,3]
print(list[0:3:2])  #[1,3]

#인덱스 생략
print(list[:3])     #시작값 생략 : [1,2,3]
print(list[3:])     #끝값 생략 : [4,5,6]
print(list[:])      #둘다 생략 : [1,2,3,4,5,6]

#슬라이싱후 새로운 리스트 생성
slc1=list[3:6]
print(slc1)

'''
리스트 함수들...
 - append(value) : 리스트 끝에 값 추가 (멤버 추가)
 - extend(iter) : 리스트 끝에 list, tuple, dict의 값을 하나씩 추가
 - insert(idx,value) : idx(인덱스)에 있는 인덱스 위치에 특정값 추가 함수
 ======================================================================
 - pop([idx]) : 인덱스를 지정하지 않으면, 마지막 인덱스 값을 반환후 삭제
                인덱스 값을 지정하면, 해당 인덱스값 반환후 삭제
 - remove(value) : 특정 값을 찾아서 삭제
 - clear() : 리스트의 모든 멤버 삭제, 빈리스트로 만듦.
 ======================================================================
 - count(value) : 리스트 내에 특정 값의 개수 반환
 - index(value) : 리스트 내에 특정 값의 인덱스 값을 반환하는 함수
 - reverse() : 리스트의 멤버의 순서를 뒤집어서 나열
 - sort([reverse=False]) : 리스트의 값을 오름차순(False), 내림차순(True)정렬
'''

#extend
list=[1,2,3,4,5,6]
list.extend('abcd')     #문자열 추가시 하나씩 분리되어저장
print(list)             #[1,2,3,4,5,6,a,b,c,d]


#insert(idx,value) : idx인덱스 위치에 값 추가
list=[1,2,3,4,5,6,7,8]
list.insert(3,'a')      #그자리 값을 밀어내고 자리차지 모두 한자리씩밀려남
print(list)

#pop()
list=[1,2,3,4,5]
a=list.pop()
print(a)
print(list)
b=list.pop(1)
print(b)
print(list)     #인덱스 1값 없어지고 모든값들이 앞으로 당겨짐


#remove(value)

list=[1,2,3,2,5,6,2,8]
list.remove(2)
print(list)
list.remove(2)
print(list)