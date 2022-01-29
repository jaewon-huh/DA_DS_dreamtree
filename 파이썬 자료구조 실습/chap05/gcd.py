# 유클리드 호제법 : 두 정수의 최대 공약수 구하기 


def gcd(x: int,y :int ) :
    if y == 0 :
        return x 
    else :
        return gcd(y, x% y)
# gcd(12,6) -> gcd(6,0) -> y = 0 , 6이 최대 공약수 

if __name__ == '__main__' :
    print('두 정수의 최대 공약수를 구합니다.')
    x = int(input('첫 번째 정수값을 입력하시오.  : '))
    y = int(input('두 번째 정수값을 입력하시오.  : '))

    print(f'두 정수값의 최대공약수는 {gcd(x,y)}')

# math.gcd() 사용 
