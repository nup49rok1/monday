#10replace.py

# 문자,문자열변경 replace(구변경대상,신)
# 문자,문자열 공백제거 lstrip,rstrip
# p89

info = 'my best friend gildong'
myret1 = info.replace('best','coffee')
print(info)
print(myret1)

#myret2 = info.replace()#TypeError: replace expected at least 2 arguments, got 0
#인수 2개가 필요함을 알려줌.

myret2 = info.replace(' ','')
print(myret2) #공백제거 mybestfriendgildong

msg = '      it is a best python     '
x = 'aaa'
y = 'yyy'

#p86
print(x+msg+y) # 공백을 유지하면서 연결(공백도 문자로 인지)
print(x+msg.lstrip()+y)  #aaait is a best python  msg 왼쪽공백제거
print(x+msg.rstrip()+y) #aaa      it is a best pythonyyy 오른쪽공백제거


print()
'''

my best friend gildong
my coffee friend gildong
mybestfriendgildong
aaa      it is a best python     yyy
aaait is a best python     yyy
aaa      it is a best pythonyyy
'''