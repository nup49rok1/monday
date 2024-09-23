#mymenu.py

import time
import sys 
#추가
from datetime import datetime  #기술하면 datetime.now()
#import datetime   #datetime.datetime.now() 형태로 작성

menu = dict()
flag = True
num,su,sel = 0,0,0
msg,info,message = '안내메','안내메','안내메'

#추가
# dt = datetime.now()
# print('처리날짜 ',datetime.now())
# print('처리날짜 ',dt)
# print()


#추가
def menuInsertNew():
    name = input('이름입력key>>>')#'cake'
    price = input('가격입력=value>>>')#700
    menu[name] = price
    print(name,'등록 성공했습니다.')

def menuAllprint():
    for k,v in menu.items() :
        print(k,' ',v)
    print()

def menuEditupdate():
    # print('key 조회후 키값이 있으면 수정 get()함수')
    name = input(' 편집대상 키값 입력>>>')
    if menu.get(name) == None:
        print('편집대상 딕트가 key 없습니다.')
    else:
        price = input('변경할 재입력value>>>')#700
        menu[name] = price
        print(name,'가격수정편집 성공했습니다.')

def menuDelete():
    name = input(' 삭제할 대상 키값 입력>>>')
    if menu.get(name) == None:
        print('삭제할 대상 딕트가 key 없습니다.')
    else:
        #삭제 pop del clear 전체삭제
        #menu.remove(name) 리스트의 삭제함수
        del menu[name] # 또는 menu.pop(name) ->리스트도 가능
        print(name,'정상적으로 삭제 성공했습니다.')
        time.sleep(0.3)
        #추가코딩 =>반복처리 때문에 함수로 작성해서 호출하는것 좋음
        for k,v in menu.items() :
            print(k,' ',v)

def menuFindsearch():
    key = input(' 조회대상 키값 입력>>>')
    if menu.get(key) == None:
        print(Key,'데이터가 없습니다.')
    else:
            #추가 코딩 해봄
        print(key,menu[key],'데이터 조회 성공했습니다.')

def menuExit():
    print('딕트처리를 종료합니다.')
    # flag = False
    sys.exit()

#----------------------------------------------------------
#----------------------------------------------------------

while flag:
    print()
    num=int(input('1.등록 2.출력 3.수정 4.삭제 5.조회 9.종료>>'))
    if num == 9: menuExit()
    elif num == 5: menuFindsearch()
        # key = input(' 조회대상 키값 입력>>>')
        # if menu.get(key) == None:
        #     print(Key,'데이터가 없습니다.')
        # else:
        #     #추가 코딩 해봄
        #     print(key,menu[key],'데이터 조회 성공했습니다.')
    elif num == 1: menuInsertNew()
    elif num == 2: menuAllprint()
    elif num == 3: menuEditupdate()
    elif num == 4: menuDelete()
    elif num == 5: menuFindsearch()
    else:print('처리번호를 잘못 입력하셨네요\n')
