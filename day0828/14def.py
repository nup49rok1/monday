#14def.py

'''
파이썬에서 함수 정의 시작 키워드 def 함수이름():
사용자 정의 함수 매개인자 구구단 실습확인
사용자 정의 함수에서 처리후 외부에 값을 줄때 return 값
사용자 정의 함수 매개인자 + 리턴값

'''

import time
#함수정의=구현=기술 함수=function=기능
def gugudan(writer,dan):
    print('구구단 저자',writer)
    for k in range(1,10) :
        print(f'{dan} * {k} = {dan*k}')
        time.sleep(0.3)

# myTotal 함수 기술 총점,평균 출력 (인수가 3개를 필요로 한다는 말)
#TypeError: myTotal() takes 0 positional arguments but 3 were given

def myTotal(kor,eng,mat): #입력->전달 매개변수명 같아도 된다.
    print('myTotal 함수영역')
    hap = kor + eng + mat
    avg = hap // 3
    print('myTotal 총점=',hap)
    print('myTotal 평균=',avg)
  

#함수 호출
# gugudan('lee',7)
if __name__ == '__main__': #생략가능  (메인역할) =>진입의 기본을 메인
    gugudan('lee',7)
    print()
    #키보드를 통해서 받아서 처리할 예정 
    kor = 90
    eng = 85
    mat = 60
    myTotal(kor,eng,mat)

print()
print()