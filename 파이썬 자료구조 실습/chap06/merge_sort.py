from math import ceil
from re import S
from tkinter import N
from typing import MutableSequence

def merge_sort(a: MutableSequence) :
    """ 병합정렬"""

    def _merge_sort(a :MutableSequence, left, right) :
        """ a[left] ~ a[right]를 '재귀적'으로 병합 정렬"""
        if left < right : 
            center = (left + right // 2)        # 가운데 부분 

        _merge_sort(a, left, center)            # 앞부분 병합정렬
        _merge_sort(a, center+1, right)         # 뒷부분 병합정렬

        # 병합 마친 앞부분과 뒷부분을 병합

        p = j = 0
        i = k = left

        while i <= center :                     # 배열의 앞부분
            buff[p] = a[i]                      # 앞부분을 buff로 복사함 
            p +=1
            i +=1

        while i <= right and j < p :            # 뒷부분 
            if buff[j] <= a[i]:                 # 배열 뒷부분과 buff로 복사한 앞부분 p개를  '병합해' 배열 a에 저장함.
                a[k] = buff[j]
                j +=1
            else : 
                a[k] = a[i]
                i += 1
            k+=1 

        while j < p :                           # 배열 buff에 남아 있는 원소를 배열 a에 복사
            a[k] = buff[j]
            k +=1 
            j +=1


    n = len(a)
    buff =[None] * N                            # 작업용 배열 생성
    _merge_sort(a,0,n-1)                        # 배열 전체를 병합정렬 
    del buff                                    # 작업용 배열 삭제 

if __name__ == '__main__':
    print('병합 정렬을 수행합니다')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num    # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    merge_sort(x)       # 배열 x를 병합 정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')