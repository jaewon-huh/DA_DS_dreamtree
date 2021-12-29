#p105 ex)3
a =input(">1번째숫자: ")
b =input(">2번째숫자: ")
print()
print("{}+{}={}".format(a,b,int(a)+int(b)))
#ex)4
string = "hello"
string.upper()
print("A지점:", string) #비파괴적 함수로 string 영향 x
print("A지점:", string.upper())
format_a =" 파이썬"