# 비 재귀적으로 퀵 정렬 구현 
# 스택으로 재귀 작업을 대신함 

from stack import Stack  # stack 파일 임포트 
from typing import MutableSequence

def qsort(a, left, right) :
    """ a[left] ~ a[right]를 비 재귀적 퀵정렬 """
    range = Stack(right - left + 1)     # 스택 생성 (크기 : 배열의 원소 수)

    range.push((left, right))           # 튜플 (left, right)를 스택에 push

    while not range.is_empty() :    
        # 초기 설정 
        pl, pr = left, right    =  range.pop()          # 왼쪽, 오른쪽 포인터를 pop
        x = a[(left+ right) // 2]                       # 피벗 

        while pl <= pr :    # 교차 전 
            while a[pl] < x :     # 스캔해 
                pl += 1
            while a[pr] > x :
                pr -= 1
            if pl <= pr  :        # pl하고 pr이 스톱함 . 교차하지 않음 
                a[pl] , a[pr] = a[pr], a[pl]    
                pl += 1 
                pr -= 1
        # 교차함 .  pl > pr

        if left < pr : range.push((left, pr))
        if pl < right: range.push((pl, right))      

def quick_sort(a: MutableSequence) :
    " 퀵 정렬 "
    qsort(a, 0, len(a)- 1)          

if __name__ == '__main__': 
    print('퀵 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num   # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    print()            
    quick_sort(x)      # 배열 x를 퀵 정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')