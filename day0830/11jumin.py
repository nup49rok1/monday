#11jumin.py
# 이름,나이 개인정보 제공->쿠폰주는 경우의 예제

import re

#jumin= '010924-4674938' #여자인 경우(4)
jumin= '870924-1674938' #변경한 경우

my = int(jumin[7]) #정규표현식을 모른경우에 문자열의 위치를 찾아서 사용

if my==1 or my==3:
    print('남자')
elif my==2 or my==4:
    print('여자')
else:
    pass


gender = re.search( '(-)(\d{1})', jumin)# 서식,찾을 대상
print(gender)#<re.Match object; span=(6, 8), match='-1'>

genderNum = int(gender.group(2))#2번째를 뽑아냄 -을 기준으로
print(genderNum)#1=>4(매칭 4(여자))

if genderNum==1 or genderNum==3:
    print('남자')
elif genderNum==2 or genderNum==4:
    print('여자')
else:
    print('성별표기 오류입니다.')

'''
  gender = re.search( '(-)(\d{1})', jumin)# 서식,찾을 대상
<re.Match object; span=(6, 8), match='-4'>
4
여자
'''



print()