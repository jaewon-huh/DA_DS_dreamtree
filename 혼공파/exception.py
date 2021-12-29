# try except 구문
try :
    number_input_a = int(input("정수입력> "))
    #출력합니다.
    print("반지름", number_input_a)
    print("원 둘레 ", 2 * 3.14 * number_input_a)
except:
    print("무언가 잘못되었습니다.")

# 숫자로 변환되는 것들만 리스트에 넣기 
list_input_a = ["53", "273", "32","spy", "103"]
# 반복 적용 
list_number = []
for item in list_input_a :
    # 숫자로 변환해서 리스트에 추가 
    try : 
        float(item) # 예외가 발생하면 진행 x  다음 
        list_number.append(item)
    except : 
        pass    
print("{}내부에 있는 숫자는". format(list_input_a))
print("{}".format(list_number))

# try_except_else rnans
try : 
    # 숫자로 변환 
    number_input_a = int(input("정수 > "))
except :
    print("정수를 입력하세요.")
else : 
    print("반지름", number_input_a)
    print("원 둘레 ", 2 * 3.14 * number_input_a)