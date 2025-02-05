#07rjust.py

#오른쪽 맞춤

for x in range(1,6,1):
    pass
    #print(f'{x} * {x} = {x*x}')
    print(x,'*',x,'=',(x*x)) #가독성이 좀더 낫다.


print()
'''

1 * 1 = 1
2 * 2 = 4
3 * 3 = 9
4 * 4 = 16
5 * 5 = 25

'''
#문자열(객체)로 인식

for x in range(100,106,1):
    print(x,'*',x,'=',str(x*x).rjust(3)) #숫자에서 문자로 변환됨
    

'''
  숫자는 오른쪽에 배치(8자리수)
1 * 1 =     1
2 * 2 =     4
3 * 3 =     9
4 * 4 =    16
5 * 5 =    25

100 * 100 =    10000
101 * 101 =    10201
102 * 102 =    10404
103 * 103 =    10609
104 * 104 =    10816
105 * 105 =    11025


'''
print()

for x in range(1,6,1):
    print(x,'*',x,'=',str(x*x).zfill(5)) #0로 채움(자릿수)

print()
'''

1 * 1 = 00001
2 * 2 = 00004
3 * 3 = 00009
4 * 4 = 00016
5 * 5 = 00025

'''