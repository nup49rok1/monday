#12replace.py

# 문자,문자열변경 replace(구변경대상,신)
# 문자,문자열 공백제거 lstrip,rstrip
# p89


msg = '      it is a best python     ' 

print(msg.replace(' ','')) #밑의 3줄과 동일하다.(결과)
print('- '*50)

print(len(msg))#30

for k in range(len(msg)):#33
    if msg[k] not in ' ': #공백이 없다면 
       print(msg[k],end = '') 
print()
mylist = msg.split() #list가 만들어진다.
                   #split()가 인수가 없으면 자동공백제거
                   #리스트화가 된다.
print(mylist)
print('='*50)

mylist2 = msg.split(' ') #공백을 기준으로 하나씩 공백까지
print(mylist2)           #출력
'''
itisabestpython
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
itisabestpython
['it', 'is', 'a', 'best', 'python']
==================================================
['', '', '', '', '', '', 'it', 'is', 'a', 'best', 'python', '', '', '', '', '']
'''