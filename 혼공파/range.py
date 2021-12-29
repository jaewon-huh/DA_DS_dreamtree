for i in range(0,10) :
    print(i)
print()
#반대로 반복하기 
for i in range(9,0-1,-1) : 
    print(i)
for i in reversed(range(0,10)) :  #reversed(array) 매개변수에 리스트도 가능 
    print(i)
print()
array = [273,52,103,32,57]
# for 반복문 : 리스트와 범위 조합하기 
for i in range(len(array)) : 
    print("{} 번째 반복 {}".format(i,array[i]))
for i, element in enumerate(array) : 
    print( "{} : {} ".format(i,element))