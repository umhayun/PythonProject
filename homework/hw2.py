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
