# 변수는 그저 이름에 불과

n = 1      # 전역 변수 global (함수 내부·외부에서 사용)
def put_id():
    x = 1  # 지역 변수(함수 내부에서만 사용)
    print(f'id(x) = {id(x)}')
    
print(f'id(1) = {id(1)}')
print(f'id(n) = {id(n)}')
put_id()