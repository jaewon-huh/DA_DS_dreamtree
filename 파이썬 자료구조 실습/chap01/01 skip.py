# 반복문 건너뛰기와 여러범위 스캔 
# 1~ 20 까지 8은 빼고 출력

for i in range(1,21):
    if i == 8 :
        continue
    print(i , end =' ')

print("\n")  # 끝가지 모두 if문을 판단해서 비효율 

for i in list(range(1,8)) + list(range(9, 21)) :
    print(i, end= ' ')
# 리스트를 사용해 8 생략 
