#else 조건문 : if 조건문이 거짓일때 실행 
number = input("정수 입력>")
number = int(number)
if number % 2 == 0 :
    print("짝수입니다.")
else :
    print("홀수입니다.")
#elif : 두개로만 구분 x
import datetime
now = datetime.datetime.now()
month = now.month
if 3 <= month <= 5 :
    print("봄입니다")
elif 6 <= month <= 8 :
    print("여름입니다")
elif 9 <= month <= 11 :
    print("가을입니다")
else :
    print("겨울입니다")
score = float(input(">학점을 입력하세요."))
if score == 4.5 :
    print("신")
elif 4.2 <= score:
    print("교수님의 사랑")
elif 3.5 <= score:
    print("현 체제의 수호자")
elif 2.8 <= score:
    print("일반인")
elif 2.3 <= score:
    print("소시민")
elif 1.75 <= score:
    print("오락왕")
elif 1.0 <= score:
    print("불가촉 천민")
elif 0.5 <= score:
    print("자벌레")
elif 0 < score:
    print("플랑크톤")
else :
    print("혁명가")    