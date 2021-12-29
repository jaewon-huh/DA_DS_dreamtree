#구문오류(Syntax error) :코드에 문제가 있어서 실행 x 
#ex) print("ㅇㅅㅇ ) 따옴표 x
#예외(런타임 오류 ) : 실행과 관련된 문제, '실행은 되지만' 죽음
#1ist_a = [1,2,3] , print(list_a[5])

#조건문으로 예외 처리 
print("밑은 조건문 예외처리입니다.")
while True :
    user_input_a = input("정수입력> ")
    if user_input_a.isdigit() :
        number_input_a = int(user_input_a)
        print("원의 반지름:", number_input_a)
        print("원의 둘레 : ", 2*3.14*number_input_a)
        print("원의 넓이 : ", 3.14 * number_input_a **2)
        break
    else:
        print("정수를 입력 해 주세요 ")
print("밑은 try 구문입니다")
#try except 구문 : 예외를 처리 할 수 있는 구문 
while True : 
    try :     #예외가 발생할 가능성이 있는 코드 
        number_input_a = int(input("정수입력> "))
        print("원의 반지름:", number_input_a)
        print("원의 둘레 : ", 2*3.14*number_input_a)
        print("원의 넓이 : ", 3.14 * number_input_a **2)
        break
    except:   #예외가 발생했을때 실행할 코드 
        print("정수를 입력 해 주세요 ")
print("밑은 try else 구문입니다")
# try except + else 구문 : else 부분에 예외가 발생하지 않았을때 실행한 코드 
try : 
    number_input_a = int(input("정수입력> "))
except:  
    print("정수를 입력 해 주세요 ")
else : #try 구문에서 예외가 발생 안했을때 실행 (그냥 다 try에 넣어도 됨)
    print("원의 반지름:", number_input_a)
    print("원의 둘레 : ", 2*3.14*number_input_a)
    print("원의 넓이 : ", 3.14 * number_input_a **2)
print("밑은 finally 구문입니다")
try :
    number_input_a = int(input("정수입력> "))
    print("원의 반지름:", number_input_a)
    print("원의 둘레 : ", 2*3.14*number_input_a)
    print("원의 넓이 : ", 3.14 * number_input_a **2)
except:  
    print("정수를 입력 해 주세요 ")
else:
    print("예외가 발생하지 않았습니다.")
finally:
    print("어찌됬건 프로그램이 끝났습니다.")