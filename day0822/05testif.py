#05testif.py

'''
 제어 if~else
 제어 if~elif~else
'''

count = 5 #내장함수 이름과 충돌이 날 가능성이 있기에 비추천
cnt = 5 #권장
mycount = 5 #권장

if cnt >= 5: #Expected :  :을 빼먹은 경우 조심
    print('게임종료 되었습니다.')
    print('다음에 도전하세요')

#에러이유 Unexpected indentation
#에러이유 Unindent 들여쓰기 indent
print('이글스 A') 
print('라이온 B')
print('타이거 C')
print('베어스 D')
print()