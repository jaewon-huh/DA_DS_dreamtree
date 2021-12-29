#예외 구분하기 
try :
    a = [273,103,52,57,100]
    number_input_a = int(input("정수입력>(0~4까지 입력해주세요) "))
    print("{}번째 요소 : {}".format(number_input_a,a[number_input_a]))
    예외.등장()
except ValueError as e: 
    print("값에 문제가 있습니다")
except IndexError as e: 
    print("0~4를 입력해주세요 .")
except Exception as e:  # !! 모든 예외의 부모격이므로 포함 
    print("알수없는 예외가 발생했습니다")
    print(type(e),e)