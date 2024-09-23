#08set.py

# 셋 set {  }
# 순서 X ,중복 X
# append(),insert() == add() 대체
# 전체 삭제 clear()

wish = {'대',126.723, 37.081,'대',37.081,126.159,'대저'}
print(wish) #{'대저', 37.081, '대', 126.159, 126.723}
wish.add('엘쥐')
wish.add('kt')
wish.add('엘쥐')
wish.add('엘쥐')
print(wish)#{126.159, 'kt', 37.081, '대저', '엘쥐', 126.723, '대'}
print()