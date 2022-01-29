# 단순 삽입 정렬 
# 인덱스 1부터 시작 : 공백으로 채우고 그 값을 임시변수에 저장 
# 공백 왼쪽값과 임시변수의 값을 비교해서 왼 > 오 -> 시프트 
# 마지막 인덱스에서 패스 스루 실행시까지 . 

from typing import MutableSequence

def insertion_sort(a :MutableSequence) :
    for i in range(1,len(a)) :
        tmp = a[i]          # 제거값 
        position = i -1     # 왼쪽 인덱스 
        while position >= 0 and a[position] > tmp :         # 왼쪽값 인덱스가 0보다 큼 (최대 맨앞) / 그리고 왼쪽값이 제거값보다 크면  
            a[position +1] = a[position]        # 스왑 
            position -= 1                       # 왼쪽인덱스를 다음 왼쪽으로 
        a[position+1] = tmp


if __name__ == '__main__':
    print('단순 삽입 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num  # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    insertion_sort(x)  # 배열 x를 단순 삽입 정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')
