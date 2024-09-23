# 12sosi.py

# 오라클 sosi테이블 + 파이썬
import pandas as pd
import cx_Oracle  
#추가

import time #함수 호출 사이의 간격을 주기위해서 import
       
#dic자료(DB접속 정보)
config = {
    'user' : 'system',  #계정 정보
    'password' : '1234', #암호
    #'dsn' : '127.0.0.1:1521/xe' #접속 DB정보 접속도메인명:포트번호/접속 서비스명
     #datasorucename 약자
    'dsn' : 'localhost:1521/xe'
}


CN = cx_Oracle.connect(**config)  #dict매개변수로 전달
print('config 매개인자 타입',type(config)) #config 매개인자 타입 <class 'dict'>
# conn = cx_Oracle.connect(user='system', password='1234', dsn='127.0.0.1:1521/xe')
cursor = CN.cursor() #conn객체를 통한 SQL구문을 실행시킬 cursor객체 얻어옴.

print("database version: ", CN.version)
print("oracle connect ok success")
print()

def sosiInsert():
    print('\nsosi테이블 신규등록 처리 ')
    decode = int(input('코드 입력>> '))
    #추가
    msg = f"select count(*) cnt from sosi where code={decode}"
    cursor.execute(msg)#sql구문 실행
    cnt = cursor.fetchone()[0]
    print('cnt타입',cnt,type(cnt),)
    
    #코드 데이터 입력후 code 필드값 중복체크 / 함수 탈출 /재입력
    #1 신규등록 2 전체 출력 3.수정 4.삭제 5.제목조회  6.종료
    #잠시 주석 ctrl+/  블럭설정 전체주석 처리
    if cnt != 0:  # 1 이라면 (존재하는 경우)
        print(decode,'코드데이터는 이미 등록된 코드입니다.')
        print('code 정확한 데이터를 입력하세요')
        #break   #while,for 반복문이 없어서 break 단독 기술 에러
        return #return 명령어 단독기술하면 함수 탈출
        print('우리나라 db처리 관련 없는 처리 구현')
        print('대한민국 db처리 관련 없는 처리 구현')
    else:
        dname = input('이름 입력>> ')
        dtitle = input('제목 입력>> ')
        dsal = int(input('급여 입력>> '))
        msg = f"insert into sosi values({decode},'{dname}','{dtitle}',{dsal}, sysdate, 'D')"    
        cursor.execute(msg)#cursor.execute(실행시킬 sql구문)
        CN.commit() #실제 테이블에 반영=>이 구문이 없으면 자동 commit이 안될수 있다.(주의할것.)
        print(decode , ' 저장 성공했습니다')
        time.sleep(1) #1초 
        
        
def sosiSelectAll():
    msg = 'select * from sosi order by code'
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
    print('%s\t %8s\t %10s\t  %4s\t %6s\t %s' %('코드','이름','제목','급여','날짜','등급') )
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
    print('%s\t %s\t %10s\t  %4s\t %6s\t %s' %('코드','이름','제목','급여','날짜','등급') )
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
#sosiInsert()
#sosiDelete()
#sosiUpdate()
sosiSelectTitle()

print()

#sosiDelete() #삭제 처리 3:10분 까지 실습
#sosiInsert()
# time.sleep(0.5)

'''
처음 작성 코드 09월 09일 월요일

# 12sosi.py

# 오라클 sosi테이블 + 파이썬
import os
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
CN = cx_Oracle.connect(**config)  #dict매개변수로 전달
print('config 매개인자 타입',type(config)) #config 매개인자 타입 <class 'dict'>
# conn = cx_Oracle.connect(user='system', password='1234', dsn='127.0.0.1:1521/xe')
cursor = conn.cursor() #conn객체를 통한 SQL구문을 실행시킬 cursor객체 얻어옴.

print("database version: ", CN.version)
print("oracle connect ok success")
print()


def sosiInsert():
    print('\nsosi테이블 신규등록 처리 ')
    #
    while True:
        num = int(input("1~10 숫자 이력:"))
        if num < 1 or num > 10:
            print("잘못 입력하셨습니다. 다시 입력해주세요")
            continue
        break
    #
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
            print(str(dcode)+'은 중복된 code값입니다.\n다시 입력하세요')
            continue
            #break
        #break
    #코드 데이터 입력후 code 필드값 중복체크 / 함수 탈출 /재입력
    #1 신규등록 2 전체 출력 3.수정 4.삭제 5.제목조회  6.종료
        else:
            dname = input('이름 입력>> ')
            dtitle = input('제목 입력>> ')
            dsal = int(input('급여 입력>> '))
            msg = f"insert into sosi values({dcode},'{dname}','{dtitle}',{dsal}, sysdate, 'D')"    
            cursor.execute(msg)#cursor.execute(실행시킬 sql구문)
            CN.commit() #실제 테이블에 반영
            print(dcode , ' 저장 성공했습니다')
            time.sleep(1) #1초 
            sosiSelectAll()
            sys.exit()
            

def sosiSelectAll():
    msg = 'select * from sosi order by code'
    cursor.execute(msg)#sql구문 실행
    rows = cursor.fetchall() #실시간으로 검색된 데이터들을 가져온다.
    #모아서 처리 하는것=>batch =>ex) 세금,벌금
    #실시간으로 처리하는것 ->fetch
    print('rows타입 ', type(rows)) # 불러오는 데이터는 리스트형태 객체로 받아옴.
    print()
    #출력 대상자 양식 출력(자릿수 맞춤)
    print('%s\t %8s\t %10s\t  %4s\t %6s\t %s' %('코드','이름','제목','급여','날짜','등급') )
    for r in rows:  #데이터들에서 하나씩 행을 꺼내서 출력양식에 맞춰서 출력
        #print(r[0],r[1],r[2],r[3],r[4],r[5])
        
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

def sosiDelete():
    print('code조회후 삭제처리하세요')
    dcode = int(input('코드 입력>> '))
    #추가
    msg = f"delete from sosi where code= {dcode} "
    #msg = f"insert into sosi values({dcode},'{dname}','{dtitle}',{dsal}, sysdate, 'D')"    
    cursor.execute(msg)#cursor.execute(실행시킬 sql구문)
    conn.commit() #실제 테이블에 반영
    print(dcode , ' 삭제 성공했습니다')
    time.sleep(1)

#추가
#sosiSelectTitle()
sosiSelectAll()
sosiInsert()
sosiSelectAll()
#sosiDelete()
#sosiSelectAll()

# time.sleep(0.5)
# sosiSelectAll()
print()


#추가
#sosiSelectAll()
#sosiInsert()
# time.sleep(0.5)
# sosiSelectAll()
# print()



'''