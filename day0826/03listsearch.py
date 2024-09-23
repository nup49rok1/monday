#03listsearch.py

data = [7,8,9,1,2]
ss = int(input('데이터 찾기>>> '))

#추가
if ss in data: #찾을 값  in 찾을 범위 부분
    #print('결과 ',ss in data)
    print(ss, '검색 성공 ok')
else:
    #print('결과 ',ss in data)
    print(ss, '검색 실패 failed')

#데이터가 있으면 성공메세지 데이터 출력
#데이터가 없으면 실패메세지 
# 참고 for 대표변수 in range(5) :
# list에서 데이터 찾기 할때 in 키워드 사용
'''
print (ss in data)

데이터 찾기>>> 4
False
PS C:\Mnet\workPython> & C:/Users/user/anaconda3/envs/ck/python.exe c:/Mnet/workPython/day0826/03listsearch.py
데이터 찾기>>> 7
True
'''

'''
데이터 찾기>>> 7
결과  True
7 검색 성공 ok
PS C:\Mnet\workPython> & C:/Users/user/anaconda3/envs/ck/python.exe c:/Mnet/workPython/day0826/03listsearch.py
c:\Mnet\workPython\day0826\03listsearch.py:18: SyntaxWarning: invalid escape sequence '\M'

데이터 찾기>>> 3
결과  False
3 검색 실패 failed
PS C:\Mnet\workPython> 
'''

'''
 예외처리 부분 =>숫자를 입력을 받아야 되는데 문자를 받는 경우
데이터 찾기>>> aa
Traceback (most recent call last):
  File "c:\Mnet\workPython\day0826\03listsearch.py", line 4, in <module>
    ss = int(input('데이터 찾기>>> '))
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: invalid literal for int() with base 10: 'aa'
PS C:\Mnet\workPython> 
'''