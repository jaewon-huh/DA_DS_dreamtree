# 시퀀스원소의 최대값을 구하는 함수 구현 

from traceback import print_tb
from typing import Any, Sequence        #any 임의의 자료형 ,sequence 시퀀스형 
# 함수
def max_of(a :Sequence) -> Any :           
    """ 시퀀스형 a원소의 최대값 반환 
        입력 : 시퀀스형 -> 반환 : any """
    maximum = a[0]
    for i in range(1,len(a)) :
        if a[i] > maximum : 
            maximum = a[i]
    return maximum

# 프로그램 (모듈)
    """직접 실행될때 __namㄴe__ == __main
    프로그램이 임포트 될때 , __name__  == 원래의 모듈이름(파일이름)  """

if __name__ == '__main__' : # 엔트리 포인트? 
    print('배열의 최대값을 구한다.')
    num = int(input('원소 수를 입력하세요. :'))
    x = [None] * num        # 원소 수가 num인 원소값 정하지 않은 리스트 생성

    # 리스트 원소 값 iterable 입력 :  for i in range(n) : x[i] = 값  0 1 2 3 4 ... 
    for i in range(num):
        x[i] = int(input(f'x[{i}]값을 입력하세요. : '))  # 사용자에게 인덱스 값을 입력받음 

    print(f'최대값은 {max_of(x)}입니다.')