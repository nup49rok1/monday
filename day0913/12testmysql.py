
# mysql test테이블 + 파이썬
import pymysql  #pip install pymysql 이미 설치된 상태
import time

# configOracle = {
#     'user' : 'system',  #계정 정보
#     'password' : '1234', #암호
#     #'dsn' : '127.0.0.1:1521/xe' #접속 DB정보 접속도메인명:포트번호/접속 서비스명
#      #datasorucename 약자
#     'dsn' : 'localhost:1521/xe'
# }

config = {
    'host' : '127.0.0.1',
    'user' : 'root',
    'password' : '1234',
    'database' : 'naver',
    'port' : 3306
}

CN = pymysql.connect(**config) #connect 함수를 ctrl+클릭을 하면 내용을 확인해 볼 수 있다.
cursor = CN.cursor()

def testSelectAll(): #사용자정의 함수를 기술 리턴값X,매개인자X

    msg = "select * from test "
    cursor.execute(msg)
    rows = cursor.fetchall()

#추가
    print(type(rows)) #tuple
    print('cursor.fetchall() 타입',type(cursor.fetchall())) # <class 'tuple'>
    print()
    length = len(rows)
    if length == 0:  # 데이터가 없으면 빠져나가라 (구문 추가)
        return
    for r in rows:
        #print(r[0], r[1], r[2], r[3] )
        print('%4d\t %12s\t %3d\t %8s' %r)
    print('레코드갯수 ', len(rows))

def testInsert(): #작성 10시 20분까지 작성
    # code | name | hit | today
    decode = int(input('코드 입력>> '))
    #추가
    msg = f"select count(*) cnt from test where code={decode}"
    cursor.execute(msg)#sql구문 실행
    cnt = cursor.fetchone()[0]
    print('cnt타입',cnt,type(cnt),)
    
    if cnt != 0:  # 1 이라면 (존재하는 경우)
        print(decode,'코드데이터는 이미 등록된 코드입니다.')
        print('code 정확한 데이터를 입력하세요')
    else:
        dname = input('이름 입력>> ')
        #dhit = int(input('조회수 입력>> '))
        #dsal = input('날짜 입력>> ')
        msg = f"insert into test values({decode},'{dname}',0,now())" #조회수,날짜   
        cursor.execute(msg)#cursor.execute(실행시킬 sql구문)
        CN.commit() #실제 테이블에 반영=>이 구문이 없으면 자동 commit이 안될수 있다.(주의할것.)
        print(decode , ' 저장 성공했습니다') 

def testSelectName():
    testSelectAll()
    print('이름데이터 like조회하세요 ')
    dname = input('이름 입력>> ')
    msg = f"select * from test where name like '%{dname}%'"   
    cursor.execute(msg)#cursor.execute(실행시킬 sql구문)
    rows = cursor.fetchall() #검색된 데이터들
    print()
    length = len(rows)
    if length == 0:  # 데이터가 없으면 빠져나가라 (구문 추가)
        return
    #출력 대상자 양식 출력 print('%4d\t %12s\t %3d\t %8s' %r)
    #print('%4d\t %12s\t %3d\t  %8s' %('코드','이름','조회수','날짜') )
    for r in rows:
        print('%4d\t %12s\t %3d\t %8s' %r)
    print('레코드갯수 ', len(rows))
    print('- ' * 50)


def testDelete():
    testSelectAll()
    print('code데이터 필드로 삭제처리하세요')
    decode = int(input('삭제할 코드 입력>> '))
    #추가
    msg = f"select count(*) cnt from test where code={decode}"
    cursor.execute(msg)#sql구문 실행
    cnt = cursor.fetchone()[0]
    if cnt == 0:  # 
        print(decode,'코드데이터는 미등록 데이터 코드입니다\n')
    else:
        #{ } 사용하면 앞에 f 붙여줘야 된다. 안그러면 소스노출됨
        msg = f"delete from test where code= {decode} " 
        cursor.execute(msg)
        CN.commit() #실제 테이블에 반영
        print(decode , ' 코드데이터 삭제처리 성공했습니다')

def testUpdate(): #수정갱신 update set where code
    testSelectAll()
    decode = int(input('수정대상 코드 입력>> '))
    #추가
    msg = f"select count(*) cnt from test where code={decode}"
    cursor.execute(msg)#sql구문 실행
    cnt = cursor.fetchone()[0]
    if cnt == 0:  # 
        print(decode,'코드데이터는 미등록 데이터 코드입니다\n')
    else:
        # code,name필드 수정대상X title,sal,wdate,grade 4개 필드 수정=>날짜는 입력받지 않는다.
        
        dname = input('수정할 이름 입력>> ')
        dhit = int(input('수정할 조회수 입력>> '))
        msg = f"update test set name='{dname}' ,hit={dhit}, today=now() where code= {decode} " 
        cursor.execute(msg)
        CN.commit() #실제 테이블에 반영
        print(decode , ' 코드 데이터 수정처리 성공했습니다')
       
# testSelectAll()
# time.sleep(1)
# testInsert()
# time.sleep(1)

#=========================================================================
testSelectAll()

while True:
    print()
    sel = int(input('1.신규등록 2.전체출력 3.수정 4.삭제 5.이름조회 9.종료>>>'))
    if sel == 9:
        break
    elif sel == 1:
        print('test테이블 신규드록 처리입니다.')
        testInsert()
        testSelectAll()
    elif sel == 2: #전체출력
        time.sleep(0.5)
        testSelectAll()
    elif sel == 3:  #수정 updtae ~ where
        time.sleep(0.5)
        testUpdate()
        testSelectAll()
    elif sel == 4:  #삭제 delete ~ where
        testDelete()
        testSelectAll()
         
    elif sel == 5:  #이름조회   where name like '%키워드%'
        testSelectName()
    else:
        print('작업번호를 잘못 선택하셨군요\n')

# web웹태그 + css = 방명록,게시판,인스타 작성 가능
# web웹태그 code,name,title,조회수,날짜,이미지
    #댓글기능까지 있으면 완벽한 프로그램
    #로그인 처리 userid,password

print('- ' * 50)
print()
'''

<class 'tuple'>
cursor.fetchall() 타입 <class 'tuple'>

2200 choi 0 2024-09-12 11:25:13
3300 rain 12 2013-03-16 00:00:00
4400 lee 0 2024-09-12 17:18:55
5500 임시 0 2024-09-13 09:51:13
5511 aaa 0 2024-09-13 10:38:59
레코드갯수  5

1.신규등록 2.전체출력 3.수정 4.삭제 5.이름조회 9.종료>>>1
test테이블 신규드록 처리입니다.
코드 입력>> 6600
cnt타입 0 <class 'int'>
이름 입력>> goo
6600  저장 성공했습니다

1.신규등록 2.전체출력 3.수정 4.삭제 5.이름조회 9.종료>>>2
<class 'tuple'>
cursor.fetchall() 타입 <class 'tuple'>

2200 choi 0 2024-09-12 11:25:13
3300 rain 12 2013-03-16 00:00:00
4400 lee 0 2024-09-12 17:18:55
5500 임시 0 2024-09-13 09:51:13
5511 aaa 0 2024-09-13 10:38:59
6600 goo 0 2024-09-13 10:41:18
레코드갯수  6

1.신규등록 2.전체출력 3.수정 4.삭제 5.이름조회 9.종료>>>9
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
1.신규등록 2.전체출력 3.수정 4.삭제 5.이름조회 9.종료>>>5
<class 'tuple'>
cursor.fetchall() 타입 <class 'tuple'>

2200             choi      0     2024-09-12 11:25:13
3300             rain     12     2013-03-16 00:00:00
4400              lee      0     2024-09-12 17:18:55
5500               임시    0     2024-09-13 09:51:13
5511              aaa      0     2024-09-13 10:38:59
6600              goo      0     2024-09-13 10:41:18
7700             test     12     2024-09-13 16:53:53
레코드갯수  7
이름데이터 like조회하세요
이름 입력>> choi

2200             choi      0     2024-09-12 11:25:13
레코드갯수  1
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

1.신규등록 2.전체출력 3.수정 4.삭제 5.이름조회 9.종료>>>3
<class 'tuple'>
cursor.fetchall() 타입 <class 'tuple'>

2200             choi      0     2024-09-12 11:25:13
3300             rain     12     2013-03-16 00:00:00
4400              lee      0     2024-09-12 17:18:55
5500               임시    0     2024-09-13 09:51:13
5511              aaa      0     2024-09-13 10:38:59
6600              goo      0     2024-09-13 10:41:18
7700             test     12     2024-09-13 16:53:53
레코드갯수  7
수정대상 코드 입력>> 5511
수정할 이름 입력>> test2
수정할 조회수 입력>> 2
5511  코드 데이터 수정처리 성공했습니다
<class 'tuple'>
cursor.fetchall() 타입 <class 'tuple'>

2200             choi      0     2024-09-12 11:25:13
3300             rain     12     2013-03-16 00:00:00
4400              lee      0     2024-09-12 17:18:55
5500               임시    0     2024-09-13 09:51:13
5511            test2      2     2024-09-13 17:12:36
6600              goo      0     2024-09-13 10:41:18
7700             test     12     2024-09-13 16:53:53
레코드갯수  7

1.신규등록 2.전체출력 3.수정 4.삭제 5.이름조회 9.종료>>>4
<class 'tuple'>
cursor.fetchall() 타입 <class 'tuple'>

2200             choi      0     2024-09-12 11:25:13
3300             rain     12     2013-03-16 00:00:00
4400              lee      0     2024-09-12 17:18:55
5500               임시    0     2024-09-13 09:51:13
5511            test2      2     2024-09-13 17:12:36
6600              goo      0     2024-09-13 10:41:18
7700             test     12     2024-09-13 16:53:53
레코드갯수  7
code데이터 필드로 삭제처리하세요
삭제할 코드 입력>> 7700
7700  코드데이터 삭제처리 성공했습니다
<class 'tuple'>
cursor.fetchall() 타입 <class 'tuple'>

2200             choi      0     2024-09-12 11:25:13
3300             rain     12     2013-03-16 00:00:00
4400              lee      0     2024-09-12 17:18:55
5500               임시    0     2024-09-13 09:51:13
5511            test2      2     2024-09-13 17:12:36
6600              goo      0     2024-09-13 10:41:18
레코드갯수  6

1.신규등록 2.전체출력 3.수정 4.삭제 5.이름조회 9.종료>>>9
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

PS C:\Mnet\workPython>
PS C:\Mnet\workPython> 

'''