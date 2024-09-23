#HWpickle.py

# open(1파일명,모드wb/rb(binary),인코딩)
# dump 쓰기/load 읽기
# 피클로 파일처리 import 

import pickle
import time
import sys
import os.path

path = 'c:/Mnet/myCalendar.txt' #확장자는 자기 마음대로 작성이 가능
#txt파일이지만 pickle로 저장했기때문에 탐색기에서 파일을 열어봤을때 깨져서 보임
#문서를 보호하고 있기때문이다.

while True:
    print()
    num = int(input('1.스케줄 기록 2.스케줄 읽기 9.종료>>>'))

    if num==1: #피클.dump()
        file = open(path,'ab') #wb->ab로 변경
        #추가
        memo = input("할일 입력 ")
        pickle.dump(memo,file)

        file.close()
        print(path,'피클 저장기록처리 성공했습니다.') #12:50 점심식사
    elif num==2: #피클.load()
        file = open(path,'rb')
        #추가
        data = pickle.load(file)
        print(data)

        file.close()
        print(path,'피클 오픈읽기처리 성공했습니다.')
    elif num==9:
        print('스케줄 피클처리 종료합니다.')
        sys.exit()
    else:
        print('작업번호 오류입니다.')

#
print()

'''
1.스케줄 기록 2.스케줄 읽기 9.종료>>>1
할일 입력 12:50 점심식사
c:/Mnet/myCalendar.txt 피클 저장기록처리 성공했습니다.

1.스케줄 기록 2.스케줄 읽기 9.종료>>>1
할일 입력 2:45 친구미팅
c:/Mnet/myCalendar.txt 피클 저장기록처리 성공했습니다


1.스케줄 기록 2.스케줄 읽기 9.종료>>>2
2:45 친구미팅
c:/Mnet/myCalendar.txt 피클 오픈읽기처리 성공했습니다. =>마지막 자료만 보임
=>단점 =>탐색기에서 지금 피클로 만든 데이터를 삭제시킴(myCalendar.txt)

'''
