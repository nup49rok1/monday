#10deftuple.py


def  two_hap(args): #리스트 데이터 받기
    hap = 0 
    for su in args:
        hap = hap + su
    return hap


mylist = [ 5,3,1,4,6] 
msg = two_hap(mylist) 
print('리스트 합계',msg)

'''
리스트 합계 19
'''