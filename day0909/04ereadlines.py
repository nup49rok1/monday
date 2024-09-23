#04readlines.py

# 임포트 문장 X import file ~
# pathName = '경로/파일.txt'
# 리턴변수 = open('파일명',모드w/r/a, 인코딩)
# 리턴변수.close() 사용하는겻이 좋다. 직접 open()쓴 경우
# ff = open(1,2,3) 대체 =>  with open(1,2,3) as ff
                           # 리턴변수.close() 사용하지 않아도 OK

# 파일 읽기 read() ,readline() ,readlines()

file = 'C:/Mnet/kakao.txt'
with open(file,'r',encoding='utf-8') as myfile: #파일변수
    for data in myfile.readlines(): #while대신에 for문으로 변경
        print(data,end='') 


print(file, '파일 읽기에 성공했습니다.\n')
print()
print()

'''
 
'''