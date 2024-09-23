#09dictreturn

# 함수의 리턴값을 1개이상 처리
# 함수의 매개인자 1개이상 처리  (* args)
# 함수의 매개인자 딕트, 리턴값은 여러개
def score_procedure(sd):

    kor_list = []
    eng_list = []
    #return 국어점수 합계, 영어점수합계,국어점수 평균,영어점수 평균
    # sum(),len() , // 몫 추출해주는 연산기호 이용
    print(type(sd))

    for data in sd.values():
        print(data)#전달받은 데이터의 자료형을 확인
        kor_list.append(data[0])
        eng_list.append(data[1])

    kor_hap = sum(kor_list)
    eng_hap = sum(eng_list)
    kor_avg = kor_hap//len(kor_list)
    eng_avg = eng_hap//len(eng_list)

    return kor_hap,eng_hap,kor_avg,eng_avg
    #return 240,175,84,90
    
    #3시 45분까지...


score = {
    'kim' : [100,60],
    'lee' : [90,77],
    'goo' : [82,34]
    }

a,b,c,d = score_procedure(score) #score 매개변수 전달
print('국어 총점 ',a)
print('영어 총점 ',b)
print('국어 평균 ',c)
print('영어 평균 ',d)
#score_procedure(score)
'''
<class 'dict'>
국어 총점  272
영어 총점  171
국어 평균  90
영어 평균  57
'''