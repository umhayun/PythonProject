
# [문제1] 윤년 구하기

'''
    윤년 구하는 코드 작성
    4의 배수는 윤년이 된다.그 외는 평년
    4의 배수면서 100의 배수인 경우는 평년이다. 그외는 윤년
    4그리고 100의배수이면서 400의 배수인 경우 윤년이다. 그외 평년
    출력예제:2017은 평년입니다.
'''
# year=int(input('연도를 입력하세요 : '))
# if year%4==0:
#     if year%100==0:
#         yun='평년'
#         if year%400==0:
#             yun='윤년'
#     else:
#         yun='윤년'
# else:
#     yun='평년'
    
# print(f'{year}은 {yun}입니다.')
'''
    문제2
    이름,학번,3과목의 성적을 입력받아 합계와 평균을 구하고,
    평균이 90이상이면 A 80이상이면 B, 70이상이면 C, 60이상이면 D, 60미만이면 F
'''

# name=input("이름 입력 : ")
# num=input("학번 입력 : ")
# score1=int(input("점수 입력 : "))
# score2=int(input("점수 입력 : "))
# score3=int(input("점수 입력 : "))
# sum=score1+score2+score3
# avg=sum/3;
# print('합계 : ', sum,"평균",avg)
# if avg>=90:
#     grade='A'
# elif avg>=80:
#     grade='B'
# elif avg>=70:
#     grade='C'
# elif avg>60:
#     grade='D'
# else:
#     grade='F'
# print(f"{name}학생은 {grade}입니다.")

'''
    문제3
    커피 개당 2000원 10개 초과하면 초과양에대해서만 1500원
    커피개수 입력받아 금액 출력
'''
# coffee=int(input("커피 개수를 입력하세요 : "))
# if coffee<=10:
#     sum=coffee*2000
# else:
#     sum=(coffee-10)*1500+10*2000
# print(f'커피값은 {sum} 입니다.')
'''
    문제4
    정수 입력받아 출력
    3의배수이면서 4의배수
    3의배수
    4의배수
    3의배수도 4의배수도 아님
    0은 3의배수도 4의배수도 아닙니다.
'''
#다중 if문을 사용하여 여러 조건식을 볼 경우에
#범위가 작은 조건식 먼저 정의
# num=int(input('정수를 입력하세요 : '))
# if num%3==0 and num%4==0:
#     c="3의배수이면서 4의배수"
# else:
#     if num%3==0:
#         c='3의배수'
#     elif num%4==0:
#         c='4의 배수'
#     else:
#         c='3의배수도 4의배수도아니다.'
# print(c)

'''
for 구문
:가장 대표적인 반복 구문 중 하나로 
주어진 조건에 따른 회차만큼 반복

(형식)
for 변수명 in range(반복 횟수): 
    종속 문장 1(for)
    종속문장2(for)
    (메인 프로그램 실행 코드 진행)
'''

#range(시작,끝,증감) : 파이썬 내장 함수
'''
사용법(range())
1.range(종료값) #시작 0 증감 +1 기본값 생략
 : 0부터 시작해서 종료값 이전까지의 값의 범위 가짐
 ex)range(10) =>[0,1,2,3,4,5,6,7,8,9]
2. range (시작값, 종료값)
  : 시작값 부터 종료값 이전까지의 값의 범위
  ex)range(5,10) =>[5,6,7,8,9]
3. range(시작,종료,증감)
  : 시작값부터 종료값 이전까지 증/감 값 간격 범위
  ex)range(0,10,2)=> [0,2,4,6,8]
  ex)range(10,0,-2) =>[10,8,6,4,2]
'''
#for문 구구단
for x in range(2,10,1):
    for y in range(1,10,1):
        print(f"{x}x{y}={x*y}",end='\t')
    print("\n")

#문제3
# 0  0  0  0  0
# 0  1  2  3  4
# 0  2  4  6  8
# 0  3  6  9  12
# 0  4  8  12  16  
for x in range(0,5,1):
    for y in range(0,5,1):
        print(f"{x*y}",end='\t')
    print()
print("\n")       
#문제 4
# 1 2 3 4 5
# 6 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20
# 21 22 23 24 25
# 26 27 28 29 30
for b in range(0,26,5):
    for a in range(1,6,1):
        print(a+b,end='\t')
    print()
        
print("\n")       
#5
# 25      24      23      22      21
# 20      19      18      17      16
# 15      14      13      12      11
# 10      9       8       7       6
# 5       4       3       2       1    
for x in range(5,0,-1):
    for y in range(5):
        print(x*5-y,end="\t")
    print()
print()
print("\n")
#6
# 1       2       3       4       5
# 2       3       4       5       1
# 3       4       5       1       2
# 4       5       1       2       3
# 5       1       2       3       4
for x in range(5):
    for y in range(5):
        print((x+y)%5+1,end='\t')
    print()
print() 