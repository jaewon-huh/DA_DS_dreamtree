#기본적인 함수의 활용
#범위 내부의 정수를 모두 더하는 함수 
def sum_all(start,end):
    output = 0  # 변수 선언  초기값을 설정할때 연산해도 값에 아무런 변화를 주지 않는 것
    for i in range(start,end+1): #범위 내부 반복문 돌리기 
        output += i 
    return output #리턴
print("0to 100 : " ,sum_all(0,100))


def sum_all2(start=0,end=100, step =1):
    output = 0  # 변수 선언  초기값을 설정할때 연산해도 값에 아무런 변화를 주지 않는 것
    for i in range(start,end+1,step): #범위 내부 반복문 돌리기 
        output += i 
    return output #리턴
print("a.", sum_all2())
print("b.", sum_all2(0,100,10))

# x^2 + 1
def f(x) :
    return (x*x) + 1
print(f(5))

# print(mul(5,6,7,8)) 매개변수로 전달된 값들을 모두 곱해서 리턴하는 가변 매개변수 함수
def mul(*values) :
    output = 1
    for i in values :  # output = 1 , i = 5 -> output =5 , output = 5 , i = 6 -> output = 30 
        output *= i
    return output
print(mul(5,6,7,8))    