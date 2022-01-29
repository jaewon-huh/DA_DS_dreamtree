# 버블정렬 알고리즘 

from typing import MutableSequence

def bubble_sort(a: MutableSequence) :
    n = len(a)
    for i in range(n-1) :                 # 5 -> 0 1 2 3 4
        exchng = 0      # 교환횟수 (패스에서 교환횟수가 0이면  다음 패스 불필요 )
        for j in range (0, n-i-1) :     # i = 0 , 0  1 2 3 4       
            if a[j] > a[j+1] :
                a[j], a[j+1] = a[j+1] , a[j]
                exchng += 1
        if exchng == 0 :
            break


if __name__ == '__main__':
    print('버블 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num  # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    bubble_sort(x)  # 배열 x를 단순 삽입 정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')
    
                

    