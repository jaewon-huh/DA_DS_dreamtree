# 넓이가 area인 직사각형에서 변의 길이 나열 

area= int(input('직사각형의 넓이를 입력하시오 :'))

for i in range(1, area +1) :
    if i * i > area : break     
    if area % i : continue      # 나누어 떨어지지 않으면 다음 i 
    print(f'{i} x {area // i }')

import random 
n = int(input('난수의 개수 입력 : '))

for _ in range(n) :                         # 조건식
    r = random.randint(10,50)
    print(r, end =' ')                      # 명령문 
    if r == 13 :                            # break
        print('\n 프로그램을 중단 합니다.')
        break
else :                                     # else문 
    print('\n 난수생성을 종료합니다.')    
