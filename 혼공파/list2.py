#list.append() 리스트 뒤에 요소 추가 
list_a = [1,2,3]
list_a.append(4)
print(list_a)
print()
#list.insert(위치, 요소) 리스트 중간에 요소 추가 
list_a.insert(0,0)
print(list_a)
print()
list_a.extend([5,6,7,8])
print(list_a)
#append insert extend 모두 파괴적함수로 기존 list_a를 변화시킨다
print()
del list_a[0]
print(list_a)
del list_a[0:3]
print(list_a)
list_a.pop(4)
print(list_a)
list_a.remove(7)
print(list_a)