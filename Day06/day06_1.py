#<<아래 내용 토대로 프로그램 작성>>
# 1. 다음과 같은 메뉴와 가격을 key와 value로 사용하여
# 사전형 자료를 만들어 보세요 (변수명 menu)
# 칼국수(6000원), 비빔밥 (5500원), 돼지국밥(7000원),
# 돈까스(7000원), 김밥(2000원), 라면(2500원)
menu={'칼국수':6000,'비빔밥':5500,'돼지국밥':7000,
      '돈까스':7000,'김밥':2000,'라면':2500}
# 2. 위에서 만든 사전형 자료 menu 변수에서 가격이 6000원 미만에 
# 해당하는 메뉴와 가격을 출력하는 코드를 작성하세요.

for m,price in menu.items():
    if price<6000:
         print(m,price)
for me in menu:    
    if menu[me]<6000:
        print(f'{me}:{menu[me]}원')
# 3. 사용자 입력으로 메뉴와 가격을 입력받아 menu 변수에 자료를 
# 추가할 수 있도록 하시오.(동일한 메뉴는 가격만 변경)
add_menu=input("메뉴를 입력하세요 : ")
add_price=int(input("메뉴 가격을 입력해주세요 : "))
if add_menu in menu:
    menu[add_menu]=add_price
else:
    menu.update({add_menu:add_price})

# 4. 메뉴를 자동으로 선택하여 출력하게 만들어 보세요

sel=input('메뉴를 자동으로 출력하시겠습니까(Y/N)')
if sel=='Y' or sel !='N':
    for me in menu:
        print(me,menu[me],'원')
    print()

