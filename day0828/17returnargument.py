#17dreturnargument.py 

def book(): #매개인자 X 리턴값 O
    title = '몽블랑' 
    return title 

def pay():  #매개인자X, 리턴값 O
    m = 7800 
    return m

def myCal(x,y,z): #매개인자 O ,리턴값 O
    total = x + y + z
    avg = total // 3  #반올림 안하고 몫만 구한 경우
    #3개 데이터를 받아서 계산 연산 처리한후 최종값 리턴
    return avg

#   myCal 함수 호출 90 85 64
#   myCal 함수 리턴값이 있으면 변수 = 함수이름
#   myCal 함수 리턴값이 있으면 print(함수이름())

data = myCal(90,85,64)
print('myCal함수결과 ', data)
print('myCal함수결과 ', myCal(90,85,64))

'''
myCal함수결과  79
myCal함수결과  79
'''

# def gugudan(name,dan): #매개인자 O ,리턴값 X
#     pass
#     #name출력 반복문 dan 출력

# def blue():
#     color = 'dark'
#     #print(데이터값 출력)

# def main():
#     print("main 함수 ")
    
# main()
'''

'''

print()
print()