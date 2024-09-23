# 15global.py

Gtotal = 78

def aaa():
    # global Gtotal #생략하면 에러  cannot access local variable 'Gtotal' 
    Gtotal = Gtotal + 1100
    print('aaa함수=' , Gtotal)
    

def bbb():
    # global Gtotal  #생략하면 에러   cannot access local variable 'Gtotal' 
    Gtotal = Gtotal + 1200
    print('bbb함수=' ,Gtotal)

aaa()
print()
bbb()