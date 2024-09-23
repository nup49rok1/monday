#13gugudan.py

#dan = 7
data = input('구구단입력>>>')
dan = int(data)
for k in range(1,10,1) :
    #pass
    print(dan,'*',k,'=',(dan*k))

print()
#print('구구단 연습')

'''
 파이썬 화면모니터 출력 print('안내문',값)
 파이썬 키보드자판 입력 input('안내문')
 파이썬 키보드입력데이터 문자로 인식
 int("1200") 숫자 1200
'''

# a = '120'
# b = '75'
# print(a+b) #문자열 연결
# c = int(a) + int(b)  #int정수=integer
# print(int(a) + int(b)) #int정수=integer
# print(c) 

'''
12075
195
195
'''

#파이썬 내장함수
#print(), int(), round(),input(),str(),sum()

'''
구구단입력>>>5
5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
5 * 5 = 25
5 * 6 = 30
5 * 7 = 35
5 * 8 = 40
5 * 9 = 45
'''