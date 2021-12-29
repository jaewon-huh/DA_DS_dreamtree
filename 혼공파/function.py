#def 함수이름(매개변수, 매개변수 , ...) : 
#    문장
def print_n_times(value,n) :
    for i in range(n):
        print(value)
print_n_times("안녕하세요",5)
# print_n_times("ㅎㅇ") TypeError : 매개변수 n이 없음
# print_n_times("ㅎㅇ",10,20) TypeError : 매개변수 2개인데 3개 입력 
#가변 매개변수 
#def 함수이름 (매개변수,매개변수,*가변매개변수):
def print_n_times2(n,*values) :
    for i in range(n):
        for value in values:
            print(value)
print_n_times2(3,"ㅎㅇ","즐거운","파이썬")
print()
# 기본 매개변수 
def print_n_times3(value,n=2) :
    for i in range(n):
        print(value)
print_n_times3("ㅎㅇ")
print()
#가변매개변수가 기본매개변수보다 앞에 올때 실행법.
#키워드 매개변수 
def print_n_times4(*values,n=2) :
    for i in range(n):
        for value in values :
            print(value)
print_n_times4("ㅎ","ㅈ","ㅇ",n=3)  #ㅎ ㅈ ㅇ 세번 실행  
#print_n_times4("ㅎ","ㅈ","ㅇ",3) 이렇게 하면  ㅎ ㅈ ㅇ 3 두번 실행
#print_n_times4("ㅎ","ㅈ","ㅇ") 이렇게 하면 ㅎ ㅈ ㅇ 두번 실행  

#리턴
def function():
    print("A")
    print("B")
    return 
    print("C")
    print("D")
print(function())