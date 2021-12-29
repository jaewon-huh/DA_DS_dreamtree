i = 0 
while i < 10 : 
    print(i , end = " ")
    i +=1
# 상태를 기반으로 반복하기 
numbers = [1,2,1,2,1,2]
while 1 in numbers :
    numbers.remove(1)
    print(numbers)
# 시간을 기반으로 반복하기 
# break 키워드 , continue 키워드 
i = 0 
while True:
    print("{}번째 반복문입니다".format(i))
    i += 1
    input_text = input("> 종료하시겠습니까 (y)")
    if input_text in ["y"," Y"]:
        print("반복을 종료합니다")
        break
numbers = [5,15,6,20,7,25]
for number in numbers :
    #number가 10보다 작으면 다음 반복으로 넘어 갑니다 .
    if number < 10 :
        continue
    print(number)