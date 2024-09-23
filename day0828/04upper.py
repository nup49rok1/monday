#04upper.py p86~90 교재참조

#대문자로 변경

msg = 'bstzpchERry'

print(msg.upper())#대문자로 변경
print(msg.lower()) #소문자로 변경
print()

'''
BTSKPCHERRY
btskpcherry
'''

print('k =',msg.find('k')) #k=3 위치에 있다고 알려줌=>없으면 -1을 리턴해준다.
print('t =',msg.index('t')) #t=2 위치

msg = 'bstkpchERry'
#print('z =',msg.find('z')) #z= -1 위치 (없는 경우)
#print('z =',msg.index('z')) #없으면 에러가 발생이 된다. ValueError: substring not found
pos = msg.find('z')

if pos == -1: #없는 경우
    pass
    print('원하는 키워드가 없습니다.')
else:
    pass
    #있으면 출력을 하거나 조작,연산처리

print('-'*70)