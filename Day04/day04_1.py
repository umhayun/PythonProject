#문제 6-1
for i in range(6):
    for j in range(i):
        print('*', end='')
    print()
    
print('='*20)
#문제 6-2
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print('*',end='')
    print()
    
print('='*20)
#문제 6-3
for i in range(6):
    for j in range(5-i):
        print(' ',end='')
    for j in range(i):
        print('*',end='')
    print()
print('='*20)  
#문제 6-4
for i in range(6):
    for j in range(i):
        print(' ',end='')
    for j in range(5-i):
        print('*',end='')
    print()
print('$'*0)
##########
import os   #os모듈은 파이썬에서 제공하는 기본 라이브러리 모듈로
            #os와 관련된 함수들이 저장된 모듈
            #system()=>os의 시스템 명령어를 사용할 수 있게 함.

import time #시간과 관련된 제공하는 기본 라이브러리 모듈
i,j=0,0;
q=1
#문제 6-5
while q:
    os.system('cls')
    num=int(input("홀수 줄수 입력 : "))
    st=1
    sp=num//2
    flag=True
    for i in range(num):
        for j in range(sp):
            print(end=' ')
        for k in range(st):
            print(end='*')
    
        if i==(num//2):
            flag=False
        if flag: 
            sp-=1
            st+=2
        else:
            sp+=1
            st-=2
                    
        print()
    num=int(input("계속 하시겠습니까?(0. 종료, 1.계속) : "))
    if num==0:
        break
