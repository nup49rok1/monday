# homeworkmilk.py
# 2024. 08. 26 (writer: B. Lim)

apart = [
    [101, 102, 103, 104],
    [201, 202, 203, 204],
    [301, 302, 303, 304],
    [401, 402, 403, 404],
]

unpaid = [101, 204, 302, 403]

print('5조 조장님')
for i in apart:
    for j in i:
        if j in unpaid:
            print(j,"delivery stop")
        else:
            print(j,"delivery continue")
    print()
