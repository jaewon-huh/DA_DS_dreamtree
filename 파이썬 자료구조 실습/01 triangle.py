# 왼쪽 아래가 직각인 이등변 삼각형으로 * 출력 
# 이중루프 
from __future__ import print_function


n = int(input('짧은 변의 길이 입력 : '))

for i in range(n) :             # i = 0 1 2 3 4  n
    for j in range(i+1) :       # j = range(1) ,range(2) , range(3)...
        print('*', end='')
    print()

# 오른쪽 아래가 직각인 이등변 (공백이 필요함 ____*)
n = int(input('짧은 변의 길이 입력 : '))
for i in range(n) :              
    for _ in range(n-i-1) :     
        print(' ', end ='')     
    for _ in range(i+1):        
        print('*',end='')
    print()
# 모든 행에 있어 공백 + 별의 수(i+1) = n  