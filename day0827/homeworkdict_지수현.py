#homeworkdict.py

score_dict = {
    '김자바':[100,60],
    '이합격':[90,77],
    '강감찬':[82, 34],
    '박이썬':[90,34],
 }


#리스트를 사용하지 않고 짧게 구현
for key in score_dict :
    print(key, sum(score_dict[key]), 
                   sum(score_dict[key])//len(score_dict[key]))



# 아래처럼 출력하시오.
# 김자바 160  80
# 이합격 167  83
# 강감찬 116  58
# 박이썬 124  62
