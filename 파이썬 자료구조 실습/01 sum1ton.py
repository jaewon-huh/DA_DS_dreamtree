# 1부터 n까지 정수 합 while

n = int(input('n값을 입력 :'))

# 준비단계
sum = 0 
i = 1           
# 루프 
while i <=n :
    sum +=i 
    i += 1

print(f'1부터 {n}까지 정수의 합은 {sum}이다. ')    

# 1부터 n까지 합 for (변수가 1개 - for)

n2 = int(input('n값을 입력 :'))

# 준비단계
sum2 = 0 
for i in range(1,n2+1) : 
    sum += i 

print(f'1부터 {n2}까지 정수의 합은 {sum2}이다. ')        

# 가우스 식 표현 sum = n * (n+1) // 2
