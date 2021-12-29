#함수로 매개변수를 전달 
def call_10_times(func):
    for i in range(10):
        func(i) # 콜백함수 

def print_hello(number): 
    print("hello",number)
call_10_times(print_hello)
print()
#람다: 또 다른 함수 구문 작성 x , 람다로 함수를 쉽게 선언 
#lambda 매개변수 : 리턴값 
call_10_times(lambda number : print( "ㅎㅇ",number))
#filter()
a = list(range(100))
# print(filter(짝수만,a)) 
# →filter object~ 제네레이터 , list()함수 적용해야 출력
b = filter(lambda number: number % 2 ==0, a)
# a 리스트에서 짝수만 
print(list(b))
#map
print(list(map(lambda number:number *number,a)))
# 리스트 내포와 기능 똑같다 
#print([i*i for i in a #if i%2 == 0 (filter의 경우 )])