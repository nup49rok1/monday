# 06re.py
# 정규식 예제

import re #정규식을 위해서 re모듈 불러옴.

# url = 'www.google.com'
# print(url.split('.')) #['www', 'google', 'com']
# print(' '.join(url)) #w w w . g o o g l e . c o m

msg = 'my bes% 2400 Flu_it is blue%#357cherry'
#print(msg)
#TypeError: findall() missing 2 required positional arguments: 
#                    'pattern' and 'string' 인수확인하기
info1 = re.findall('[a-zA-Z]{3,7}',msg) #자동으로 리스트화가 된다.
info2 = re.findall('[a-zA-Z0-9]{3,7}',msg)
print(info1) #['bes', 'Flu', 'blue', 'cherry']
print(info2) #['bes', '2400', 'Flu', 'blue', '357cher']
print()
'''
  3글자 이상 
['bes', 'Flu', 'blue', 'cherry']
['bes', '2400', 'Flu', 'blue', '357cher'] 밑에는 숫자가 나옴(위 설정)
'''
#7에서 10글자내에서 적합한 데이터를 찾아서 출력하기->4글자로 변경 결과
# my = re.findall('[a-zA-Z]{4,10}',msg)
my = re.findall('[a-zA-Z]{4,10}',msg)
if my :
    print(my)
else:
    print('[a-zA-Z]{7,10} 조건에 맞는 데이터 없습니다.')

# msg = 'my bes% 2400 Flu_it is blue%#357cherry'