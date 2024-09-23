#06testpickle.py


# open(1파일명,모드wb/rb(binary),인코딩)
# dump 쓰기/load 읽기
# 피클로 파일처리 import 

import pickle
import time

fileName = 'c:/Mnet/movie.young' #확장자는 자기 마음대로 작성이 가능(pckl,young,,,)
#메모장에서 불러오면 깨져서 불러옴.
mybest = {'슈퍼맨super':9.2,'아이iron':7.4,'손흥민':5.3}  #영어한글썪어씀
#file = open(fileName,'wb') #b사용하면=>물리적으로 단독 실행이 되지를 않음.
# 일반파일저장 file.write('슈퍼맨superman')
# 피클은 한꺼번에 모아서 처리한다.
pickle.dump(mybest,open(fileName,'wb'))
print(fileName,'피클저장 성공했습니다.')
print('-' * 60)
print()

time.sleep(1)
#피클파일 저장 dump(1,2) / load(1,'rb')
data = pickle.load(open(fileName,'rb'))
print(data)
print(fileName,'피클읽기 성공했습니다.')
print()

'''
c:/Mnet/movie.pckl 피클저장 성공했습니다.

Traceback (most recent call last):
  File "c:\Mnet\workPython\day0902\06testpickle.py", line 24, in <module>
    data = pickle.load(open(fileName,'rb'))
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
EOFError: Ran out of input =>파일 손상시 불러오지 못하는 경우 발생
                           =>파일을 새로 생성(확장자를 바꿔서 하면 OK)

c:/Mnet/movie.young 피클저장 성공했습니다.
------------------------------------------------------------

{'슈퍼맨super': 9.2, '아이iron': 7.4, '손흥민': 5.3}
c:/Mnet/movie.young 피클읽기 성공했습니다.
'''
