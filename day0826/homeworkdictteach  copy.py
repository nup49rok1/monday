#homeworkdict.py

#김자바, 이합격, 박이썬
#aaa,bbb,ccc kim lee goo

score_dict={
    '김자바':[100,60],
    '이합격':[90,77],
    'lee':[82,34],
    'park':[90,34]
}

list_kor = []
list_eng = []

#추가
names = []

for name in score_dict.keys():
    names.append(name)

print(names)
print('--'*30)


for data in score_dict.values():
    #print(data[0],data[1])
    list_kor.append(data[0])
    list_eng.append(data[1])
    
    hap_kor = sum(list_kor)
    hap_eng = sum(list_eng)

    print('국어점수',hap_kor,hap_kor//2)
    print('영어점수',hap_eng,hap_eng//2)

    #추가
    #score=zip(name,list_kor,list_eng)
    #print('score=>',score)
     
        
'''

'''
print('--' *30)


'''
아래처럼 출력
# 4시 10분 시작  총점,평균

김자바 160 80
이합격 167 83
강감찬 116 58
박이썬 124 62
'''
#name=['김자바','이합격','강감찬','박이썬']