# 힙 정렬 알고리즘 구현 
# heap_sort 안의 down_heap 

from calendar import c
from typing import MutableSequence 

def heap_sort(a:MutableSequence) :
    
    def down_heap(a, left,right) :   
        """ a[left] ~a[right]를 힙으로 만들기  """
        temp = a[left]      # 루트

        parent = left 
        while parent < (right+1) // 2 :             #힙 삭제 & 트리클링 : 힙 재구성 
            cl = parent *2 + 1                      #왼쪽 자식
            cr = parent *2 + 2                      #오른쪽 자식 
            child = cr if cr <= right and a[cr] > a[cl] else cl             # 자식 둘 비교해서 더 큰 값 
            if temp >= a[child]:                    # 트리클 노드가 더큼 (적절한 자리) 
                break
            a[parent] = a[child]                    # 트리클링 (스왑)
            parent = child                          # 다음 단계 
        a[parent] = temp

    n = len(a)                                  # 배열 원소수 

    for i in range((n-1) //2 , -1 , -1) :       # a[i] ~ a[n-1] 를 힙으로 만들기 : 배열 a를 힙
        down_heap(a,i,n-1)

    for i in range(n-1, 0, -1) :                # 힙정렬 알고리즘 i = n-1 초기화
        a[0], a[i] = a[i], a[0]                 # 루트와 마지막원소 스왑 
        down_heap(a,0, i-1)                     # a[0] ~ a[i-1]을 힙으로 

if __name__ == '__main__':
    print('힙 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요. : '))
    x = [None] * num    # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}] : '))

    heap_sort(x)        # 배열 x를 힙 정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')    

