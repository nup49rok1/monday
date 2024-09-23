#14deftuple.py 
# # 첫번째 함수이름 test(매개인자)
# 두번째 test('code'=2400,'title'='summer','grade'='A')
# 세번째 test함수에서 코드 2400 제목 summer 등급 A
# 세번째 test함수에서  code 2400 title summer 등급 A 

def test(*args):
    print(type(args))
    print(args)

def test2(code=2400,title='summer',grade='A'):
    print('code=>',code,"title=>",title,"grade=>",grade)

def test3(**kvargs):
    print(type(kvargs))# <class 'dict'>
    print(kvargs.keys())#dict_keys(['code', 'title', 'grade'])
    print(kvargs.values())#dict_values([2400, 'summer', 'A'])
    for k,v in kvargs.items():
        print(k, " : ",v)

test(1,2,3,4)
test([1,2,3],[1,2,3])
test([1,2])
# 파이썬 함수이름(*매개인자):
# 파이썬 함수이름(**매개인자):
test2()

test3(코드=2400,제목='summer',등급='A')
test3(code=2400,title='summer',grade='A')
'''

<class 'tuple'>
(1, 2, 3, 4)
<class 'tuple'>
([1, 2, 3], [1, 2, 3])
<class 'tuple'>
([1, 2],)

<<class 'dict'>
dict_keys(['코드', '제목', '등급'])
dict_values([2400, 'summer', 'A'])
코드  :  2400
제목  :  summer
등급  :  A

<class 'dict'>
dict_keys(['code', 'title', 'grade'])
dict_values([2400, 'summer', 'A'])
code  :  2400
title  :  summer
grade  :  A
'''