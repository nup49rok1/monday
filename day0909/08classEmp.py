#08classEmp.py

#자바의 this=>파이썬에서는 self를 사용한다.
##TypeError: Emp.insert() takes 0 positional arguments but 1 was given =>self

# 파이썬에서 클래스 이름만 명시
# 클래스안에 있는 메서드 매개인자(self)
# 클래스안에 있는 메서드 호출 ob = 클래스()

class Emp:
    #member 변수=global variable=public variable
    user_id = '아이디'
    user_pwd = '1111' 
    
    #생성자
    def __init__(self,id,pwd):
        self.user_id = id
        self.user_pwd = pwd
        
    def insert(self,age):  #파이썬에서의 함수내부에는 self를 써줘야 된다.
        print('전역변수  user_id',self.user_id)#전역변수에 접근가능하게 해주는 키워드 self.전역변수명
        print('전역변수  user_pwd',self.user_pwd)
        print('전달된 이름 ',nick)
        print('전달된 나이 ',age)
        print('신규등록 insert(self키워드)')
        print(' insert into 처리\n')

    def delete(self):
        print('삭제처리')
        print('딕트 del, delete where 조건')
        

#  에러 발생 delete()
ob = Emp('sky','7788') #생성자=>객체를 생성할때 맨 처음 호출되는 함수(값 초기화)
##TypeError: Emp.insert() takes 0 positional arguments but 1 was given 
ob.insert(7) #객체명.함수명()
ob.delete()


'''


'''