#07comprehension.py  [연산 if/else  for  ]

message = ['ham','spam','spam','ham','spam','ham','spam']

#dummy = [1,1,0,1,0,1,0]
dummy = []
#문제3  span=0 ham=1 dummy = [1,1,0,1,0,1,0 ] ret = [ ]
#message = ['spam','ham','spam','ham','spam','ham','spam','ham','spam']
# for ~  if ~ else

for k in message :
    if k == 'spam':
        dummy.append(0)
    else:
        dummy.append(1)

print('반복 ~ 제어 정석 ',dummy)
'''
spam spam spam 
temp_list= ['spam', 'spam', 'spam']

[1, 1, 0, 1, 0, 1, 0]
'''
#  참인값 출력 if 참인조건 else  거짓인값 출력 for 문구현
mydummy = [ 0 if k == 'spam' else 1 for k in message ]
print('comprehension',dummy)

print()