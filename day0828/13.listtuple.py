#13listtuple.py

#리스트    순서유지, 중복 허용
#튜플      순서유지, 중복 허용 

mylist = ['kim',78,True,3.1415,78,'kim']
mytuple = ( 'lee',54,True,3.1415,54,'lee' )

mylist[1]=1200   #리스트 변경 가능
#mytuple[1]=1200   #튜블 변경 X  
#TypeError: 'tuple' object does not support item assignment

print(mylist)
print(mytuple)


print()
'''
PS C:\Mnet\workPython> & C:/Users/user/anaconda3/envs/ck/python.exe c:/Mnet/workPython/day0828/13.listtuple.py
['kim', 78, True, 3.1415, 78, 'kim']
('lee', 54, True, 3.1415, 54, 'lee')
'''