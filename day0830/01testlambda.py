#01testlambda.py
# 람다식은 import 기술안함, 키워드 lambda 기술


def mycal(su):
    # cal = 3 * su + 8
    # return cal
    return 3 * su + 8

print('일반식',mycal(5))
my1 = lambda su:3 * su + 8
#(lambda 매개변수:처리수식)(전달받은값)
print('람다식',my1(5)) #람다식을 변수로 받아서 함수처럼 호출하는 경우
print('람다식',(lambda su:3 * su + 8)(5))
print()

def myAdd(x,y):
    # hap = x + y
    # return hap
    return x + y

print('일반식',myAdd(11,9))
my2 = lambda x,y:x + y
#(lambda 매개변수:처리수식)(전달받은값)
print('람다식',my2(11,9))
print('람다식',(lambda x,y:x + y)(11,9)) #추천(권장)
print()

print('- ' * 50)
print()
#함수에서 계산처리후 if ~ else 제어문 리턴값
def myCheck(su):
    # pass if~else 짝수/홀수인지 체크
    msg = '안내문'
    if su % 2 == 0:
        # print(su,'은 짝수')
        msg= '짝수'
    else:
        # print(su,'은 홀수')
        msg= '홀수'
    return msg

print('일반식',myCheck(17))
print('람다식',(lambda su:'짝수' if su%2==0 else '홀수' )(17))

print()