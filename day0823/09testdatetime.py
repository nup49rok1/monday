#09testdatetime.py

import time

my = time.localtime()

print(my.tm_year,'년')#2024
print(my.tm_mon,'월')#8
print(my.tm_mday,'일')

wday = my.tm_wday

week = [ '월요일','화요일','수요일','목요일','금요일','토요일','일요일']
print(week[wday]) #리스트를 쓰는것이 아래와 같이 다중 if문 쓰는것보다 낫다

#반복문 대신 if 제어문 사용
# 0(월) 1(화) 2(수) 3(목) 4(금) 5(토) 6(일)

# if wday == 0:
#     print('월요일')
# elif wday == 1:
#     print('화요일')
# elif wday == 2:
#     print('수요일')
# elif wday == 3:
#     print('목요일')
# elif wday == 4:
#     print('금요일')
# elif wday == 5:
#     print('토요일')
# elif wday == 6:
#     print('일요일')
# else:
#     print('일요지정이 잘못되었습니다.')

print()

'''
2024 년
8 월
23 일
금요일
'''