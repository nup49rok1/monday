import datetime
import time

# 문제 1: 성별 체크 (1, 3 = 남자 / 2, 4 = 여자)
# 문제 2: 생일
# 문제 3: 나이계산 2024 - ????


def checkLen(first, second):
    if len(first) == 6 and len(second) == 7:
        printInfo(first, second)

    else:
        print("올바르지 않은 주민등록번호입니다.-checkLen")


def checkGen(second):
    if second[0] == "1" or second[0] == "3":
        gen = "남자"
    elif second[0] == "2" or second[0] == "4":
        gen = "여자"
    else:
        print("올바르지 않은 주민등록번호 입니다.-checkGen")

    return gen
    # print("성별 : ", gen)


def getBirthday(first):
    month = first[2:4]
    day = first[4:6]
    birthday = "{}월 {}일".format(month, day)

    return birthday
    # print("생일 : ", birthday)


def getAge(first, second):
    if second[0] == "1" or second[0] == "2":
        year = "19" + first[0:2]
    elif second[0] == "3" or second[0] == "4":
        year = "20" + first[0:2]
    else:
        print("올바르지 않은 주민등록번호 입니다.-getAge")

    now = time.localtime()
    nowYear = now.tm_year

    age = nowYear - int(year)
    return age
    # print("나이 : ", age)


def printInfo(first, second):
    try:
        birthday = getBirthday(first)
        gen = checkGen(second)
        age = getAge(first, second)
        info = "당신은 {}살 {}이고, 생일은 {}입니다.".format(age, gen, birthday)
        print(info)
    except:
        print("올바르지 않은 주민등록번호입니다.")


def main():
    jumin = input("당신의 주민등록 번호를 입력해주세요(-포함) >> ")
    if "-" in jumin:
        jum1 = jumin.split("-")[0]
        jum2 = jumin.split("-")[1]
        checkLen(jum1, jum2)
    else:
        print("올바르지 않은 주민등록번호입니다.-main")


while True:
    main()
