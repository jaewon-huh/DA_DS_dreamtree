key_list = ["name", " hp", "mp", "level"]
value_list = ["기사", 200, 30, 5]
character = {}
# 짝 지은후 딕셔너리를 선언 딕[새로운 키] = 새로운 값
for i in range(len(key_list)) :
    character[key_list[i]] = value_list[i]
    # 리스트 2개를 함께 반복을 도는 경우 , i & range 함수 이용 
print(character)

# 숫자를 하나씩 증가시켜가며 더할 때 몇을 더하면 10000 초과 
print()
limit = 10000
i =1 
# 더한 값을 선언한다 
sum_value = 0
while sum_value <limit :
    sum_value += i  # 0부터 더해감 
    i  += 1         # +1  , +2 ,+3 ...
print("{}을 더할때 {}을 넘으며 그때의 값은 {}".format(i,limit,sum_value))

print()
max_value = 0 
a = 0 
b = 0
for i in range(1,100) :
    j = 100- i
    #최대값 구하기 
    if max_value < i * j :
        max_value = i * j
        a = i
        b = j
# a = 50 b =50 일때 다음 차례 i= 51 , j=49  50*50 < 51*49 를 만족 하지 않음 따라서 밑의 조건문 실행 x 그대로 종료 
print("최대가 되는 경우 : {} * {} = {}".format(a,b,max_value))