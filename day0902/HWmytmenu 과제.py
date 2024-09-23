#HWmymenu과제.py

import time
import sys 
#추가
from datetime import datetime  #기술하면 datetime.now()
#import datetime   #datetime.datetime.now() 형태로 작성

# menu = dict()
# flag = True
# num,su,sel = 0,0,0
# msg,info,message = '안내메','안내메','안내메'
# #추가
# # path = 'c:\\Mtest\\menu.txt'
# path = 'c:/Mtest/menu.txt'

# 세번째 파일 path = 'c:\\Mtest\\menu.txt'
# 두번째 신규등록 menuInsertnew 할때만 일반 text 파일 저장

# 첫번째 HWmenu.py문서를 class화
flag = True

class EmpMenu:
    menu = dict()#dict객체 생성
    #flag = True
    num,su,sel = 0,0,0
    msg,info,message = '안내메','안내메','안내메'
    #추가
    path = 'C:/Mnet/menu.txt'
    i=1

    def __init__(self):
        pass

    def menuInsertNew(self):
        print('처음 self.i=>',self.i)
        name = input('이름입력key>>>')#'cake'
        price = input('가격입력=value>>>')#700
        self.menu[name] = price
        #추가
        self.menu['time'+str(self.i)] = datetime.now() #등록 시간 추가
        print(name,'등록 성공했습니다.')
        # key:value 데이터가 아닌 저장등록된 시간분 기록
        # import datetime
        #추가 코딩
        #path = 'c:/Mtest/menu.txt' 전역변수 또는 지역변수 상관없다.
        file = open(self.path,'a',encoding='UTF-8')
        # file.write(name+'['+price+']'+' time['+str(self.menu['time'+str(self.i)])+']'+'\n')
        file.write(name+'['+price+']'+' time'+str(self.i)+'['+str(self.menu['time'+str(self.i)])+']'+'\n')
        file.close()  #권장
        #추가
        self.i+=1
        print('나중 self.i=>',self.i)

    def menuAllprint(self):
        for k,v in self.menu.items() :
            # print(k,' ',v)
            print('k=>',self.menu[k],'v=>',self.menu[v])
        print()

    def menuEditupdate(self):
        # print('key 조회후 키값이 있으면 수정 get()함수')
        name = input(' 편집대상 키값 입력>>>')
        if self.menu.get(name) == None:
            print('편집대상 딕트가 key 없습니다.')
        else:
            price = input('변경할 재입력value>>>')#700
            self.menu[name] = price
            print(name,'가격수정편집 성공했습니다.')

    def menuDelete(self):
        name = input(' 삭제할 대상 키값 입력>>>')
        if self.menu.get(name) == None:
            print('삭제할 대상 딕트가 key 없습니다.')
        else:
            #삭제 pop del clear 전체삭제
            #menu.remove(name) 리스트의 삭제함수
            del self.menu[name] # 또는 menu.pop(name) ->리스트도 가능
            print(name,'정상적으로 삭제 성공했습니다.')
            time.sleep(0.3)
            #추가코딩 =>반복처리 때문에 함수로 작성해서 호출하는것 좋음
            for k,v in self.menu.items() :
                print(k,' ',v)

    def menuFindsearch(self):
        key = input(' 조회대상 키값 입력>>>')
        if self.menu.get(key) == None:
            print(key,'데이터가 없습니다.')
        else:
                #추가 코딩 해봄
            print(key,self.menu[key],'데이터 조회 성공했습니다.')

    def menuExit(self):
        print('딕트처리를 종료합니다.')
        # flag = False
        sys.exit()

    #추가
    def menuFileOpen(self):
        file = open(self.path,'r',encoding='UTF-8')
        data = file.read()# 전체 읽어 들이기
        print(data)
        file.close()  #권장

        # with open(path,'r',encoding='UTF-8') as file:
        #     pass

    def menuAllprint(self):
        for k,v in self.menu.items() :
            print(k,' ',v)
        print()

    def menuEditupdate(self):
        # print('key 조회후 키값이 있으면 수정 get()함수')
        name = input(' 편집대상 키값 입력>>>')
        if self.menu.get(name) == None:
            print('편집대상 딕트가 key 없습니다.')
        else:
            price = input('변경할 재입력value>>>')#700
            self.menu[name] = price
            print(name,'가격수정편집 성공했습니다.')

    def menuDelete(self):
        name = input(' 삭제할 대상 키값 입력>>>')
        if self.menu.get(name) == None:
            print('삭제할 대상 딕트가 key 없습니다.')
        else:
            #삭제 pop del clear 전체삭제
            #menu.remove(name) 리스트의 삭제함수
            del self.menu[name] # 또는 menu.pop(name) ->리스트도 가능
            print(name,'정상적으로 삭제 성공했습니다.')
            time.sleep(0.3)
            #추가코딩 =>반복처리 때문에 함수로 작성해서 호출하는것 좋음
            for k,v in self.menu.items() :
                print(k,' ',v)

    def menuFindsearch(self):
        key = input(' 조회대상 키값 입력>>>')
        if self.menu.get(key) == None:
            print(key,'데이터가 없습니다.')
        else:
                #추가 코딩 해봄
            print(key,self.menu[key],'데이터 조회 성공했습니다.')

    def menuExit(self):
        print('딕트처리를 종료합니다.')
        # flag = False
        sys.exit()

    #추가
    def menuFileOpen(self):
        file = open(self.path,'r',encoding='UTF-8')
        #추가
        data = file.read()
    # data = rfile.readline()
        print(data)
        file.close()  #권장

        # with open(path,'r',encoding='UTF-8') as file:
        #     pass
#----------------------------------------------------------
#----------------------------------------------------------
def Main():
    while flag:
        print()
            #6.파일열기추가
        num=int(input('1.등록 2.출력 3.수정 4.삭제 5.조회 6.파일열기 9.종료>>'))
        dictEmp = EmpMenu()
        if num == 9: 
            dictEmp.menuExit()
        elif num == 5: dictEmp.menuFindsearch()
                
        elif num == 1: dictEmp.menuInsertNew()
        elif num == 2: dictEmp.menuAllprint()
        elif num == 3: dictEmp.menuEditupdate()
        elif num == 4: dictEmp.menuDelete()
        elif num == 5: dictEmp.menuFindsearch()
            # 파일열기 추가 코딩
        elif num == 6: dictEmp.menuFileOpen()
        else:print('처리번호를 잘못 입력하셨네요\n')

Main()

'''

1.등록 2.출력 3.수정 4.삭제 5.조회 6.파일열기 9.종료>>1
이름입력key>>>홍길동
가격입력=value>>>200
홍길동 등록 성공했습니다.

1.등록 2.출력 3.수정 4.삭제 5.조회 6.파일열기 9.종료>>2
홍길동   200
time   2024-09-04 17:21:51.150999


1.등록 2.출력 3.수정 4.삭제 5.조회 6.파일열기 9.종료>>3
 편집대상 키값 입력>>>테스트
편집대상 딕트가 key 없습니다.

1.등록 2.출력 3.수정 4.삭제 5.조회 6.파일열기 9.종료>>3
 편집대상 키값 입력>>>홍길동
변경할 재입력value>>>9000
홍길동 가격수정편집 성공했습니다.

1.등록 2.출력 3.수정 4.삭제 5.조회 6.파일열기 9.종료>>2
홍길동   9000
time   2024-09-04 17:21:51.150999


1.등록 2.출력 3.수정 4.삭제 5.조회 6.파일열기 9.종료>>5
 조회대상 키값 입력>>>테스트
테스트 데이터가 없습니다.

1.등록 2.출력 3.수정 4.삭제 5.조회 6.파일열기 9.종료>>5
 조회대상 키값 입력>>>홍길동
홍길동 9000 데이터 조회 성공했습니다.

1.등록 2.출력 3.수정 4.삭제 5.조회 6.파일열기 9.종료>>6
홍길동[200] time[2024-09-04 17:21:51.150999]


1.등록 2.출력 3.수정 4.삭제 5.조회 6.파일열기 9.종료>>1
이름입력key>>>김길동
가격입력=value>>>500
김길동 등록 성공했습니다.

1.등록 2.출력 3.수정 4.삭제 5.조회 6.파일열기 9.종료>>2
홍길동   9000
time   2024-09-04 17:23:51.734320
김길동   500


1.등록 2.출력 3.수정 4.삭제 5.조회 6.파일열기 9.종료>>6
홍길동[200] time[2024-09-04 17:21:51.150999]
김길동[500] time[2024-09-04 17:23:51.734320]


1.등록 2.출력 3.수정 4.삭제 5.조회 6.파일열기 9.종료>>4
 삭제할 대상 키값 입력>>>홍길동
홍길동 정상적으로 삭제 성공했습니다.
time   2024-09-04 17:23:51.734320
김길동   500

1.등록 2.출력 3.수정 4.삭제 5.조회 6.파일열기 9.종료>

'''