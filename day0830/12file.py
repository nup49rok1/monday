#12file.py

# 리턴변수 = open('파일명',모드w/r/a, 인코딩)
# 리턴변수.close()
# 임포트 문장 없어요
import time

pathName = 'C:\Mnet/sample.txt'
wfile = open(pathName,'a',encoding='utf-8')
name = input('이름입력 >>> ')
age = input('나이입력 >>> ')
juso = input('주소입력 >>> ')

#자동 줄바꿈이 안되기에 뒤에 라인개행문자 써줌.
wfile.write(name + '\n')
wfile.write(age + '\n')
wfile.write(juso + '\n')
wfile.close() # 추천 권장

time.sleep(0.5)
print(pathName, '파일 저장에 성공했습니다.')
print()

print('--'*70)
time.sleep(1)
pathName2 = 'C:/Mnet/sample2.txt'
# wfile = open(pathName2,'a',encoding='utf-8')
# wfile.close() 권장
with open(pathName2,'a',encoding='utf-8') as myfile: #파일변수

    name = input('이름입력 >>> ')
    age = input('나이입력 >>> ')
    juso = input('주소입력 >>> ')

    #자동 줄바꿈이 안되기에 뒤에 라인개행문자 써줌.
    myfile.write(name + '\n')
    myfile.write(age + '\n')
    myfile.write(juso + '\n')
    #wfile.close() # 추천 권장

    time.sleep(0.5)
    print(pathName2, '파일 저장에 성공했습니다.')
    print()
'''
 pathName = 'C:\Mnet/sample.txt'
이름입력 >>> kim
나이입력 >>> 21
주소입력 >>> 서울
sample.txt 파일 저장에 성공했습니다.

=>기존의 값을 덮어쓴다. ->추가할려면 모드를 a로 줘야 된다.
=>탐색기에서 파일 생성유무 확인할것.
'''

''' 
 파일의 내용 확인 2개의 데이터를 연속적으로 입력한 경우(추가모드임.)

임시
45
서울시
홍길동
34
대전시
'''