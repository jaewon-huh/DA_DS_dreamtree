# 순수한 재귀함수 (재귀호출을 여러번 ) 

import re


def recur(n: int) :
    if n >0 :
        recur(n-1)
        print(n)
        recur(n-2)

x = int(input('정수값을 입력하시오. : '))

recur(x)