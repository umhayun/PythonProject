

# 퀴즈 : 리스트 정의하여 첨자 위치 저장
# a의 총 개수와 첨자의 위치 출력

st='Have a nice day Have a nice day Have a nice day'
list=[]
idx=0
while True:
    idx=st.find('a',idx)
    if idx!=-1:
        list.append(idx)
        idx+=1
    else:
        break
print("a 개수 : ", st.count('a'))
print('첨자의 위치 출력',list)

#strip()특정문자 제거
str2='파이썬파'
print(str2.strip('파'))     #이썬
print(str2.lstrip('파'))    #이썬파
print(str2.rstrip('파'))    #파이썬

st3='--1-파이썬-1--'
print(st3.strip('-'))   #1-파이썬-1
print(st3.lstrip('-'))  #1-파이썬-1--
print(st3.rstrip('-'))  #--1-파이썬-1
#replace()함수 사용
st='2015-06-05'
print(st[0:4])
print(st.replace(st[0:4],'2022'))
#split(str): 특정 문자 기준으로 문자열 나누는 함수->리스트로 반환

#splitlines() :개행('\n')을 기준으로 문자열 나누는 함수->리스트 저장
st2='Naver\nEver\nGive\nUp'
print(st2)
print(st2.splitlines())
# 여러줄 문자열 처리 : '''~''',"""~"""
st='''Naver give up
naver 
naver give me'''
print(st)
a=st.splitlines()
print(a)
#join(): 지정한 문자열을 기준으로 문자열 데이터 결합 
st3='123'
print(st3.join('%%'))
print('%'.join(st3))

#아래의 리스트를 문자열로 변경해보세요. 'I am a student'로 변경 join()이용

list2=['I','am','a','student']

print(' '.join(list2))

#문제
#input함수로 이름과 나이값을 입력 받을 때 한번에 입력 받아 처리하고
#출력하는 코드 작성
# ex) 이름과 나이 입력하세요 : 
    #=>이름: 엄하윤 나이: 26살
'''
self=input("이름과 나이를 입력하세요 : ")
list=self.split(' ')
name=list[0]
age=list[1]
print(f"이름 : {name}, 나이 : {age}살")
'''
#문제
# input함수로 입력 받은 수의 더하기 빼기 곱하기 나누기의 간단한 수식처리 코드
#ex)계산식 입력하세요:
    #계산 결과:
'''
while True:
    calc=input("계산식 입력하세요 : ")
    if '+' in calc:
        num1,num2=calc.split('+')
        num1=int(num1)
        num2=int(num2)
        print("계산 결과 : ",num1+num2)
    elif '-' in calc:
        num1,num2=calc.split('-')
        num1=int(num1)
        num2=int(num2)
        print("계산 결과 : ",num1-num2)
    elif '*' in calc:
        num1,num2=calc.split('*')
        num1=int(num1)
        num2=int(num2)
        print("계산 결과 : ",num1*num2)
    elif '/' in calc:
        num1,num2=calc.split('/')
        num1=int(num1)
        num2=int(num2)
        print("계산 결과 : ",num1/num2)
    else:
        print("수식이 잘못되었습니다. 다시 입력해주세요!")
    sel=input("계속 하시겠습니까?")
    if sel=='n':
        break
'''