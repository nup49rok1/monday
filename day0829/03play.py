#03play.py

import time #시간차 두기
import game #물리적인 파일이름만 명시

print('03play.py')
time.sleep(1)

print(game.user_id) #파일명.전역변수명
print(game.user_pwd)

time.sleep(1)
game.terran() #파일명.호출함수명()

time.sleep(1)
game.LG('gram')

time.sleep(1)
miter = game.running()
print('코스길이 ',miter)
print('코스길이2 ',game.running())

# game.py 불러오기
# 전역변수 user_id,user_pwd
# 함수 terran() LG(lg) running () 리턴값 있음
'''
03play.py
kim
1234
terran 함수
메딕
'''







print()