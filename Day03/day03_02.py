# while구문
# : 조건식이 참인 경우에 반복하는 반복문
# (형식)
# while (조건식) : 
#       종속문장
#       종속문장
# (메인 프로그램 코드 실행)
# 
'''
문제1]
쌀 100통이 저장되어 있는 창고에 암수 1쌍의 쥐가 있습니다.
쥐 한마리가 하루20g씩 쌀을 먹고 있습니다.
10일마다 쥐의 수가 2배 증가하고 있다면,
며칠만에 창고의 쌀이 모두 쥐의 먹이가  될까?
또, 이때에 쥐는 총 몇마리가 되어 있을까?
(쌀 한통은 1kg, 쥐는 쌀을 먹은 후 2배로 증가하는 조건)
'''
rice=100*1000
mouse=2
day=1
while True:
    rice-=mouse*20
    if day%10==0:
        mouse*=2
    if rice<=0:
        break
    day+=1
print(f"{day}일 만에 쥐는 {mouse}마리") 

#문제2] 1~100까지 합
n=1
sum=0
while n<=100:
    sum+=n
    n+=1
print("1~100합 : ",sum)
# 문제3] 1부터 1씩 증가하는 값에 대해 누적합 구할 때 10,000보다
# 큰 누적합 값에 대해 마지막에 더해진 값이 얼마인지 구하시오
n2=1
sum2=0
while True:
    sum2+=n2
    if sum2>10000:
        break
    n2+=1
print(sum2)
print('마지막 으로 더해진 값 : ',n2)


# 문제4]1부터 100사이의 소수(prime number)를 출력하고 개수를 구하시오
# bool형 자료를 이용한 알고리즘
count=0
for x in range(2,101):
    flag=True #flag가 True면 소수
    for y in range(2,x):
        if x%y==0:
            flag=False
            break
    if flag:
        count+=1
        print(x,end=' ')
print('1~100사이 소수 개수 : ',count)