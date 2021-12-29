#튜플 : 리스트와 비슷한 자료형 , 소괄호()로 선언 , 한번 선언한 값 수정 x 
a = (1,2,3,4,)
a[0]
print(a[0])
print()
# a[0] = 5 , 불가 
#괄호없는 튜플
c,d = 30, 40 
print(c,d)
#스왑
c,d = d,c 
print(c,d)

# 튜플- 함수의 리턴
def test() :
    return 10,20
a,b = test()
print(a)
print(b)
#튜플을 리턴 divmood() 몫과 나머지 구하는 함수 
(e,f) = 90,40
print()
print(divmod(e,f))
print(type(divmod(e,f)))
def test():
    return 10,20
g,h = test()
print(g,h)
print()
z = {
    (0,0) : 10  #튜플은 딕셔너리의 키로 사용가능 
}
print(z[(0,0)])
print(z[0,0])   #딕셔너리의 튜플 값 호출할때 괄호 생략해도 문제 x  