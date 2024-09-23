#10testlambda.py

# 람다 = 익명의 함수 = 함수 이름이 없어요
# 람다식은 import 없습니다.
# 람다식은 lambda 키워드 기술

def mysu(num):
    cal = 3 * num + 5
    return cal 

data = int(input('숫자입력>>> '))
print('일반식',mysu(data))
# (lambda 매개변수명:함수가 처리할 내용)(매개변수명)
print('람다식', (lambda num:3 * num + 5)(data))
print()
'''
숫자입력>>> 8
일반식 29
람다식 29
'''