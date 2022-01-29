# 양의 정수 n의 팩토리얼 구하는 함수 
# or math 모듈 factorial() 

def factorial(n) :
    if n > 0 :
        return n * factorial(n-1)
    else :
        return 1 
    
if __name__ == '__main__' :
    n = int(input('출력할 팩토리얼값을 입력 : '))
    print(f'{n}! 은 {factorial(n)}입니다. ')