# 단순 선택 정렬 

from typing import MutableSequence

def selection_sort(a : MutableSequence) :

    n = len(a)
    for i in range(n-1) :       # i : 0 ~ len(a) -1  
        for j in range(i+1, n) :
            if a[i] > a[j] :
                a[i], a[j] = a[j] , a[i]
                
if __name__ == '__main__':
    print('단순 선택 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num  # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}] : '))

    selection_sort(x)  # 배열 x를 단순 선택 정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')                