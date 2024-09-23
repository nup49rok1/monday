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

for k in score_dict:
    print(type(score_dict[k]))

'''
[100, 60]
[90, 77]
[82, 34]
[90, 34]
'''
print('--' *30)

for k in score_dict:
    #print(score_dict[k])
    for v in score_dict[k]:
        print(v)
'''
100
60
90
77
82
34
90
34
'''
for k in score_dict:
    #print(score_dict[k])
    for v in score_dict[k]:
        list_kor.append(v)
        list_eng.append(v)

for a in list_kor:
    print('a=>',a)

for b in list_eng:
    print('b=>',b)

'''
아래처럼 출력
# 4시 10분 시작  총점,평균

김자바 160 80
이합격 167 83
강감찬 116 58
박이썬 124 62
'''
name=['김자바','이합격','강감찬','박이썬']