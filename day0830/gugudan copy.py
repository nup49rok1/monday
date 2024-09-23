# gugudan.py

# 함수 4개작성
#  시작 진입 호출 main
#  main함수 toptitle()호출, guguinput(),guguoutput(),undertitle()호출
# 출력 time.sleep(1)
# 입력 input() 내장함수 이용, 형변환

from time import sleep,localtime #import time  사용 ->time.sleep(1)

def toptitle():
    print()
    print('mygugudan 처리 보고서')
    print('-' * 30)

def endtitle():
    print('-' * 30)
    print()

def guguinput():#입력받을시 예외처리 꼭 하기
    #잘못 입력을 할 수 있기에 초기값을 주기(반드시 리턴처리)
    dan = 1 # 지역변수
    try:
        dan = int(input('원하는 단입력>>'))
    except Exception as ex:
        print('에러이유 ',ex)
    return dan

def guguoutput(dan):#매개변수 O
    for k in range(1,10,1) :
        print(f'{dan}*{k}={dan*k}') 
        sleep(0.5) 

def main():
    #진입=시작
    toptitle()
    data=guguinput() #리턴값 필수 (입력받은 값을 받음)
    guguoutput(data) #매개인자
    endtitle()

# 진입함수 호출
main()
'''
dan = int(input('원하는 단입력>>')) #input('안내문') 문자형으로 인식
                                   #숫자로 변환해 줘야 된다.
for k in range(1,10,1) :
    #print(dan,'*',k,'=',(dan*k)) #문자를 숫자만큼 반복하게 된다.
    print(f'{dan}*{k}={dan*k}') #앞의 f를 빼면 액면그대로의 문자열 출력됨.
    time.sleep(0.5) 
'''