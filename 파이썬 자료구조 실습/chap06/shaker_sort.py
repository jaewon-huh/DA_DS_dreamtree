# 셰이커 정렬 알고맂므 
from typing import MutableSequence 

def shaker_sort(a :MutableSequence) :
    
    left = 0                # --> 방향 스캔 왼 오
    right = len(a) -1       # <-- 방향 스캔 오 왼 

    last = right    
    # 배열  9 1 3 4 6 8 7 
    while left < right : 
        for j in range(right, left , -1) :          # <--- 방향 스캔 6 5 4 3 2 1 0 , j : 6
            if a[j-1] > a[j] :                      # a[5] > a[6]  = 8 > 7
                a[j-1] , a[j] = a[j], a[j-1]        # 9 1 3 4 6 7 8 
                last = j                            # last = 6      -> 최종 1 9 3 4 6  7 8 , last = 1  
        left = last                                 # left 1 

        # 짝수 패스                                 # 배열 1 9 3 4 6 7 8 
        for i in range(left, right) :               # 1 ~ 6
            if a[j] > a[j+1]  :                     # 1 > 2  
                a[j] , a[j+1] = a[j+1] ,a[j]        # swap 1 3 9 4 6 7 8
                last = j                            # last 1  -> 최종 1 3 4 6 7 8 9
        right = last                                # right = 5 
    

if __name__ == '__main__':
    print('셰이커 정렬을 수행합니다')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num    # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}] : '))

    shaker_sort(x)      # 배열 x를 단순 교환 정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')