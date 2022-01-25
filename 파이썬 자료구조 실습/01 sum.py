# a부터 b까지 정수의 합 구하기 for문 

a = int(input('정수 a 입력 : '))
b = int(input('정수 b 입력 : '))

if a > b : 
    a, b  = b , a  # 스왑을 통한 오름차순 정렬 5 , 1 -> 1 , 5

sum = 0 
for i in range(a, b+1) :
    sum += i

print(f'{a} 부터{b}까지 정수의 합은 {sum}이다 .')