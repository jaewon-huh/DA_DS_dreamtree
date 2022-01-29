# 뮤터블 시퀀스 원소를 역순으로 정렬

# 인덱스 차원에서 i(왼) + n-i-1(오)  = n-1 (총 인덱스 수) /     0 ~ n-1
# 원소 6개 0 - 5 / 1 - 4  / 2 - 3 대응 시켜 교환  (교환횟수 n //2 , 나머지는 교환 x)

from typing import Any, MutableSequence

def reverse_array(a: MutableSequence) -> None:
    """뮤터블 시퀀스형 a의 원소를 역순으로 정렬"""
    n = len(a)
    for i in range(n // 2):
         a[i], a[n - i - 1] = a[n - i - 1], a[i]

if __name__ == '__main__':
    print('배열 원소를 역순으로 정렬합니다.')
    nx = int(input('원소 수를 입력하세요.: '))
    x = [None] * nx   # 원소 수가 nx인 리스트를 생성

    for i in range(nx):
        x[i] = int(input(f'x[{i}] : '))

    reverse_array(x)  # x를 역순으로 정렬

    print('배열 원소를 역순으로 정렬했습니다.')
    for i in range(nx):
        print(f'x[{i}] = {x[i]}')


# 함수 이용 x, x.reverse() , x / y = list(reversed(x))

