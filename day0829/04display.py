#04display.py
import time
#03play.py 파일 내용을 복사해서 작성한다.

# import 문서이름
  # 참조할때 game.user_pwd, game.terran()

# from 문서이름 import 전역변수,함수이름만 =>여러줄에 나눠어서 써도 된다.
# pdf파일 참조(모듈에서 찾아보기)

from game import user_id,user_pwd,terran
from game import LG,running 

print('04display.py')

print(user_id) 
print(user_pwd)

terran() 
LG('gram')

miter = running()
print('코스길이 ',miter)
print('코스길이2 ',running())

# game.py 불러오기
# 전역변수 user_id,user_pwd
# 함수 terran() LG(lg) running () 리턴값 있음
