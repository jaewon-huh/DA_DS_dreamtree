# 셸 정렬 알고리즘 구현 

from typing import MutableSequence 

def shell_sort(a : MutableSequence) :
    n = len(a)
    h = n // 2  #몫 연산자  8 -> 4 -> 2 -> 1 

    while h > 0 : 
        for i in range(h ,n) :          # n = 8 -> range(4 , 8) 4 5 6 7
            j = i-h                     # 0 1 2 3 
            tmp = a[i]
            while j >= 0 and tmp < a[j] :  #앞 놈이 더 큰 값이면 a[i ] = a[4] = tmp = 7 , a[j] = a[0] = 8
                a[j+h] = a[j]              # a[4] = a[0] = 8 
                j -=h                      # j = -4
            a[j+h] = tmp                   # a[0] = 7       스왑 참 어렵네 . 

        h //= 2   # 다음 h  업데이트    

if __name__ == '__main__':
    print('셸 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num  # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    shell_sort(x)  # 배열 x를 셸 정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')        