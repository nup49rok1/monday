#game.py

# 전역변수 =>함수밖에 선언
# 300이상 문장이 되면 따로 메서드로 뽑아서 작성권장

user_id = 'kim'
user_pwd = '1234'

def terran():
    print('terran 함수')
    print('메딕')


def running():
    print()
    print('running 함수')
    print('조깅 마라톤')
    print('춘천 마라톤')
    print('서울 마라톤')
    km = 42.195 #지역변수
    return km

def LG(lg):
    print()
    print('LG함수')
    print(lg,'엘취')