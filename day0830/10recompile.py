# 10recompile.py

import re

data = '''
kim 840916-1694852
lee 921207-2759326
red 981024-1674938
'''

# print(data[12:])

# for k in data:
#     print(k,end='')
#  \n 라인개행 enter 기능 \t 탭 \b 백space  + 반복
#\d decimal(정수의미)
# com = re.compile('(\d{6})[-](\d{7})')  
com = re.compile('-\d+')# 경고 메세지 나와도 괜찮다.
first = com.sub('-*******',data) #2번째항목에 data입력
#                   <1>1번째부터 적용
print(first) # 비권장
print()
#print(data)

#숫자중에서 7번째에 적용하겠다는 표시(찾을조건,적용문자열,데이터대상자)
two = re.sub('[0-9]{7}','*******',data) # 권장(추천) sub(1,2,3적용문자열)
print(two) # 다 가릴수는 없다.

'''
kim 840916-*******
lee 921207-*******
red 981024-*******
'''
# compile('\d{6}-\d{7}') 적용후  sub() 확인
# 문자열 함수 for ~ if ~ data [시작위치:]
# 정규식  re.sub('-[0-9]{4}-','-****-,)

# kim 840916-*******
# lee 921207-*******
# goo 981024-*******


# #4번째 정규식 예제 re.sub(1,2,3)
# import re #정규식을 위해서 re모듈 불러옴.

# phone = '010-7800-1234 박이썬'
# # 힌트 re.sub('1패턴','2변경적용',phone)
# # 문자열의 함수,문자열의 기본이 중요하다.
# model = re.sub( '-[0-9]{4}', '-****', phone)

# print(phone) #-4자리이상의 숫자형 데이터를 찾아라 (-[0-9]{4}(자리수))
# print(model) #010-****-1234 박이썬

'''
010-7800-1234 박이썬
010-****-**** 박이썬
'''

#3번째 정규식 예제 re.findall()
# #msg변수에 새로운 내용 덮어씌우는 재할당
# msg = 'my best %#@& 245 오렌지 is (_^!& ^.^ 수박 cherry as tea'

# result1 = re.findall('[\w]+ ',msg)#소문자 찾기 + 한글자이상
# result2 = re.findall('[\W]*',msg) #대문자 찾기 (비권장)
# result3 = re.findall('[a-zA-Z0-9가-힣]+ ',msg)#한글자 이상 뽑음.
# result4 = re.findall('[^a-zA-Z0-9가-힣]+ ',msg)#앞에 ^ 아닌거 찾기
# # 가-힣(한글까지 검색) 3~10글자이하 찾기(자릿수가 있어야 검색원활)

# print(result1);print()
# print(result2);print()
# print(result3);print()
# print(result4);print() #[' %#@& ', ' (_^!& ^.^ ']

'''
#['y ', 't ', '5 ', '지 ', '박 ', 'y ', 's ']
#[' ', ' ', '%', '#', '@', '&', ' ', ' ', ' ', ' ', ' ', ' ']
#['y ', 't ', '5 ', '지 ', '박 ', 'y ', 's ']

'''
# #2번째 정규식
# msg = 'my best blue myjava my cherry blue my python my'
# x = re.findall('my',msg) #찾는 단어를 직접 입력해도 된다. 빈도수찾기
# y = re.findall('blue',msg)
# z = re.findall('red',msg)

# print(x) 
# print(y)
# print(z) # 에러대신 [] 출력
# print()
'''
['my', 'my', 'my', 'my', 'my']
['blue', 'blue']
[] =>찾는 데이터 없음.
'''

# 첫번째 정규식 예제
# msg = 'my bes% 2400 Flu_it is blue%#357cherry'
# info1 = re.findall('[a-zA-Z]{3,7}',msg) #자동으로 리스트화가 된다.
# info2 = re.findall('[a-zA-Z0-9]{3,7}',msg)
# print(info1) ['best','Flu' 'blue','cherry']
# print(info2) ['best','2400,'Flu' 'blue','357cherry']
# print()

print()