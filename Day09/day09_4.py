#암호화
'''
readstr,content="",""
key=100     #암호화 연산을위한 값
choice=input("1. 파일 저장 \n2. 파일 불러오기\n번호선택>> ")
fileName=input("파일명 입력 : ")
if choice=='1':
    content=input("단일 문자 입력 : ")
    # 1.open
    sfile=open("Day09/data/"+fileName,'w',encoding="utf8")
    #2. 작업
    chNum=ord(content)
    chNum=chNum+key
    content=chr(chNum)
    sfile.write(content)
    # 3. close
    sfile.close()
elif choice=='2':
    rfile=open("Day09/data/"+fileName,'r',encoding="utf8")
    readstr=rfile.read()
    chNum=ord(readstr)
    chNum=chNum-key
    readstr=chr(chNum)
    print("파일에 지정된 값 : ",readstr)
    rfile.close()
'''
# [문제1]
#  위 예제를 이용하여 문자열을 암호화 시켜주세요
#  - 현재 단일 문자만 저장 가능
#  - 문자열을 암호화하여 파일에 저장할 수 있도록 코드 수정
#  - 반대로 암호화된 문자열복호화 하여 화면에 출력할 수 있도록 코드 수정

#풀어보기
'''
while True:
    readstr1,content1="",""
    choice1=input("1. 파일 저장 \n2. 파일 불러오기\n번호선택>> ")
    fileName1=input("파일명 입력 : ")
    key=100
    if choice1=='1':
        content1=input("문자열 입력 : ")
        # 1.open
        sfile1=open("Day09/data/"+fileName1,'w',encoding="utf8")
        # 2. 작업
        content2=''
        for i in content1:
            chNum1=ord(i)
            chNum1+=key
            i=chr(chNum1)
            content2+=i
        sfile1.write(content2)
        # 3. close
        sfile1.close()
    elif choice1=='2':
        rfile1=open("Day09/data/"+fileName1,'r',encoding="utf8")
        content3=rfile1.read()
        for i in content3:
            chNum1=ord(i)
            chNum1=chNum1-key
            i=chr(chNum1)
            readstr1+=i
        print("파일에 지정된 값 : ",readstr1)
        rfile1.close()
    re=input('계속하시겠습니까 (y/n)')
    if re=='n':
        break
'''


# [문제2]
# 위 내용을 이용하여 문서 파일에 저장할 입력 내용을 암호화 시켜주세요
# - 문자열을 암호화하여 파일에 저장할 수 있도록 코드 수정
# - (문자열을 반복적으로 입력할수 있게 만들어서 처리후 암호화)
# - 반대로 암호화된 문자열을 복호화하여 화면에 출력할 수 있도록 코드 수정
'''
while True:
    readstr1,content1="",""
    content2=''
    choice1=input("1. 파일 저장 \n2. 파일 불러오기\n번호선택>> ")
    fileName1=input("파일명 입력 : ")
    key=100
    if choice1=='1':
        content1=input("문자열 입력 : ")
        # 1.open
        sfile1=open("Day09/data/"+fileName1,'a',encoding="utf8")
        # 2. 작업
        
        while True:
            for i in content1:
                chNum1=ord(i)
                chNum1+=key
                i=chr(chNum1)
                content2+=i
            content2+="\n"
            sel=input("문자열 입력을 계속 하시겠습니까? (y/n) : ")
            if sel=='n':
                sfile1.write(content2)
                sfile1.close()
                break
            
            
    elif choice1=='2':
        rfile1=open("Day09/data/"+fileName1,'r',encoding="utf8") 
        while True:
            content3=rfile1.readline()
            if content3=="":
                rfile.close()
                break
            for i in content3:
                chNum1=ord(i)
                chNum1=chNum1-key
                i=chr(chNum1)
                readstr1+=i

            print("파일에 지정된 값 : ",readstr1)
            rfile1.close()
    re=input('계속하시겠습니까 (y/n)')
    if re=='n':
        break
'''  

#open()모드에 '+'옵션 사용하기
'''
fileName=input('파일명 입력 : ')
file=open(fileName,'r+',encoding='utf8')    #r에 +붙이면 읽기쓰기 동시발생
readstr=file.read()
print(readstr,end='')
writestr=input('\n문서에 추가할 내용을 입력하세요 : ')
file.write(writestr+'\n')
file.close()
'''
#모드 옵션
#t=>텍스트(문서) =>생략가능
#b=>바이너리(2진데이터)

#문제] file입출력을 이용하여 "특정 파일"을 복사하는 프로그램 코드 작성

#복사할 대상(원본) :Day09/data/test.jpg
#복사할 위치(복사본) :Day09/data/test_copy.jpg

org=input('복사할 대상 : ')
new=input('복사할 위치 : ')

file=open(org,'rb')
img=file.read()
file2=open(new,'wb')
file2.write(img)
file.close()
file2.close()