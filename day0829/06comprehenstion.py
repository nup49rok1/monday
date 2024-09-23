#06comprehenstion.py

mylist = [ a**2 for a in range(1,11,1)] # 추천
print(mylist)
print()


myset = { c**2 for c in range(1,11,1) } #단점 순서가 없다.
print(myset)
print()
'''
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

{64, 1, 4, 36, 100, 9, 16, 49, 81, 25}
'''

