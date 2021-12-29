def test():             #함수선언
    print("a 지점 통과")
    yield 1 
    print("b 지점 통과")
    yield 2
    print("c 지점 통과")
output = test()         #함수 호출
print("d 지점 통과")
a = next(output)        #next 함수 호출
print(a)                #print(next) : 리턴값출력
# a지점 통과(next()로 실행 ) , 1 출력
print("E지점 통과")
b= next(output)
print(b)                #b지점 통과 + 리턴값 2 
print("f지점 통과")
print()
#반복문과 활용 
for i in test():
    pass
for i in test():        #i로 전달해준 값이 오게됨 
    print(i)



#split()
print("go_go_go ".split("_"))
#"문자열".join()
print(":".join(["1","2","3"]))  #그냥[1,2,3] → 에러 
numbers = [1,2,3,4,5,6]
print("::".join(map(str,numbers)))