# 보초법 : 배열 끝에 검색하고자 하는 키 값을 추가 

from typing import Any, Sequence
import copy             # deepcopy 이용 

def seq_search(seq: Sequence, key: Any) -> int:
    
    a = copy.deepcopy(seq)      # seq 복사
    a.append(key)               
    
    i = 0

    while True:
        if a[i] == key:
            break
        i += 1
    return -1 if i == len(seq) else i   

    """ i 값이 len(seq) : 찾은값이 보초 (실패) -1 반환,  그렇지 않으면 i 반환 성공 """

if __name__ == '__main__':
    num = int(input('원소 수를 입력하세요.: '))  # num 값을 입력
    x = [None] * num                           # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))         # 원소 값 채워 넣기 

    ky = int(input('검색할 값을 입력하세요.: '))  # 검색할 키 ky를 입력받기

    idx = seq_search(x, ky)                     # ky와 같은 원소를 x에서 검색

    if idx == -1:
        print('검색값을 갖는 원소가 존재하지 않습니다.')
    else:
        print(f'검색값은 x[{idx}]에 있습니다.')