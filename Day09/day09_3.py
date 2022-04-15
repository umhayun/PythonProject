## 패키지 생성 후 사용하기 
# 패키지란? 여러 동작과 관련된 모듈을 모아 놓은 것을 의미함
# (패키지 생성 순서)
# 1. 패키지로 사용할 폴더 생성
# 2. 패키지 폴더에 묶어서 사용할 모듈 저장
# ([주의사항] python 3.3이하 버전에서는 폴더에 "__init__.py파일이 
# 생성되어야 합니다. 파일안에 내용이 없어도 상관 없음")
# 3. 패키지를 import명령어를 사용하여 불러옴
#   (패키지 폴더 이름이 바로 패키지명이 된다.)
#   from 패키지명 import 모듈명
# 
# #
from testpack import Sum,Sub,Mul,Div

print(Sum.Sum(100,200))
print(Sub.Sub(200,100))
print(Mul.Mul(100,2))
print(Div.Div(200,100))

### python 파일 입출력 사용
# - 디스크에 파일을 읽어 들이거나
# - 디스크에 파일을 생성하여 저장하는 기능 의미함.
# - 많은 양의 데이터를 처리(저장)할 때에 유용하게 사용됨
# ex) 홈페이지 이미지, 데이터, 음악, 파일 정보등을 저장할 때에...

# [과정-순서]
# 1. open함수를 이용하여 파일(객체)을 열기
# 2. read(읽기) 또는 write(쓰기) 관련 함수를 이용하여 파일에 대해서 작업
#    진행 및 처리 단계
# 3. open으로 열린 파일의 내용을 close함수를 사용하여 닫는다.
import os
print(os.getcwd())

'''
# 1. open함수를 이용하여 파일(객체)을 열기
file=open("Day09/data/test_text.txt",mode='a',encoding='utf-8')
#/data/test_text.txt 파일에 대한 fileIO생성...


# "a"=>모드 영역
# open 함수 사용시 모드 설정 값
# r(read-읽기) => 파일이 있는 경우, 해당 파일에 대해 읽기 동작 실행
#                 파일이 없는 경우, 에러 출력 (File Not Found!!)
# w(write-쓰기) => 파일이 있는 경우, 파일에 있는 내용을 삭제 후 새롭게 쓰기
#                  파일이 없는 경우, 파일을 생성하고 쓰기 진행
# a(append-추가) => 파일이 있는 경우, 파일에 마지막에 추가로 쓰기 작업 진행
#                   파일이 없는 경우, 파일 생성하고 쓰기 진행
# x             => 파일이 있는 경우, 생성 에러 발생
#                  파일이 없는 경우 파일 생성하고 쓰기 진행
# Mode에 "+"를 사용하는 경우, 추가기능이 사용됨(읽기 쓰기 가능)
# 모드에 t=>text작업, b=>binary 작업
# -encoding : 문자 설정


# 2. open으로 생성된 내용을 토대로 작업 진행
str1=input("파일에 저장할 내용을 입력 : ")
i=file.write(str1)
print("file.write()의 반환 값: ",i)

# 3. 작업한 파일의 내용을 close()로 종료
file.close()

'''

'''
##파일 읽기
# 1.open
rfile=open("Day09/data/test_text.txt",'r',encoding="utf-8")
# 2.작업
readbuffer=rfile.read()
print(readbuffer)
#3. close
rfile.close()


'''
'''
Quiz 파일명 : data/quiz1.txt
1. 본인의 인적사항을 파일에 저장후에 출력하세요.
(이름,나이,주소)
- 당신의이름 : 
- 홍길동님의 나이는 : 
- 홍길동님의 주소는 : 
[출력결과]=>파일에 저장된결과 출력
홍길동
20살
산골짜기
'''
'''
# 1.open
file=open("Day09/data/quiz1.txt",'a',encoding="utf-8")
# 2. work
name=input("당신의 이름 : ")
age=input(f"{name}님의 나이는 : ")
addr=input(f"{name}님의 주소는 : ")
file.write(name+"\n"+age+"\n"+addr+"\n")
# 3. close
file.close()

##파일 출력
rfile=open("Day09/data/quiz1.txt",encoding="utf8")
buf=rfile.read()
print(buf)
file.close()

#예제2] readline() =>데이터를 읽어들일때에 "\n"을 기준으로
#데이터를 읽어들이는 함수
rfile2=open("Day09/data/quiz1.txt",'r',encoding='utf8')
while True:
    readbuffer=rfile2.readline()
    if readbuffer=="":
        print("\n더이상 값이 존재하지 않습니다.")
        rfile2.close
        break
    print(readbuffer,end='')
'''
#예제3] readlines()=> "\n"을 기준으로 데이터를 읽어들이는 함수,
#읽어들인 문장들은 리스트에 저장하는 함수

rfile3=open("Day09/data/quiz1.txt",'r',encoding="utf8")
buf3=rfile3.readlines()
print(buf3,type(buf3))
rfile3.close()
print()
#문자열 리스트에 "\n"을 제거하여 저장
buf4=[]
for i in buf3:
    buf=i.replace("\n","")
    buf4.append(buf)
print(buf4)

