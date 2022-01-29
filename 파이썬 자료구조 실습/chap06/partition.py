# 퀵정렬 알고리즘 : 분할 & 재귀

# 분할 알고리즘 

from typing import MutableSequence

def partition(a: MutableSequence) :
    n = len(a)
    pl = 0          # 왼쪽 포인터
    pr = n-1        # 오른쪽 포인터 
    x = a[n//2]     # 피벗 : 배열의 가운데 원소 

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

    print(f'피벗은 {x}입니다.')

    print('피벗 이하인 그룹입니다.')

    print(*a[0:pl])                      # a[0]  ~ a[pl -1]

    if pl > pr +1 :
        print('피벗과 일치하는 그룹입니다.')
        print(*a[pr+1 : pl])             #  a[pr+1]  ~ a[pl -1]
    
    
    print('피벗 이상인 그룹입니다.')
    print(*a[pr+1: n])             

if __name__ == '__main__':
    print('배열을 나눕니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num    # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))      # 원소 넣기 

    partition(x)         # 배열 x를 나누어서 출력
