# *개를 n개 출력하되 w개마다 줄바꿈

n = int(input('몇개를 출력할까요 ? : '))
w = int(input('몇개마다 줄바꿈 할까요 ? : '))

for i in range(n):   # n번 반복
    print('*', end='')
    if i%w == w -1 :  # n번 판단 
        print()       # w-1 일때 줄바꿈


if n % w:            # 나머지 o 
    print()          # for 문 밖에서 줄바꿈


# *개를 n개 출력하되 w개마다 줄바꿈2 

n2 = int(input('몇개를 출력할까요 ?2 : '))
w2 = int(input('몇개마다 줄바꿈 할까요 ?2 : '))

for _ in range(n // w):   # n //w 번 반복
    print('*' * w)   # w개 출력

rest = n % w         # 나머지
if rest : 
    print('*' * rest) # 나머지 만큼 출력 

 
