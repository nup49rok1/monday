# 숙제 homeworkfunc.py

a,b=9,5

hap,sub,gob,nmg=0,0,0,0
mok=0.0

def cal(a=9,b=5):
    hap=a+b
    sub=a-b
    gob=a*b
    mok=a/b
    nmg=a%b

    print(a,'+',b,'=',hap)
    print(a,'-',b,'=',sub)
    print(a,'*',b,'=',gob)
    print(a,'/',b,'=',mok)
    print(a,'%',b,'=',nmg)
    print('--'*30)

cal(9,5)
cal(9)
cal()


'''
 9+5=14
 9-5=4
 9*5=45
 9/5=1
 9%5=4
'''