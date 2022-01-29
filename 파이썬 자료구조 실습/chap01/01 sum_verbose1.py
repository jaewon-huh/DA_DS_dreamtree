# 반복 과정에서 조건 판단하기 
# a부터 b까지 정수의 합
# '합을 구하는 과정'과 '최종값'

a = int(input('정수 a 입력 : '))
b = int(input('정수 b 입력 : '))

if a > b : 
    a, b = b,a 
sum = 0
for i in range(a, b+1) :
    if i < b :                  #i 가 b 보다 작으면 합을 구하는 과정 
        print(f'{i} +', end='')
    else :                      # i = b이면 최종값 출력을 위해 i = 출력
        print(f'{i} = ', end ='')
    sum += i                    # sum에 i를 더함 .

print(sum)
# a = 2 , b = 4   i = range(2,4+1)  2 + 3+ 4 = sum 
# problem : for문에서 반복하는 동안  i<b 행만 b-a번 실행되고 else문은 단 한번 실행됨
# -> for 문안에 if문을 제외하고 별도로 

# a부터 b까지 정수의 합 구하기2 .


a2 = int(input('정수 a2 입력 : '))
b2 = int(input('정수 b2 입력 : '))

if a2 > b2 : 
    a2, b2 = b2,a2 

sum2 = 0
for i in range(a2,b2) :   # a ~ b-1 까지의 합
    print(f'{i} +', end='')
    sum2 += i        
print(f'{b} = ', end = '')
sum2 += b

print(sum2)