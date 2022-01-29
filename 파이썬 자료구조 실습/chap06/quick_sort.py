# 퀵 정렬 알고리즘 구현 

from typing import MutableSequence

def qsort(a: MutableSequence, left : int, right : int) :
    """ a[left] ~ a[right]를 퀵 정렬 """

    pl = left                       # 왼쪽 포인터 
    pr = right                      # 오른쪽 포인터
    x = a[(left +right) // 2 ]      # 피벗

    print(f'a[{left}] ~ a[{right} ] :', *a[left : right +1])       # 나누는 과정을 추가함.

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

    if left < pr : qsort(a , left , pr)     # 왼쪽 그룹 재귀
    if pl < right: qsort(a, pl, right)      # 오른쪽 그룹 재귀 

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