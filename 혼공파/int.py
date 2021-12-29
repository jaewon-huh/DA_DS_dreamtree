string_a = input("입력A>")
int_a = int(string_a)
# 밑과 같습니다 
# string_a =input("입력A>")
# string_a = float(string_a) 
string_b = input("입력b>")
int_b = int(string_b)
#float(): 부동소수점
print("문자열 자료:" , string_a + string_b)
print("숫자자료:", int_a + int_b)

a=input("문자열입력> ")
b=input("문자열입력> ")
c=b #두개 상태에서는 서로를 바꿀수 없으니 별도의 변수 c 선언 b가 비었음
b=a #이제 b에 a를
a=c #다시 a에 c를 넣으면 a →b , b→a 로 !
print(a,b)