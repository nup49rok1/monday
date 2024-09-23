# 12sosi.py

# mysql test 테이블 + 파이썬

import pymysql
import time
       
config = {
         'host' :'127.0.0.1',
         'user':'root',
         'password':'1234',
         'database':'naver',
         'port':3306
}
CN = pymysql.connect(**config)
cursor = CN.cursor()
print('CN,cursor객체 생성 성공!!!')
print('CN=>',CN,'cursor=>',cursor)
print()

def sosiInsert():
    print('\ntest테이블 신규등록 처리 ')
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
        msg = f"insert into test values({decode},'{dname}',0,now())"    
        cursor.execute(msg)#cursor.execute(실행시킬 sql구문)
        CN.commit() #실제 테이블에 반영=>이 구문이 없으면 자동 commit이 안될수 있다.(주의할것.)
        print(decode , ' 저장 성공했습니다')
        time.sleep(1) #1초      
        
def sosiSelectAll():
    msg = 'select * from test order by code'
    cursor.execute(msg)#sql구문 실행
    rows = cursor.fetchall() #실시간으345로 검색된 데이터들을 가져온다.
    #모아서 처리 하는것=>batch =>ex) 세금,벌금
    #실시간으로 처리하는것 ->fetch
    print('rows타입 ',type(rows)) # 불러오는 데이터는 리스트형태 객체로 받아옴.
    print()
    length = len(rows)
    if length == 0:  # 데이터가 없으면 빠져나가라 (구문 추가)
        return
    #출력 대상자 양식 출력(자릿수 맞춤)
    print('%s\t %s\t %s\t  %5s' %('코드','이름','조회수','날짜') )
    for r in rows:  #데이터들에서 하나씩 행을 꺼내서 출력양식에 맞춰서 출력
        #print(r[0],r[1],r[2],r[3])

        print('%s\t %s\t %s\t %5ss' %r) 
    print('전체데이터 갯수:' , len(rows))#검색된 총갯수 출력
    print('- ' * 50)
    time.sleep(1)

    # rows타입  <class 'tuple'>

# 코드     이름    조회수      날짜
# 2200     choi    0       2024-09-12 11:25:13s
# 3300     rain    12      2013-03-16 00:00:00s
# 5568     hong    0       2024-09-12 11:38:00s
# 7700     snow    0       2011-09-28 00:00:00s
# 9900     cake    12      2024-09-12 11:25:13s
# 전체데이터 갯수: 5


def sosiSelectTitle():
    sosiSelectAll()
    print('제목데이터 like조회하세요 ')
    dtitle = input('제목 입력>> ')
    msg = f"select * from sosi where title like '%{dtitle}%'"   
    cursor.execute(msg)#cursor.execute(실행시킬 sql구문)
    rows = cursor.fetchall() #검색된 데이터들
    print()
    length = len(rows)
    if length == 0:  # 데이터가 없으면 빠져나가라 (구문 추가)
        return
    #출력 대상자 양식 출력
    print('%s\t %s\t %10s\t  %4d\t %6s\t %s' %('코드','이름','제목','급여','날짜','등급') )
    for r in rows:  #데이터들에서 하나씩 행을 꺼내서 출력양식에 맞춰서 출력
        # print(r[0],r[1],r[2],r[3],r[4],r[5])
        print('%4d\t %10s\t %10s\t  %4d\t %6s\t %s' %r) 
    print('전체데이터 갯수:' , len(rows))#검색된 총갯수 출력
    print('- ' * 50)
    time.sleep(1)
    #sosiSelectAll()

# def sosiDelete():
#     pass
#     print('code조회후 삭제처리하세요')
#view ->appearance->minimap 해제 
def sosiDelete():
    sosiSelectAll()
    print('code데이터 필드로 삭제처리하세요')
    decode = int(input('삭제코드 입력>> '))
    #추가
    msg = f"select count(*) cnt from sosi where code={decode}"
    cursor.execute(msg)#sql구문 실행
    cnt = cursor.fetchone()[0]
    if cnt == 0:  # 
        print(decode,'코드데이터는 미등록 데이터 코드입니다\n')
    else:
        #{ } 사용하면 앞에 f 붙여줘야 된다. 안그러면 소스노출됨
        msg = f"delete from sosi where code= {decode} " 
        cursor.execute(msg)
        CN.commit() #실제 테이블에 반영
        print(decode , ' 코드데이터 삭제처리 성공했습니다')
        time.sleep(1)
    sosiSelectAll()

def sosiUpdate(): #수정갱신 update set where code
    sosiSelectAll()
    decode = int(input('수정대상 코드 입력>> '))
    #추가
    msg = f"select count(*) cnt from sosi where code={decode}"
    cursor.execute(msg)#sql구문 실행
    cnt = cursor.fetchone()[0]
    if cnt == 0:  # 
        print(decode,'코드데이터는 미등록 데이터 코드입니다\n')
    else:
        # code,name필드 수정대상X title,sal,wdate,grade 4개 필드 수정=>날짜는 입력받지 않는다.
        
        dtitle = input('수정제목 입력>> ')
        dsal = int(input('수정급여 입력>> '))
        dgrade = input('수정등급 입력>> ')
        msg = f"update sosi set title='{dtitle}' ,sal={dsal}, wdate=sysdate, grade='{dgrade}'  where code= {decode} " 
        cursor.execute(msg)
        CN.commit() #실제 테이블에 반영
        print(decode , ' 코드데이터 수정처리 성공했습니다')
        time.sleep(1)
        sosiSelectAll()

#추가
# 클래스 작성은 생략가능, 처리단위를 함수작성 + try ~ except 예외처리
while True:
    print('1 등록 2.전체 출력 3.수정 4.삭제 5.제목조회 9 종류>>>')
    #sel = int(input('1 등록 2.전체 출력 3.수정 4.삭제 5.제목조회 9 종류>>>'))
    break
    # if sel == 9:
    #     break
    # elif
# sosiSelectAll() 십만건이라면 보여주고 등록하기가 쉽지 않다.
# sosiInsert() #conn.commit()을 잠시 주석 처리 한다.->메모리에 저장=>실제 테이블X
# #time.sleep(1)

print()
#추가
sosiSelectAll()
sosiInsert()
sosiSelectAll()
#sosiDelete()
#sosiUpdate()
#sosiSelectTitle()
print()

#sosiDelete() #삭제 처리 3:10분 까지 실습
#sosiInsert()
# time.sleep(0.5)

'''



'''