# 세 정수를 입력받아 중앙값 구하기 

def med3(a,b,c):
    if a >= b:          # b  a 
        if b >= c :     # c  b  a 
            return b
        elif a <= c :   # b  a  c 
            return a 
        else :          # b  c  a 
            return c 
    elif a > c :        # elif -> a  b 
        return a        # a> c -> c  a b 
    elif b > c :        # a  < b , a <= c , b> c 
        return c        # a   c    b 
    else :              # a  < b , a <= c , b <= c  
        return b        # a   b    c 


a = int(input('정수 a 값 : '))
b = int(input('정수 b 값 : '))
c = int(input('정수 c 값 : '))

print(f'중앙값은 {med3(a,b,c)}입니다.')


def med3_2(a,b,c) :
    if (b >= a and c <= a) or (b <= a and c>= a) :
        return a 
    elif (a>b and c<b) or (a<b and c> b) :      #  b>=a 가 아니면 무조건 a>b라 불필요.
        return b
    return c 