#12juminlist.py

import datetime #from import 
import time

# x = datetime.now() #에러 발생->실행시
# print(x)
#          [0]    [1]
jumin = '971230-1835064' #금융권에서는 - 로 계좌번호등 사용

# mylist = list(jumin.split()) #비권장
# 은행, 금융, 보험  - 분리
mylist = list(jumin.split('-'))
print(mylist)
# print(mylist[0])
# print(mylist[1])

gender = mylist[1][0] # 이 자체가 리스트
print('성별표시확인 ',gender)

# print(mylist[1][0]) #1

'''
['971230', '1835064']
971230
1835064
'''
# [1]항목중에서 첫번째 문자열을 의미
if (jumin.split('-')[1][0]==1) or (jumin.split('-')[1][0]==3) :
    pass
    print('당신의 성별은 남자입니다.')
elif (jumin.split('-')[1][0]==2) or (jumin.split('-')[1][0]==4) :
    pass
    print('당신의 성별은 여자입니다.')
else:
    print('성별표기 오류입니다.\n다시 체크하세요')

print()
print('😊 ' * 30)

year = jumin.split('-')[0][:2] #[0:2]에서 0을 생략해도 된다.
# year = jumin.split('-')[0][0:2] 
print('태어난 년도 ',year) #태어난 년도  97


last = jumin.split('-')[1][:]
print('주변 뒷자리 ',last)