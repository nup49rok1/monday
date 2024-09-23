# 07re.py
# 정규식 예제

import re #정규식을 위해서 re모듈 불러옴.

msg = 'my best blue myjava my cherry blue my python my'
x = re.findall('my',msg) #찾는 단어를 직접 입력해도 된다. 빈도수찾기
y = re.findall('blue',msg)
z = re.findall('red',msg)

print(x) 
print(y)
print(z) # 에러대신 [] 출력
print()

'''
['my', 'my', 'my', 'my', 'my']
['blue', 'blue']
[] =>찾는 데이터 없음.
'''
#msg변수에 새로운 내용 덮어씌우는 재할당
msg = 'my best %#@& 245 오렌지 수박 cherry as tea'

result1 = re.findall('[\w] ',msg)#소문자
result2 = re.findall('[\W]',msg) #대문자입력
result3 = re.findall('[a-zA-Z0-9가-힣] ',msg)# 가-힣

print(result1)
print(result2)
print(result3)

# 첫번째 정규식 예제
# msg = 'my bes% 2400 Flu_it is blue%#357cherry'
# info1 = re.findall('[a-zA-Z]{3,7}',msg) #자동으로 리스트화가 된다.
# info2 = re.findall('[a-zA-Z0-9]{3,7}',msg)
# print(info1) ['best','Flu' 'blue','cherry']
# print(info2) ['best','2400,'Flu' 'blue','357cherry']
# print()

print()