 #예외 객체 : except 예외의 종류 as 예외객체를 활용할 변수 이름 
list_number = [52,23,231,3,100]
# try except as 
try : 
    # 숫자를 입력해 
    number_input = int(input("정수입력 > "))
    # 리스트의 요소 출력
    print("{}번째 요소는 {}".format(number_input, list_number[number_input]))
except Exception as e :
    # 예외 객체를 출력
    print("type(exception):", type(e))
    print("exception : ",e )   

try :
    a = [273,103,52,57,100]
    number_input_a = int(input("정수입력>(0~4까지 입력해주세요) "))
    print(a[number_input_a])
except Exception as e: 
    if type(e) == ValueError :
        print("값에 문제가 있습니다")
    elif type(e) == IndexError :
        print("0~4를 입력해주세요 .")

#예외 구분하기 
try :
    a = [273,103,52,57,100]
    number_input_a = int(input("정수입력>(0~4까지 입력해주세요) "))    #1
    print("{}번째 요소 : {}".format(number_input_a,a[number_input_a])) #2 확인 if 0~4 -> 2번째 요소는 52 & 3-1  else -> except
    예외.등장()                                                        #3-1 알수없는 예외가 발생 NameError
except ValueError as e: 
    print("값에 문제가 있습니다")
except IndexError as e: 
    print("0~4를 입력해주세요 .")
except Exception as e:  # !! 모든 예외의 부모격이므로 포함 
    print("알수없는 예외가 발생했습니다")
    print(type(e),e)

