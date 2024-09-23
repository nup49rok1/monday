# 12sosi과제.py

# 오라클 sosi테이블 + 파이썬
import pandas as pd
import cx_Oracle  
#추가
import sys

# pip install oracledb 
# import oracledb  #에러가 발생이 될 가능성이 있다.(버전차이?)  os가 11버전에서 에러발생?  
import time #함수 호출 사이의 간격을 주기위해서 import
       
#dic자료(DB접속 정보)
config = {
    'user' : 'system',  #계정 정보
    'password' : '1234', #암호
    #'dsn' : '127.0.0.1:1521/xe' #접속 DB정보 접속도메인명:포트번호/접속 서비스명
     #datasorucename 약자
    'dsn' : 'localhost:1521/xe'
}

# conn = oracledb.connect(**config) #오류
# conn = oracledb.connect(user='system', password='1234', dsn='127.0.0.1:1521/xe') #오류
# connect(DB정보를 받아서) conn객체를 얻어옴.
conn = cx_Oracle.connect(**config)  #dict매개변수로 전달
print('config 매개인자 타입',type(config)) #config 매개인자 타입 <class 'dict'>
# conn = cx_Oracle.connect(user='system', password='1234', dsn='127.0.0.1:1521/xe')
cursor = conn.cursor() #conn객체를 통한 SQL구문을 실행시킬 cursor객체 얻어옴.

print("database version: ", conn.version)
print("oracle connect ok success")
print()

def sosiInsert():
    print('\nsosi테이블 신규등록 처리 ')
    '''
    while True:
        num = int(input("1~10 숫자 이력:"))
        if num < 1 or num > 10:
            print("잘못 입력하셨습니다. 다시 입력해주세요")
            continue
        break
    '''
    while True:
        dcode = int(input('코드 입력>> '))
    #추가
        msg = f"select count(*) from sosi where code={dcode}"
        cursor.execute(msg)#sql구문 실행
        row = cursor.fetchone()
        print('row=>',type(row),row)
    #if row == 0:
        #for r in row:
        if row[0] == 1:
            print(str(dcode)+'은 중복된 code값입니다.')
            continue
    #코드 데이터 입력후 code 필드값 중복체크 / 함수 탈출 /재입력
    #1 신규등록 2 전체 출력 3.수정 4.삭제 5.제목조회  6.종료
        else:
            dname = input('이름 입력>> ')
            dtitle = input('제목 입력>> ')
            dsal = int(input('급여 입력>> '))
            msg = f"insert into sosi values({dcode},'{dname}','{dtitle}',{dsal}, sysdate, 'D')"    
            cursor.execute(msg)#cursor.execute(실행시킬 sql구문)
            conn.commit() #실제 테이블에 반영
            print(dcode , ' 저장 성공했습니다')
            time.sleep(1) #1초 
            sosiSelectAll()
            #sys.exit()
            main()
            

def sosiSelectAll():
    msg = 'select * from sosi order by code'
    cursor.execute(msg)#sql구문 실행
    rows = cursor.fetchall() #실시간으로 검색된 데이터들을 가져온다.
    #모아서 처리 하는것=>batch =>ex) 세금,벌금
    #실시간으로 처리하는것 ->fetch
    print('rows타입 ', type(rows)) # 불러오는 데이터는 리스트형태 객체로 받아옴.
    print()
    #출력 대상자 양식 출력(자릿수 맞춤)
    print('%s\t %8s\t %8s\t  %4s\t %6s\t %s' %('코드','이름','제목','급여','날짜','등급') )
    for r in rows:  #데이터들에서 하나씩 행을 꺼내서 출력양식에 맞춰서 출력
        #print(r[0],r[1],r[2],r[3],r[4],r[5])
        '''
        3300 three cake 96.2 2024-09-09 09:25:03 D
        4400 테스트 python 93.0 2024-09-09 09:41:26 D
        5576 java you 54.96 2024-09-05 11:22:19 B
        '''
        #자리수를 맞춰서 출력을 하는것이 변별력을 위해서 더 좋은 출력형태임
        print('%4d\t %10s\t %10s\t  %4d\t %6s\t %s' %r) 
    print('전체데이터 갯수:' , len(rows))#검색된 총갯수 출력
    print('- ' * 50)
    time.sleep(1)

    # 코드           이름            제목       급여             날짜        등급
    # 3300          three            cake         96   2024-09-09 09:25:03     D
    # 4400            테스트       python         93   2024-09-09 09:41:26     D
    # 5576           java             you         54   2024-09-05 11:22:19     B
    # 전체데이터 갯수: 3


# def sosiSelectTitle():
#     pass
#     print('제목데이터 like조회하세요 ')

def sosiSelectTitle():
    print('제목데이터 like조회하세요 ')
    dtitle = input('제목 입력>> ')
    msg = f"select * from sosi where title like '%{dtitle}%'"   
    cursor.execute(msg)#cursor.execute(실행시킬 sql구문)
    rows = cursor.fetchall() #검색된 데이터들
    print()
    #출력 대상자 양식 출력
    print('%s\t %s\t %10s\t  %4s\t %6s\t %s' %('코드','이름','제목','급여','날짜','등급') )
    for r in rows:  #데이터들에서 하나씩 행을 꺼내서 출력양식에 맞춰서 출력
        # print(r[0],r[1],r[2],r[3],r[4],r[5])
        print('%4d\t %10s\t %10s\t  %4d\t %6s\t %s' %r) 
    print('전체데이터 갯수:' , len(rows))#검색된 총갯수 출력
    print('- ' * 50)
    time.sleep(1)

# def sosiDelete():
#     pass
#     print('code조회후 삭제처리하세요')

def sosiEditupdate():
    print('code조회후 수정 처리하세요')
    
    while True:
        dcode = int(input('수정할 코드 입력>> '))
        msg = f"select count(*) from sosi where code={dcode}"
        cursor.execute(msg)#sql구문 실행
        row = cursor.fetchone()
        print('row=>',type(row),row)
        if row[0] == 0:
            print(str(dcode)+'은 수정할 수 없는 code값입니다. 다시 입력하세요')
            continue
        else:
            # code,name필드 수정대상X title,sal,wdate,grade 4개 필드 수정=>날짜는 입력받지 않는다.
            dtitle = input('수정제목 입력>> ')
            dsal = int(input('수정급여 입력>> '))
            dgrade = input('수정등급 입력>> ')
            msg = f"update sosi set title='{dtitle}' ,sal={dsal}, wdate=sysdate, grade='{dgrade}'  where code= {dcode} " 
            cursor.execute(msg)
            conn.commit() #실제 테이블에 반영
            print(dcode , ' 수정 성공했습니다')
            time.sleep(1)
            sosiSelectAll()
            #sys.exit()
            main()

def sosiDelete():
    print('code조회후 삭제처리하세요')
    
    while True:
        dcode = int(input('코드 입력>> '))
        msg = f"select count(*) from sosi where code={dcode}"
        cursor.execute(msg)#sql구문 실행
        row = cursor.fetchone()
        print('row=>',type(row),row)
        if row[0] == 0:
            print(str(dcode)+'은 없는 code값입니다. 다시 입력하세요')
            continue
        else:
            msg = f"delete from sosi where code= {dcode} "
            cursor.execute(msg)#cursor.execute(실행시킬 sql구문)
            conn.commit() #실제 테이블에 반영
            print(dcode , ' 삭제 성공했습니다')
            time.sleep(1)
            sosiSelectAll()
            #sys.exit()
            main()

print()


def menuExit():
    print('DB연결 프로그램을 종료합니다.')
    sys.exit()

def main():
    while True:
        print()
    #1 신규등록 2 전체 출력 3.수정 4.삭제 5.제목조회  6.종료
        num=int(input('1.신규등록 2.전체출력 3.수정 4.삭제 5.제목조회 9.종료>>'))
        if num == 9: menuExit()
        elif num == 1: sosiInsert()
        elif num == 2: sosiSelectAll()
        elif num == 3: sosiEditupdate()
        elif num == 4: sosiDelete()
        elif num == 5: sosiSelectTitle()
        else:print('처리번호를 잘못 입력하셨네요\n')

main()
'''

config 매개인자 타입 <class 'dict'>
database version:  11.2.0.2.0
oracle connect ok success


1.신규등록 2.전체출력 3.수정 4.삭제 5.제목조회 9.종료>>2
rows타입  <class 'list'>

코드           이름              제목       급여             날짜        등급
1100         python           test2         34   2024-09-09 12:39:47     D
2200           five             ten         41   2024-09-09 11:37:08     D
3300          three           three         96   2024-09-09 09:25:03     D
4400            테스트       summer         93   2024-09-09 09:41:26     D
5576           java            snow         54   2024-09-05 11:22:19     B
6600            lee            rain         31   2024-09-09 11:37:56     D
7700            임시2         seven         45   2024-09-09 12:11:18     D
전체데이터 갯수: 7
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

1.신규등록 2.전체출력 3.수정 4.삭제 5.제목조회 9.종료>>3
code조회후 수정 처리하세요
수정할 코드 입력>> 9900
row=> <class 'tuple'> (0,)
9900은 수정할 수 없는 code값입니다. 다시 입력하세요
수정할 코드 입력>> 7700
row=> <class 'tuple'> (1,)
수정할 급여를 입력하세요66
7700  수정 성공했습니다
rows타입  <class 'list'>

코드           이름              제목       급여             날짜        등급
1100         python           test2         34   2024-09-09 12:39:47     D
2200           five             ten         41   2024-09-09 11:37:08     D
3300          three           three         96   2024-09-09 09:25:03     D
4400            테스트       summer         93   2024-09-09 09:41:26     D
5576           java            snow         54   2024-09-05 11:22:19     B
6600            lee            rain         31   2024-09-09 11:37:56     D
7700            임시2         seven         66   2024-09-09 12:11:18     D
전체데이터 갯수: 7
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

1.신규등록 2.전체출력 3.수정 4.삭제 5.제목조회 9.종료>>
'''