# match~case 구문 : 파이썬 3.10.0 이후에 도입...
# 다른 언어의 switch~case구문과 같은 동작
# 예제1
'''
def num_chk(st):
    match st:
        case 1 :
            return '일'
        case 2 :
            return '이'
        case 3 : 
            return '삼'
        case _ :
            return '선택범위를 벗어났습니다.'

st=1
wh=num_chk(st)
print(wh)     
'''
#예제
'''
def alpha_chk2(chk):
    match chk:
        case 'a'|'A':
            return 'A'
        case 'b'|'B':
            return 'B'
        case 'c'|'C':
            return 'C'
        case _:
            return 'A~C이외의 알파벳'

alpha=input('A~C사이 알파벳 입력 : ')
print('입력한 알파벳은 :',alpha_chk2(alpha))
'''
# 연습 : 국가명을 입력받아 해당 국가 번호를 출력 함수 구현
# 01 -unitedstate 33-france, 34-spain, 81-japan,82-korea
#코드가 없는 경우에는 -1을 반환값으로 하는 getPhoneCode() 구현

#(ex) getPhoneCode('southkorea')->82(대소문자 구분x)
#math~case문 사용
'''
def getPhoneCode(country):
    match country:
        case 'unitedstate':
            return 1
        case 'france':
            return 33
        case 'spain':
            return 34
        case 'japan':
            return 81
        case 'southkorea':
            return 82
        case _:
            return -1

coun=input('나라이름 영어로 입력 : ')
country=coun.lower()
num=getPhoneCode(country)
print(country,'의 국가 번호는 ',num,'입니다.')
'''

