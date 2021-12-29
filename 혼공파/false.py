#False로 변환되는값
#bool() - None, 0 , 빈컨테이너("",{},(),[]) : False로 변환 
number = input("정수를 입력하세요 >")
number = int(number)
if number :             #if 매개변수에 불이아닌 다른값 올때 자동으로 불로 변환 
    print("음수 혹은 양수입니다.")
else :
    print("o입니다.")
number2 = input("정수를 입력하세요 >")
number2= int(number2)
if number2 >0 :
     #양수일때 미구현 상태입니다.
     pass
else:
    #음수일때도 미구현입니다.
     pass