#09dictmenu.py
# 예외처리 try: ~~except:~~ 생략

import time
import sys #프로그램 종료 sys.exit()

menu = dict()
flag = True
num,su,sel = 0,0,0
msg,info,message = '안내메','안내메','안내메'


while flag:
    print()
    num=int(input('1.등록 2.출력 3.수정 4.삭제 5.조회 9.종료>>'))
    if num == 9:
        print('딕트처리를 종료합니다.')
        # break 해도 된다.
        #flag = False
        sys.exit() #프로그램 종료
    #elif num == '1': 문자로 인식이 되기때문에 주의 할것.
    elif num == 1: #딕트 등록 mysite[200] = 'kakao'
        name = input('이름입력key>>>')#'cake'
        price = input('가격입력=value>>>')#700
        menu[name] = price
        print(name,'등록 성공했습니다.')
    elif num == 2: # 딕트 전체 출력 for 반복문 권장
        for k,v in menu.items() :
            print(k,' ',v)
        print()
    elif num == 3:#딕트 편집 처리 가격대상 value 변경
        # print('key 조회후 키값이 있으면 수정 get()함수')
        name = input(' 편집대상 키값 입력>>>')
        if menu.get(name) == None:
            print('편집대상 딕트가 key 없습니다.')
        else:
            #추가 코딩 해봄
            price = input('변경할 재입력value>>>')#700
            menu[name] = price
            print(name,'가격수정편집 성공했습니다.')
    elif num == 4:#삭제
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
    elif num == 5: #조회(한건만 = 본인)
        key = input(' 조회대상 키값 입력>>>')
        if menu.get(key) == None:
            print(Key,'데이터가 없습니다.')
        else:
            #추가 코딩 해봄
            print(key,menu[key],'데이터 조회 성공했습니다.')
    else:
        pass
        print('처리번호를 잘못 입력하셨네요\n')


print()


# 사용자정의 함수
# 클래스
# 파일처리 - 파일저장,파일열기
# 예외처리
# ㄴ C = 추가 신규 등록 create(insert=add)
# ㄴ R read 읽기 update 수정 delete 삭제

# mysite = dict() # 100k : 네이버 v 200k : 카카오 v

# mysite[100] = 'naver'
# mysite[200] = 'kakao'
# #추가코딩
# mysite[300] = 'apple'

# for i,k in enumerate(mysite):
#     print(i,k,' ',mysite[k])

# 등록 # 100k : 네이버 v 200k : 카카오 v
# 출력 items(), enumerate(mysite)
# 수정 100:네이버 => 100: 에이콘
# 키값 조회
'''
0 100   naver
1 200   kakao
'''
# mysite[100] = '에이콘'
# print()

# for k,v in mysite.items() :
#     print(k,' ',v)
'''
0 100   naver
1 200   kakao

100   에이콘
200   kakao
'''
# print()
# #print(mysite[210]) #mysite[키명(200)] =>없는키를 쓰면 에러발생
# #print(mysite.get()) #TypeError: get expected at least 1 argument, got 0
# print(mysite.get(210)) #에러대신 None 출력이 된다.
# print( 210 in mysite)  #에러대신 False 출력이 된다.

print()