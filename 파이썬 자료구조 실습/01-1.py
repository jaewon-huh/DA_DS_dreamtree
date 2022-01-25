# 세 정수를 입력받아 최대값  

print('세 정수의 최대값을 구한다')
a = int(input('정수 a : '))
b = int(input('정수 b : '))
c = int(input('정수 c : '))


maximum = a 
if b > maximum : maximum = b
if c > maximum : maximum = c 

print(f'최대값은 {maximum}이다.')

def max3(a,b,c) :
    maximum = a
    if b > maximum : maximum = b
    if c > maximum : maximum = c
    return maximum

print(max3(3,5,2))   