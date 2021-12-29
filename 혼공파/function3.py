# n! = 1 * 2 * 3 * ...* (n-1) * n  
def factorial_1(n):
    output = 1
    for i in range(1, n+1) :
        output *= i
    return output
print(factorial_1(5))
# n! = n *(n-1)!
# 0! = 1
# 재귀함수 함수 내부에서 함수를 호출
# f(n) = n * f(n-1) (n>=1)
# f(0) = 1
def factorial_2(n):
    if n == 0 :
        return 1
    else:
        return n * factorial_2(n-1)
print(factorial_2(6))  

#피보나치 수열 
#f(1) = 1
#f(2) = 1
#f(n) = f(n-1) + f(n-2)

# 변수를 선언
counter = 0
# 함수 선언 
def factorial_3(n):
    global counter
    counter += 1
    if n ==1 or n==2 :
        return 1
    else :
        return factorial_3(n-1) + factorial_3(n-2)
print(factorial_3(10))
print(counter)
# 메모화  
# 메모장 딕셔너리 
dictionary = {
    1 : 1,
    2 : 1
}
def fibonacci(n) :
    if n in dictionary: # 메모장에 n(key)이 있으면 
        return dictionary[n]
    else:
        output= fibonacci(n-1) + fibonacci(n-2)
        dictionary[n] = output
        return output
print(fibonacci(5))

#조기리턴 (중간에 리턴사용해서 들여쓰기 없애기, else 없애고 한문장으로 )
def fibonacci2(n) :
    if n in dictionary:
        return dictionary[n] # if t면 끝. 아니면 else 없어도 밑으로 
    output= fibonacci(n-1) + fibonacci(n-2)
    dictionary[n] = output
    return output
print(fibonacci2(5))