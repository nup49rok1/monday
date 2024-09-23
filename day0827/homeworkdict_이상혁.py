# homeworkdict.py

score_dict = {
    'Witkiewicz' : [100,60],
    'Dostoevsky' : [90,77],
    'Tolstoy' : [82,34],
    'Navokov' : [90,34]
}

list_kor = []
list_eng = []

for key in score_dict:
    list_kor.append(score_dict[key][0])
    list_eng.append(score_dict[key][1])

for k in range(4):  #0~3까지
    print(f'{list(score_dict.keys())[k]} {list_kor[k]+list_eng[k]} {(list_kor[k]+list_eng[k])//2}')

# 아래처럼 출력
# Witkiewiz 160 80
# Dostoevsky 167 83
# Tolstoy 116 58
# Navokov 124 62