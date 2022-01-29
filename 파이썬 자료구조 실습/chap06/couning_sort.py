# 도수 정렬 알고리즘 구현 

from typing import MutableSequence 

def fsort(a: MutableSequence, max : int) :
    """도수 정렬 (배열의 원소값은 0 ~ max )"""
    n= len(a)                                  # 정렬할 배열 a
    f = [0] * (max+1)                          # 누적 도수 분포표 배열 f 
    b = [0] * n                                # 작업용 배열 b

    for i in range(n) :
        f[a[i]] += 1                            # 도수 분포표
    for i in range(1, max+1) :
        f[i] += f[i-1]                          # 누적 도수 분포표
    for i in range(n-1, -1 , -1) : 
        f[a[i]] -= 1
        b[f[a[i]]] = a[i]                       # 작업용 배열 (정렬된거 ㅅ)
    for i in range(n):
        a[i] = b[i]                        # 배열 복사 (작업용 배열 -> 원래 배열)

def counting_sort(a: MutableSequence) :
    fsort(a,max(a))
    

if __name__ == '__main__':
    print('도수 정렬을 합니다.')
    num = int(input('원소 수를 입력하세요. : '))
    x = [None] * num  # 원소 수가 num인 배열을 생성

    for i in range(num):  # 양수만 입력받음
        while True:
            x[i] = int(input(f'x[{i}] : '))
            if x[i] >= 0: break             # 양수 입력 x -> 다시 input해야함  

    counting_sort(x)  # 배열 x를 도수 정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')