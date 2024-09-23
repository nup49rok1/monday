#05ospath.py

# 임포트 문장 X import file ~
# pathName = '경로/파일.txt'
# 리턴변수 = open('파일명',모드w/r/a, 인코딩)
# 리턴변수.close() 사용하는겻이 좋다. 직접 open()쓴 경우
# ff = open(1,2,3) 대체 =>  with open(1,2,3) as ff
                           # 리턴변수.close() 사용하지 않아도 OK

# 파일 읽기 read() ,readline() ,readlines()

import sys
import os.path 


save_path = os.path.abspath('C:/Mnet/my.txt') #abspath(절대경로)
try:
    if not os.path.exists(save_path): #경로에 파일이 있는지 체크할때
        print(save_path, '대상 파일이 존재하지 않습니다.')
        #sys.exit() # 프로그램 종료
    else:
        pass #파일없으면 에러메세지 처리
except Exception as EX:
    print('에러이유 확인',EX)


print()


'''
C:\Mnet\my.txt 대상 파일이 존재하지 않습니다.
 
'''