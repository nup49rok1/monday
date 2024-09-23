#09set.py

# 셋 set {  }
# 순서 X ,중복 X
# append(),insert() == add() 대체
# 전체 삭제 clear()

wish = { } #선언하면 set 아니라 dict로 인식하기때문에 에러가 발생이 된다.
'''
AttributeError: 'dict' object has no attribute 'add'
'''
wish.add('엘쥐')
wish.add('kt')
wish.add(37.081)
wish.add('엘쥐')
wish.add('엘쥐')
print(wish)
print()