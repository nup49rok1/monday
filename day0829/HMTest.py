# 01test.py

# day0829 폴더 오픈 
# 문제1 name,age,gender 변수 사용, 키보드 입력,나이는 숫자
# 문제2 나이입력 범위 20~70 사이 입력 그 이외 숫자입력하면 재입력 
# 조건 20 미만 청소년 1~19   20~30 청년 31~65 중년 66이상 노년
# 문제3 남자/남/man True 출력   여자/여/woman 입력 False 출력
# 문제4 해결안하고 고민만  list관리/tuple관리/dict 관리 =>예외처리
#             
# 문제5 아래내용을 함수이름 임의의 명명 def 함수이름() :

# *********** 본인 정보 **********
# 이름 홍길동
# 34세 청년입니다.
# 성별은 남자입니다.

# 홍길동
# 24세 청년
# 남자
# def person():
#     print('홍길동')
#     print(34,'청년')
#     print('남자')


name = input('이름을 입력하세요?')
age = int(input('나이을 입력하세요?'))
gender = input('성별을 입력하세요?')

test='' #청년유무

if (age>=1 and age<=19):
        test='청소년'
else:
    while (20<age<70):

        if (age>=20 and age<=30):
            test='청년'
            break
        elif (age>=31 and age<=65):
            test='중년'
            break
        elif age >=66:
            test='노년'
            break
        else:
            print('다시 입력하시기 바랍니다.')
            age = int(input('나이을 입력하세요?'))
            break

if (gender == '남' or gender == '남자' or gender == 'man'):
    print(True)
else:
    print(False)

print('****본인 정보*****')
print('이름',name)
print(str(age)+'세',test+'입니다.')
print('성별은',gender,'입니다.')