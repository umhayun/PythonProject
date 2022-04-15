#2장 4번
# 3개의 단어를 키보드로 입력 받아서 각 단어의 첫글자를 추출하여 단어의 약자를 출력하세요

# word1=input("첫번째 단어 : ")
# word2=input("두번째 단어 : ")
# word3=input("세번째 단어 : ")
# word=word1[0]+word2[0]+word3[0]

# print(f"약자 : {word}")


# #3장
# #문제1
# #A형
# kg=int(input("짐의 무게는 얼마입니까?(kg) : "))
# if kg<10:
#     print("수수료는 없습니다.")
# elif kg>=10:
#     print("수수료는 10,000입니다.")
# #B형
# kg2=int(input("짐의 무게는 얼마입니까?(kg) : "))
# n=kg2//10
# if kg2<10:
#     print("수수료는 없습니다.")
# elif kg2>=10:
#     print(f"수수료는 {n*10000}입니다.")
    
# #문제2 while문 이용한 숫자 맞추기 게임

# from random import randint

# print("<<숫자 맞추기 게임>>")
# com=randint(1,10)
# while True:
#     my=int(input("숫자를 입력하시오 : "))
#     if my<com:
#         print("업")
#     elif my>com:
#         print("다운")
#     else:
#         print("정답")
#         break
    
# #문제3

# s=0
# for num in range(1,101):
#     if num%3==0 and num%2==1:
#         print(num,end=" ")
#         s+=num

# print("누적합=",s)

# #문제4

# multiline="안녕하세요. 파이썬 세계로 오신걸 환영합니다. 파이썬은 비단뱀 처럼 매력적인 언어입니다."

# count=0
# for w in multiline:
#     print(w,end="")
#     if w==' ':
#         print()
#         count+=1
# print("단어 개수 : ",count)

# #4장
# #문제1
# lst=[10,1,5,2]
# result=lst*2
# print("단계 1 : ",result)
# result.append(lst[0]*2)
# print("단계 2 : ",result)
# result2=result[1::2]
# print("단계 3 : ",result2)

#문제2
#A형
l=int(input("vector 수 : "))
list=[]
for p in range(l):
    el=int(input())
    list.append(el)
print("vector의 크기 : ",len(list))

#B형
l2=int(input("vector 수 : "))
list2=[]
for p in range(l2):
    el2=int(input())
    list2.append(el2)
find=int(input("찾을 값 : "))
if find in list2:
    print("YES")
else:
    print("NO")
