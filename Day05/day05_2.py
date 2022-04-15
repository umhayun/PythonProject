#문제3 lst_sec=[['홍길동','남',36],['김수양','여',32],['박담수','남',28]]
# 아래 형태로 출력
# 이름: 홍길동
# 성별: 남
# 나이: 36
lst_sec=[['홍길동','남',36],['김수양','여',32],['박담수','남',28]]
for i in range(len(lst_sec)):
    for j in range(len(lst_sec[i])):
        if j==0:
            print('이름 : ',lst_sec[i][j])
        elif j==1:
            print('성별 : ',lst_sec[i][j])
        else:
            print('나이 : ',lst_sec[i][j])
    print()

#문제4  구구단 출력 코드 2차 리스트에 결과값 저장하고 출력
gugu=[]
for x in range(2,10):
    gugu.append([])
    for y in range(1,10):
        gugu[x-2].append(x*y)
#print(gugu)
for x in range(2,10):
    for y in range(1,10):
        print(f'{x} x {y} = {gugu[x-2][y-1]}',end=' ')
    print()
    
#=========================================================

### list 내포 (List Comprehension) : 리스트 안에서 for와 if를 사용하는 문법
    
# 형식1 (for)
# 변수 =[실행문 for 변수 in 열거형 객체]
# for문의 실행결과가 변수 리스트네 append처리가 되어진다.
    
x=[2,4,1,5,7]
y=[xy**2 for xy in x ]
print(y)        #[4,16,1,25,49]
    
# 형식2 (for와 if를 같이 사용하는 경우)
#   변수=[실행문 for 변수 in 열거형객체 if 조건문]
# 형식2 : 1~10 -> 2의 배수 추출 -> i*2 ->list에 저장
num=list(range(1,11))
list2=[i*2 for i in num if i%2==0]
print(list2)        #[4,8,12,16,20]



'''
위에서 학습한 내용을 토대로 다음과 같은 내용을 프로그램 하세요
아래와 같은 메뉴를 만들고, 친구 이름을 관리하는 코드 작성
(리스트 사용)
---------------------------
1. 친구 리스트 출력         #등록한 친구 목록 보기
2. 친구 추가                #친구 등록하기(정보는 문제 3번 참조)
3. 친구 삭제                #등록친구 삭제
4. 이름 변경                #이름 변경
0. 종료                     #프로그램 종료
메뉴를 선택하세요 : 2
이름을 임력하시오 : 홍길동
'''
# import os
# os.getcwd()
# choice=1
# friend=[]
# while choice!=0:
    
#     os.system('cls')
#     print(' 1. 친구 리스트 출력','\n',
#           '2. 친구 추가','\n',
#           '3. 친구 삭제','\n',
#           '4. 이름 변경','\n',
#           '0. 종료')
#     choice=int(input("메뉴 선택 : "))
#     if choice==1:
#         print(friend)
#     elif choice==2:
#         friend.append(input("이름을 입력하시오 :"))
#     elif choice==3:
#         friend.remove(input('삭제할 친구를 입력하시오 : '))
#     elif choice==4:
#         name=input('변경이 필요한 친구 이름을 입력하시오 : ')
#         new=input('변경할 이름을 입력하시오 : ')
#         idx=friend.index(name)
#         friend[idx]=new
    
    
    

