#16defreturn.py =>15defreturn.py와 비슷

def book():
    title = '몽블랑' #제목  지역변수=local variable (휘발성)
    return title #return 전달할값(리턴값)

def pay():
    m = 7800 #지역변수=local variable
    return m

# 일반함수 리턴값 X  없는 호출해서 출력하면 None
def blue():
    color = 'dark'
    #print(데이터값 출력)

def main():
    print("main 함수 ")
    print("책제목 ",book())
    print("책가격 ",pay())
    print("블루색 ",blue()) # None 출력/pass 필드


#함수 단독 기술해서 호출해도 된다.
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