# 배열의 원소의 최대값을 구해서 출력 (원소값 난수 생성)
import random

from scipy import rand
from max import max_of

num = int(input('난수의 개수를 입력하세요. : '))
lo = int(input('난수의 최소값을 입력하세요. : '))
hi = int(input('난수의 최대값를 입력하세요. : '))

x = [None] * num

for i in range(num) : 
    x[i] = random.randint(lo, hi)

print(f'{(x)}') # 리스트를 출력 
print(f'이 가운데 최대값은 {max_of(x)}입니다. ')