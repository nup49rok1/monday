#04testlambda.py
# 람다식은 import 기술안함, 키워드 lambda 기술


def mycal(su):
    return su * su

print('일반식',mycal(6))
my1 = lambda su:3 * su + 8
#(lambda 매개변수:처리수식)(전달받은값)
print('람다식',my1(6)) #람다식을 변수로 받아서 함수처럼 호출하는 경우
print('람다식',(lambda su:3 * su + 8)(6))
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

print('일반식',myCheck(7))
print('람다식',(lambda su:'짝수' if su%2==0 else '홀수' )(7))
print('😊 ' * 30)
print()

#문제 리스트 1 2 3 ~  8 9 10 까지 출력 for,while 반복문 사용 금지
# 머신러닝 문제에서 for,while을 잘 안쓴다.
data = list(range(1,11,1)) #리스트화 시킴->1 ~ 10 출력
# data = range(1,11,1)  #출력 range(1,11)
print(data) #[1*1 2*2, 3*3, ~*8*8 ,9*9,10*10]
print(data*2)#똑같은것을 두번 반복한다.(단순히)=>제곱이 아님
# 추가
# print('람다식',(lambda su:su*su)(data)) # 에러유발
#TypeError: can't multiply sequence by non-int of type 'list'
# 반복의 의미 지 계산이 안됨
# 첫번째 예제 성공 print('람다식',(lambda su:su*su)(6))

my = (lambda su:su*su)(6)
print(my)#36

print()
# map 함수 이용
# my = map((lambda su:su*su),(data)) 
# print(my)#36 <map object at 0x000001B6D5E65600> 맵객체 표시 출력됨
# print(list(my)) #리스트화 시킴
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#최종적으로 맵함수로 전달받은값을 리스트형태로 만들어야 출력이 된다.
my = list(map((lambda su:su*su),data)) 
print(my) #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# 람다함수 최종 마무리 =>pdf파일 참조 설명
