# 정렬을 마친 두 배열을 병합
from typing import Sequence, MutableSequence
# a + b -> c 
def merge_sorted_list(a : Sequence , b: Sequence , c :MutableSequence ) :
    """ 정렬을 마친 배열 a와 b를 병합해 c에 저장 """
    pa, pb, pc = 0, 0, 0                    # 각 배열의 포인터 
    na, nb, nc = len(a), len(b), len(c)     # 각 배열의 원소 수 

    while pa < na and pb < nb :             # 배열 a,b를 탐색할 것임
        if a[pa] <= b[pb] :
            c[pc] = a[pa]                  
            pa += 1
        else:
            c[pc] = b[pb]
            pb += 1
        pc += 1
                # a,b의 인덱스 값을 비교해 더 작은 값을 c에 인덱스에 저장 
                # 그리고 더 작은 배열의 포인터만 이동 
                
    # 포인터가 배열 맨 끝에 도착함 ! a, b 하나  
    while pa < na :                 
        c[pc] = a[pa]
        pa += 1
        pc += 1             # a 배열은 안 끝남.  a의 남은 원소 -> c로
    while pb < nb :                 
        c[pc] = b[pb]
        pb += 1
        pc += 1             # b 배열은 안 끝남.  b의 남은 원소 -> c로
    

if __name__ == '__main__' :
    a = [2, 4, 6, 8, 11, 13]
    b = [1, 2, 3, 4, 9, 16, 21]
    c = [None] * (len(a) + len(b))
    print('정렬을 마친 두 배열의 병합을 수행합니다.')

    merge_sorted_list(a, b, c)  # 배열 a와 b를 병합하여 c에 저장

    print('배열 a와 b를 병합하여 배열 c에 저장하였습니다.')
    print(f'배열 a: {a}')
    print(f'배열 b: {b}')
    print(f'배열 c: {c}')


print()
print('sorted() 함수와 ,heqpq 모듈의 merge 사용한 병합')

import heapq
a = [2, 4, 6, 8, 11, 13]
b = [1, 2, 3, 4, 9, 16, 21]

c = list(sorted(a+b))       # a와b 를 연결하여 오름차순으로 정렬한 것을 list로 변환해 c에 저장 
print(c)

d = list(heapq.merge(a,b))
print(d)