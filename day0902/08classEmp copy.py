#08classEmp.py



class Emp:
    #member 변수=global variable=public variable
    user_id = '아이디'
    user_pwd = '1111' 
    
    #생성자
    def __init__(self,id,pwd): #self 빼면 안된다.
        self.user_id = id   #self.user_id='sky'
        self.user_pwd = pwd #self.user_pwd=7788
        
    def insert(self,age):  #파이썬에서의 함수내부에는 self를 써줘야 된다.
        print('\n전역변수  user_id',self.user_id)#전역변수에 접근가능하게 해주는 키워드 self.전역변수명
        print('전역변수  user_pwd',self.user_pwd)
        print('전달된 이름 ',self.user_id)
        print('전달된 나이 ',age)
        print('신규등록 insert(self키워드)')
        print(' insert into 처리\n')

    def delete(self):
        print('삭제처리')
        print('딕트 del, delete where 조건')
        

#  생성자(id,pwd) 호출하면서 값 2개가 전달이 된다.
ob = Emp('wed','1234') 
ob.insert(23) 
ob.delete()


'''
전역변수  user_id wed
전역변수  user_pwd 1234
전달된 이름  wed
전달된 나이  23
신규등록 insert(self키워드)
 insert into 처리

삭제처리
딕트 del, delete where 조건

'''