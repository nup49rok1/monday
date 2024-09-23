# homeworkcoffee.py

money,sel = 0,9

money = int(input('금액입력 >>>')) #600 or 500 입력해서 실습테스트
#jandong = 0

while True:
    print('\n-------커피 머신-------')
    print(' ')
    data = int(input('1.커피(250) 2.코코아(200) 3.변환  9:종료>>> '))
    sel = int(data)
    #if~elif~if 제어문 (커피값 계산)
    if sel == 9 :
        break
    #커피 주문
    elif sel == 1:
        if (money > 0 and money >= 250) :
            money-=250
            print('커피 성공,잔액은 '+str(money)+'원 남았습니다.')
        else:
            print('잔액 부족으로 커피 주문은 할 수 없습니다.')

    #코코아 주문    
    elif sel == 2:
        if (money > 0 and money >= 200) :
            money-=200
            print('코코아 성공,잔액은 '+str(money)+'원 남았습니다.')
        else:
            print('잔액부족으로 코코아주문은 할 수 없습니다.')
     
    elif sel == 3:
        pass
    
    else :
        print('주문번호를 정확히 선택하세요')

print()
print('현재 잔액은 ', money , '입니다.')
