#if 조건문!
number = input("정수입력>")
number = int(number)
if number > 0 :
    print("양수")
if number < 0 :
    print("음수")
if number == 0 :
    print("제로")
import datetime
#날짜구하기 
now = datetime.datetime.now()
if now.hour < 12 :
    print("현재시각은{}시로 오전입니다.".format(now.hour))
if now.hour >= 12 :
    print("현재시각은{}시로 오후입니다.".format(now.hour))
#print(now.year)
#print(now.month)
#print(now.day)
#print(now.hour)
#print(now.minute)
#print(now.second)
 
