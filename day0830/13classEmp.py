#13classEmp.py

#자바의 this=>파이썬에서는 self를 사용한다.
##TypeError: Emp.insert() takes 0 positional arguments but 1 was given =>self

# 파이썬에서 클래스 이름만 명시
# 클래스안에 있는 메서드 매개인자(self)
# 클래스안에 있는 메서드 호출 ob = 클래스()

class Emp:
    def insert(self):  #파이썬에서의 함수내부에는 self를 써줘야 된다.
        print('신규등록')
        print('딕트 등록, 파일저장, insert into 처리')
        print(' insert into 처리\n')



    def delete(self):
        print('삭제처리')
        print('딕트 del, delete where 조건')
        

#  에러 발생 delete()
ob = Emp()
##TypeError: Emp.insert() takes 0 positional arguments but 1 was given 
ob.insert() #객체명.함수명()
ob.delete()

#구분용
print()
print('9월 2일 월요일 3')
print('9월 2일 월요일 4')
print('9월 2일 월요일 7')

'''
규등록
딕트 등록, 파일저장, insert into 처리
 insert into 처리

삭제처리
딕트 del, delete where 조건

9월 2일 월요일 3
9월 2일 월요일 4
9월 2일 월요일 7
'''