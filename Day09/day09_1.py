#Builtins 함수(내장함수)
##
# help()    #함수, 객체에 대한 설명 (도움말)
# print()   #터미널 화면에 결과 출력
# input()   #표준 입력으로 받은 결과 처리
# sum()     #인자값으로 여러개의 숫자를 받아서 합 계산 함수
# min()     #인자값들 중에서 가장 작은 수 반환
# max()     #인자값들 중에서 가장 큰 수 반환
# pow()     #인자값을 통해서 제곱 처리
# 내장함수들은 도움말(help) ->in module builtins...
#
# import ** : 모듈을 불러오는 명령어
# 
# import builtins
# dir(builtins) #내장 클래스, 내장 함수 보여줌
# 
# #
import builtins
# print(dir(builtins))

# 1.abs(x) : x를 대상으로 절대값 반환하는 함수
print(abs(10))
print(abs(-10))

# 2. all(iterable) : 모든 요소가 True면 True반환
list1=[1,3,4,7,-9,38]
list2=[0,1,2,3,4,5,7]
print(all(list1))
print(all(list2))

# 3. any(iterable) : 하나 이상의 요소가 True일때 True 반환
list3=[0,False,'',[]]
list4=[1,False,0,-15.3]
print(any(list3))
print(any(list4))

# 4. bin(number) : 10진수 정수를 2진수로 변환
#    oct(number) : 0o,hex(number)->0x

# 5. dir(x) : 객체 x에서 제공하는 변수, 내장함수, 내장클래스 목록 반환
# print(dir(list3))

# 6. eval(expr) : 문자열 수식을 인수로 받아 계산 가능한 파이썬 수식으로 변환
print(eval("10+20"))        #30
print(eval("10+20")+10)     #40

# 7. ord(character) : character를 아스키코드값(문자코드값) 으로 반환
# ' '->0x20(32), 0->0x30(48), A->0x41(65), a->0x61(97)
print(ord('0'))     #0x30(48)
print(ord('a'))
print(ord("A"))
print(ord('가'))

# 8. chr(number) : number는 코드값을 문자로 바꿔줌
print(chr(0x30))

# 9. pow(x,y) : x에 대한 y 제곱
print(pow(2,3))

# 10. round(number, 자리수) : 올림값 처리
print(round(3.141592))      #3
print(round(3.141592,3))    #3.142

# 11. sorted(iterable) : 반복 가능한 원소들을 오름차순 또는 내림차순으로 정렬 결과 반환

#12. zip(iterable*) : 반복 가능한 객체와 객체간의 원소들을 묵어서 튜플로 반환

zi=zip([1,3,5],[2,4,6])
print(list(zi))

