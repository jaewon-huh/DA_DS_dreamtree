# 링 버퍼의 활용 (오래된 데이터를 버리기 (최근 데이터만 저장))

# 원하는 개수(n) 만큼 값을 입력받아 마지막 n개를 저장

n = int(input('정수를 몇 개 저장할까요? :'))
a = [None] * n      # 배열 

cnt = 0             # 정수를 입력받은 개수 

while True: 
    a[cnt % n] = int(input((f'{cnt + 1}번째 정수를 입력하세요. :')))
    cnt += 1 

    retry = input(f'계속 할까요 ? (Y - Yes / N - No):')
    if retry in {'N', 'n'}  :       # 사용자가 N을 입력했다면
        break

i = cnt - n 
if i < 0 : i = 0        # 초기 cnt = 0 , n > 0 음수 -> i = 0으로 초기값

while i < cnt :         
    print(f'{i+1}번째 = {a[i%n]}')
    i+=1

    """ 정수 10개 입력해 첫번째 값 cnt = 0 , a[cnt % n] = a[0]
        2번째 값 입력 cnt 1 a[1] 
        10번째 값 입력 cnt 9 a[9] 
        11번째 값 입력 cnt 10 a[0] 덮어쓰기 (기존 첫번째 값이 업데이트됨)"""