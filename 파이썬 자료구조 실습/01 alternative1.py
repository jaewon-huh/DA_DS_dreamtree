# 반복과정에서 조건 판단하기 2
# '줄바꿈 없이' +와 -를 '번갈아' 출력
print('+와 - 를 번갈아 출력합니다.')
n = int(input('몇개를 출력할까요? : '))

for i in range(n) :         # 0 ~ n-1 , 
    if i %2 == 0 :
        print('+', end= '') # 짝수면 +
    else :
        print('-', end = '')

print() # 1~ n까지 1씩 증가 : range(1,n+1) , 홀수일때 + 

#problem for n번 if문도 n번(판단 n번) 

# 수정 
print('+와 - 를 번갈아 출력합니다2.')
n2 = int(input('몇개를 출력할까요?2 : '))

for _ in range(n2 // 2):  # 언더바 _ 사용 : 무시하고 싶은 값 
    print('+-', end ='')  # +-를 n//2 개 출력 (몫)
if n2 %2 :
    print('+', end= '')   # 나머지가 있으면 (홀수) : +를 출력 

print()
# 짝수라면 for 문 단계에서 종료 / 홀수라면 if문 추가 
