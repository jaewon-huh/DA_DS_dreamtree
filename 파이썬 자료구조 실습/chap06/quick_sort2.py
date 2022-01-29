# 퀵 정렬 알고리즘 구현 (원소 수가 9 미만이면 단순 삽입정렬)
from typing import MutableSequence


def sort3(a : MutableSequence , idx1 , idx2 ,idx3) :
    """ 최적의 피벗 선택 알고리즘. 인덱스 3개 선택 , 정렬 -> 중앙값의 인덱스 반환"""
    if a[idx2] < a[idx1]: a[idx2], a[idx1] = a[idx1], a[idx2]
    if a[idx3] < a[idx2]: a[idx3], a[idx2] = a[idx2], a[idx3]
    if a[idx2] < a[idx1]: a[idx2], a[idx1] = a[idx1], a[idx2]
    return idx2


def insertion_sort(a: MutableSequence , left, right) :
    for i in range(left +1 , right +1) :
        j = i 
        tmp = a[i]          # 꺼낼값 
        while j > 0 and a[j-1] > tmp :      # 맨끝에 오지 않음 ,꺼낸 값보다 왼쪽에 있는 값이 더큼
            a[j] = a[j-1]                   # 스왑
            j -=1                           # 다음 왼쪽 
        # j = 0 or a[j-1] <= tmp    
        a[j] = tmp                          # 꺼낸값 다시 넣음 

def qsort(a , left, right) :
    if right - left < 9  :                  # 원소수가 9 미만 
        insertion_sort(a, left, right)
    else : 
        pl = left                           # 왼쪽 포인터 
        pr = right                          # 오른쪽 포인터
        m = sort3(a, pl, (pl+pr) //2, pr )  # 배열의 중앙값
        x = a[m]                            # 피벗
        
        a[m], a[pr-1]  = a[pr-1] , a[m]     # 피벗과 right -1 원소 교환 (피벗 이하 , 피벗 이상) 
        # a[left +1] ~ a[right -2] 만 분할하면 됨. 
        pl += 1 
        pr -= 2                              


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
    print('퀵 정렬을 수행합니다(원소가 9미만이면 단순 삽입정렬)')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num   # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    print()            
    quick_sort(x)      # 배열 x를 퀵 정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')