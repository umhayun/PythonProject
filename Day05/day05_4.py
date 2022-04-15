'''
딕셔너리(Dictionary)
1. List와 비슷한 자료형. List는 요소(멤버)에 대한 접근시 첨자(Index)를 사용
2. 딕셔너리도 첨자 사용, 사용하는 첨자는 'key'를사용
3. 딕셔너리는 key가 가리키는 곳에 값(value-데이터)이 존재함.
  key값을 사용하는 장점:
      1) 빠른 탐색 - 탐색속도 빠름
      2) 사용하기 편리함
4.딕셔너리를 정의할때는 "{}" 를 사용함.
5. 특정 슬롯에 대하여 참조할 때는 key-value를 입력하거나,
딕셔너리 안에 있는 요소를 참조할 경우에 "[]"를 사용한다.

(형식)
변수명={} #비어있는 딕셔너리 선언
변수명={key1:value,key2:value2,.....}
dict()를 이용해서 선언하는 경우,
변수명=dict([(k1,v1),(k2,v2),(k3,v3),...])
(접근방식)
dic={key:value}
dic[key]=value1
print(dic[key]) =>value값 출력
'''

print(dict([('a',100),(1,'test')]))
dic={'a':100,1:'test'}
print(dic['a'])
print(dic[1])
dic={'a':1,'b':2,'c':3}
print(dic['c'])
dic['c']=5*dic['b']
print(dic['c']) 
dic['d']=100
print(dic)

#for문 사용
for k in dic:
  print(k)
  print(f'키값 : {k}, 키를 이용한 참조값: {dic[k]}')
  
#예제3] 딕셔너리와 리스트를 같이 사용하는 경우 (딕셔너리 안에 값을 리스트로 사용)
dl={'음료':['탄산','과일','우유','물'],
    '식사':['김밥','라면','돈까스','비빔밥']}

for key in dl:
  print(dl[key])
  for i in dl[key]:
    print(i,end=' ')
  print()
  for j in range(4):
    print(dl[key][j], end=' ')
  print()
  
#예제4] 리스트 안에 딕셔너리가 있는 경우
ld=[{'name':'홍길동','age':18,'blood':'A'},
    {'name':'이방원','age':24,'blood':'B'}]
for dic in ld:
  print(dic['name'],dic['age'],dic['blood'])
  
# 딕셔너리에서 사용하는 함수들
# - update(dict) : 사전형 자료에 값 추가(key:value)
# - fromkeys(iter[,value]) : iter에 리스트, 튜플의 값을 딕셔너리의 키로 사용하는
#                             딕셔너리를 생성하여 반환
# - get(key[,value]) : 사전형의 키를 사용하여 값을 얻어오는 함수
# - keys() : 사전형 자료에서 모든 키를 반환하는 함수
# - values() : 사전형 자료에서 모든 값을 반환하는 함수
# - items() : 사전형의 모든 '키:값'의 쌍으로 튜플(*)로 반환
# - pop(key) : 사전형 자료의 키를 통해서 값을 반환한 후에 삭제
# - popitem() :  사전형 자료의 마지막 '키:값' 쌍을 튜플(*)로 반환 후 삭제
# - clear() : 사전형의 모든 '키:값'을 삭제하여 빈 사전형 자료로 만듬

#update()
dic={'a':1,'b':2,'c':3}
dic.update({'d':4})
print(dic['a'])
print(dic['d'])
print(dic)

#fromkeys(iter,value)
ke=['a','b','c','d']
dic1={}.fromkeys(ke)
dic2={}.fromkeys(ke,1)
print(dic1)
print(dic2)

#get(key[,value]) **
dic={'a':1,'b':2,'c':3}
value=dic.get('b')
print(value)
print(dic.get('d'))   #None
print(dic.get('d','Not exist key'))   #Not exist key
print(dic.get('c','Not exist key'))   #3
print(dic)

#keys()
dic={'a':1,'b':2,'c':3}
for key in dic.keys():
  print(key,end=' ')
print(type(dic.keys()))
print(dic.keys())
print()

#values()
dic={'a':1,'b':2,'c':3}
for values in dic.values():
  print(values,end=' ')
print()
print(dic.values())

#items()
dic={'a':1,'b':2,'c':3}
for key,value in dic.items():
  print(f'{key} : {value}')

#pop(key)
dic={'a':1,'b':2,'c':3}
value=dic.pop('b')
print(value)
print(dic)

#popitem()
dic={'a':1,'b':2,'c':3}
tu1=dic.popitem()
print(tu1)
print(dic)

#clear()
dic={'a':1,'b':2,'c':3}
print(dic)
dic.clear()
print(dic)

# <<문제>>
# 1. 이름, 전화번호, 이메일 주소를 키로 사용하는 사전자료 생성하시오
# 2. 리스트형 변수에 1번 문제와 같은 사전 자료가 여러개 생성될 수 있게 하시오.
# (입력값을 받아서 자료 생성)
# 3. 2번에서 입력한 자료가 출력될 수 있도록 하시오.
# (출력예시)
# 이름 : 홍길동
# 전화번호 : 010-xxxx-xxxx
# 이메일 : xxxx@xxxx.com

people={'이름':'홍길동','전화번호':'010-xxxx-xxxx','이메일':'xxxx@xxxx.com'}

# import os
# ld=[]

# while True:
#   dic2={}
#   dic2.update({'이름':input('이름 입력 : ')})
#   dic2.update({'전화번호':input('전화번호 입력 : ')})
#   dic2.update({'이메일':input('이메일 입력 : ')})
#   a=input('계속 하시겠습니까 (o/x): ')
#   ld.append(dic2)
#   if a=='x':
#     break


# for d in ld:
#   print(f"이름 : {d['이름']}")
#   print(f"전화번호 : {d['전화번호']}")
#   print(f"이메일 : {d['이메일']}")
  
import turtle
turtle.shape('turtle')
for x in range(3):
  if x==0 : turtle.color('red','red')
  if x==1 : turtle.color('green','green')
  if x==2 : turtle.color('blue','blue')
  for i in range(3):
    turtle.forward(100)
    turtle.right(120)
  turtle.penup()
  turtle.backward(200)
  turtle.pendown()
turtle.exitionclick()
turtle.begin_fill()
turtle.end_fill() 