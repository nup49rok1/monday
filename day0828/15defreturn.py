#15defreturn.py

'''
파이썬에서 함수 정의 시작 키워드 def 함수이름():
사용자 정의 함수 매개인자 구구단 실습확인
사용자 정의 함수에서 처리후 외부에 값을 줄때 return 값
사용자 정의 함수 매개인자 + 리턴값
'''

def book():
    title = '몽블랑' #제목  지역변수=local variable (휘발성)
    return title #return 전달할값(리턴값)

def pay():
    m = 7800 #지역변수=local variable
    return m

def main():
    print("main 함수 ")
   # print("책제목 ",title)
   # print("책가격 ",m)
    data = book()
    value = pay()
    print("책제목 ",data)
    print("책가격 ",value)
    print("책제목 ",book)#함수명을 주면 함수의 주소값이 출력이 된다.
    print("책가격 ",pay)
    print("책제목 ",book())
    print("책가격 ",pay())

if __name__ == '__main__':
    main()
'''
main 함수 
책제목  몽블랑
책가격  7800
책제목  <function book at 0x0000022D3DA18A40>
책가격  <function pay at 0x0000022D3DC79B20>
책제목  몽블랑
책가격  7800
'''

print()
print()