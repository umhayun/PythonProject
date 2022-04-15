### set클래스 
# 여러개의 지료를 비순서로 적재하는 가변길이 비순차 자료구조
#변수={값1,값2,값3,...}
# 특징
# - 중복 불가
# - 순서가 없기 때문에 색인(index)를 사용할 수 없다.
# - 객체에서 제공하는 함수를 이용해서 추가, 삭제 및 집합 연산 등이 가능함.

# 1)중복 불가
se={2,3,4,3,1}  #숫자인 경우에는 정렬 표시
print(len(se))
print(se)
st=set('hello') #set(): 셋 타입을 생성하는 함수
print(len(st))
print(st)

# 2) 요소 반복
for d in se:
    print(d,end=' ')
print()

for s in st:
    print(s,end=' ')
print()

# 3) 집합 관련 함수
# - union([set타입 자료]) : 합집합
# - difference([set타입 자료-뺄집합]):차집합
# - intersection([set타입 자료]): 교집합

se2={2,4,6,8}
print(se.union(se2))            #{1,2,4,6,8}
print(se.difference(se2))       
print(se.intersection(se2))
st2=set('world')
print(st.union(st2))
print(st.difference(st2))
print(st.intersection(st2))

##값의 타입은 상관하지 않음
list=['test','user','server','data']
print(set(list))

##set을 사용하는 예시: 중복된 원소 제거

# python의 문자열
# :파이썬에 사용하는 문자열 처리

# 특징
# 1) 인덱싱을 이용한 참조 가능
string='python string'
print(string[0])    #p
print(string[7])    #s
print(string[-1])   #g
# 2) 슬라이싱을 이용한 참조
print(string[:6])   #python
print(string[0::2])  #pto tig
# 3) 문자열 반복문(for)
st='python string for'
for x in st:
    print(x,end=' ')
    
#문자열 함수
'''
 - find(str) : 문자열에서 특정 문자열을 찾아서 해당 문자의 index값 반환
 - count(str) : 문자열에서 특정 문자열을 찾아서 해당 문자열의 수 반환
 - lower() : 문자열에서 영문 대문자를 소문자로 변경하여 반환
 - upper() : 문자열에서 영문 소문자를 대문자로 변경하여 반환
 - strip() : 문자열에서 양쪽 공백 또는 문자를 제거하여 반환
 - lstrip() : 문자열에서 왼쪽 공백 또는 문자를 제거하여 반환
 - rstrip() : 문자열에서 오른쪽 공백 또는 문자를 제거하여 반환
 - replace(old,new) : 문자열에서 왼쪽(old)문자열을 찾아서, 오른쪽(new)
  문자열로 변경
 - split() : 문자열을 특정 문자열 기준으로 분리 -> 반환값 리스트 
'''
#find 예제
st='python string'
print()
print(st.find('string'))       #7
#find(str,시작 인덱스,끝 인덱스)
print(st.find('t'))            #2
print(st.find('t',3))          #8
#find()가 문자열을 찾지 못한 경우의 반환값 :-1
print(st.find('t',9))

#count()
st='python string'
print(st.count('t'))    #2
#count(str,시작idx,끝idx)
print(st.count('t',6))  #1

#lower()
st='PYTHON STRING'
print(st.lower())   #반환값으로 변경된 내용 전달. 원본 수정 x
print(st)
st1=st.lower()
print(st1)
#upper()
st='python string'
print(st.upper())
st2=st.upper()
print(st2)

#strip() : 양쪽에 인자로 전달받은 문자열 제거
#          인자값이 없는 경우 공백 제거.
st='        python string'
#print(st)
print(f"[{st}]")
st1=st.strip()
print(f"[{st1}]")
#lstrip()
st2=st.lstrip()
print(f"[{st2}]")
#rstrip()
st3=st.rstrip()
print(f"[{st3}]")

#replace(old,new)
st='python string'
st1=st.replace('string','문자열')
print(st1)

#split(str) 문자열을 str에 있는 문자를 기준으로 분리 -> list로 저장
st='python string'
st1=st.split()  #공백 기준으로
print(st1)      #['python','string']

#swapcase() : 영문 대소문자를 변경 대문자->소문자,소문자->대문자
print(st)
#title() 단어 첫번째 글자만 대문자
#문제1
# 1)아래의 문장 주어진 조건에 맞게 변경
# 'NevEr-eVer 100gIVe Up' [전]
# 'Never-Ever 100Give Up' [후]
st='NevEr-eVer 100gIVe Up'
st1=st.title()
print(st1)
# 2) Have a nice day 문자열에서 다음알아오기
# 'a', 'day','dak'의 갯수 알아오기
st2='Have a nice day'
print('a의 개수 : ',st2.count('a'))
print('day의 개수 : ', st2.count('day'))
print('dak의 개수 : ',st2.count('dak'))

#문제2. "It is a fun python class" 문자열의 길이,
#문자 'a'의 개수, 's'의 개수를 출력하는코딩 (함수 사용 x)
st3="It is a fun python class"
cnt=cnt_a=cnt_s=0
for i in st3:
    cnt+=1 #문자열 길이
    if i=='a':
        cnt_a+=1
    elif i=='s':
        cnt_s+=1
print("문자열의 길이 : ",cnt)
print("문자열 'a'의 길이 : ",cnt_a)
print("문자열 's'의 길이 : ",cnt_s)
#문제3. "Have a nice day"  문자열을 가지고 다음을 처리하세요.
# 1) 각각 find와 index를 사용하여 "day" 문자의 위치를 찾으세요.
# 2) 각각 find와 index를 사용하여 "kkk"문자의 위치를 찾으세요.
st4="Have a nice day"
print("find('day') : ",st4.find('day') )
print("index('day') : ",st4.index('day') )
print("find('kkk') : ",st4.find('kkk') )
print("index('kkk') : ",st4.index('kkk') )

# 3) find를 사용하여 첫번째, 두번째, 세번째, 네번째 'a'의 위치 출력
idx=st4.find('a')
print("첫번째 위치 : ",idx)
idx=st4.find('a',idx+1)
print("두번째 위치 : ",idx)
