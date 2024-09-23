#homeworkmilk.py (숙제 리스트 우유)

aprt = [
    [101,102,103,104],
    [201,202,203,204],
    [301,302,303,304],
    [401,402,403,404]

]
unpaid = [101,204,302,403]

for x in range(len(aprt)) :#3행을 가리킴 열갯수 고정임
    for y in range(len(aprt[x])) :#각행의 열의 갯수만큼 뽑아와서 k(열의 갯수)
        #if ss in data:
        #print(aprt[x][y],end =' \t') #행,열 출력
        if aprt[x][y] in unpaid:
            print(str(aprt[x][y])+'호 우유 배달 중지 X')
        else:
            print(str(aprt[x][y])+'호 우유 배달 계속 O')
    print()
#힌트 중첩 for

'''
for x ~~
    for y ~~
     if 조건 in unpaid
         우유배달 x
     else:
         우유배달 O
'''

#101호 우유 배달 중지 X
#102호 우유 배달 계속 O
#103호 우유 배달 계속 O
#104호 우유 배달 계속 O

#201호 우유 배달 계속 O
#202호 우유 배달 계속 O
#203호 우유 배달 계속 O
#204호 우유 배달 중지 X

#301호 우유 배달 계속 O
#302호 우유 배달 중지 X
#303호 우유 배달 계속 O
#304호 우유 배달 계속 O

#401호 우유 배달 계속 O
#402호 우유 배달 계속 O
#403호 우유 배달 중지 X
#404호 우유 배달 계속 O
