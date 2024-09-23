#14deftuple.py 


def test(**my):
    print('test함수(my)')
    print('my타입',type(my))

# def test3(**kvargs):
#     print(type(kvargs))# <class 'dict'>
#     print(kvargs.keys())#dict_keys(['code', 'title', 'grade'])
#     print(kvargs.values())#dict_values([2400, 'summer', 'A'])
#     for k,v in kvargs.items():
#         print(k, " : ",v)


# test3(코드=2400,제목='summer',등급='A')
test(code=2400,title='summer',grade='A')
