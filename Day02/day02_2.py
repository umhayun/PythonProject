# 제어문(if), 반복문 (for,while)
# 제어문(if)
# 
# 단순 if
#   사용형식1
# if 조건식 :
#       실행문
#       실행문
# 특징 : 조건식이 참일 경우에 종속 문장 실행
#       파이썬에서 다른 언어와 다르게 들여쓰기 중요
#       들여쓰기를 가지고 블럭 구분
# #

#[예제]
# num=int(input("정수 입력 : "))
# if num%2==0:
#     print("num변수의 값 짝수")
#     print("num 변수의 값은 2의 배수")
# print("if 다음 문장 실행")

'''
if문 문제
1. 입력한 데이터가 3의 배수인 경우 출력
2. 절대값을 구하는 프로그램 작성
3. 수를 입력받아 짝홀수 구분 출력
4. 두 수 입력받아 큰수 출력
5. 세수 입력 받아 큰수 출력
6. 두수 입력받아 큰수가 짝수면 출력
7. 두수 입력받아 합이 짝수이고 3의 배수인 수 출력

''' 
#1
num1=int(input("정수 입력 : "))
if num1%3==0:
    print("정수는 3의배수입니다.")
else:
    print("3의 배수가 아닙니다.")
#2
num2=int(input("실수 입력 : "))
if num2<0:
    num2=-num2
print(f"절대값 : {num2}")

#3
num3=int(input("정수 입력 : "))
if num3%2==0:
    print("짝수입니다.")
else:
    print("홀수입니다.")
    
#4
n4=int(input("정수 입력 : "))
n5=int(input("정수 입력 : "))
if n4>n5:
    print(f"{n4}가 {n5}보다 크다")
elif n4==n5:
    print("두수가 같다.")
else:
    print(f"{n5}가 {n4}보다 크다")
    
#5
n6=int(input("정수 입력 : "))
n7=int(input("정수 입력 : "))
n8=int(input("정수 입력 : "))

if n6>n7 and n6<n8:
    print("제일큰수 : ",n6)
if n7>n6 and n7>n8:
    print("제일큰수 : ",n7)
if n8>n6 and n8>n7:
    print("제일큰수 : ",n8)
    
    
'''
Quiz
 - 사용자로부터 Gbyte값을 받아 byte, Kbyte, Mbyte로 각각 출력
 -(1, byte 2.Kbyte 3.Mbyte 선택)
 단위 1024
'''
choice=int(input("변환하고싶은 단위입력(1, byte 2.Kbyte 3.Mbyte 선택) :  "))
g=int(input("Gbyte입력 : "))
m=g*1024
k=g*1024**2
b=g*1024**3
if choice==3:
    print(m,"mbyte")
elif choice==2:
    print(k,"kbyte")
else:
    print(b,"byte")
'''
Quiz2
인증 프로그램 만들기
1. 아이디가 틀리면 등록되지 않은 아이디 출력
2. 비밀번호가 틀리면 '비밀번호 비일치' 출력
3. 아이디와 비밀번호 일치하면 인증 통과

'''
old_id='test' 
old_pw='python123'

print("인증 프로그램 시작")
new_id=input("id입력 : ")
new_pw=input("pw입력 : ")
if new_id!=old_id:
    print("등록된 아이디가 없습니다.")
else:
    if new_pw==old_pw:
        print("인증 통과")
    else:
        print("비밀번호 불일치")
        
