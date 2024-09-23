#03fileread.py

# 임포트 문장 X import file ~
# pathName = '경로/파일.txt'
# 리턴변수 = open('파일명',모드w/r/a, 인코딩)
# 리턴변수.close() 사용하는겻이 좋다. 직접 open()쓴 경우
# ff = open(1,2,3) 대체 =>  with open(1,2,3) as ff
                           # 리턴변수.close() 사용하지 않아도 OK
import time

#파일 읽기 처리 read()대신에 readline() 한라인씩 읽기
pathName = 'C:\Mnet/sample.txt'
rfile = open(pathName,'r',encoding='utf-8') #wfile->rfile
#추가
#data = rfile.read()
data = rfile.readline()# 한줄씩 처리 샘플.txt sample.txt 맨처음 한줄만 실행이 된다
print(data)
print('- ' * 50)
rfile.close()
time.sleep(0.5)
print(pathName, '파일 읽기에 성공했습니다.\n')
print()

time.sleep(2)
fileName = 'C:/Mnet/kakao.txt'
# wfile = open(pathName2,'a',encoding='utf-8')
# wfile.close() 권장
with open(fileName,'r',encoding='utf-8') as myfile: #파일변수
    # 권장 my = myfile.read() 전체 읽어서 출력
    my = myfile.readline() #한줄씩 처리
    while my != '': #공백이 아닐때까지  =>무한루프에 빠짐
        # print(my) 공백이 생김
        print(my,end='') #공백 제거
        my = myfile.readline()
 
    #wfile.close() # 추천 권장 =>with open(fileName,'a',encoding='utf-8') as myfile:
    # 생략 가능
    
print(fileName, '파일 읽기에 성공했습니다.\n')
print()
print()

'''
pathName = 'C:\Mnet/sample.txt'
aaaaa  nbnnnn  ccccc

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
C:\Mnet/sample.txt 파일 읽기에 성공했습니다.


aaaaaa      777777   8888888
카카오 파일 kakao.txt
김길동
34
홍대입구2
연습2
65
부산시
월요일 rain
break time
C:/Mnet/kakao.txt 파일 읽기에 성공했습니다.


'''
  