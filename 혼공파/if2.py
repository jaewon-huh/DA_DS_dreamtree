#계절구분하기 
import datetime
now =datetime.datetime.now()
if 3 <= now.month <=5 :
    print("{}월로 봄이네요".format(now.month))
if 6 <= now.month <=8 :
    print("{}월로 여름이네요".format(now.month))
if 9 <= now.month <=11 :
    print("{}월로 가을이네요".format(now.month))
if now.month == 12 or 1<= now.month <=2 :
    print("{}월로 봄이네요".format(now.month))

number = input("정수 입력>")
last_character= number[-1]
#in 활용해 홀짝구하기 
if last_character in "02486" :
    print("짝수")
if last_character in "13579" :
    print("홀수")
#더 빠른 방법 컴퓨터적
number1 = input("정수 입력2>")
number1 = int(number1)
if number1 % 2 ==1 :
    print("홀수입니다")
if number1 % 2 == 0 :
    print("짝수입니다.")
#ex)04 
a = float(input(">1번째 숫자 : "))
b = float(input(">2번째 숫자 : "))
print()
if a > b :
    print("첫째로 입력한 {}가 {}보다 큽니다.".format(a,b))
if a < b :
    print("둘째로 입력한 {}가 {}보다 큽니다.".format(b,a))
