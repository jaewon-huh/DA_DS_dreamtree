# 고정 길이 큐 클래스 사용 

from enum import Enum 
from fixed_queue import FixedQueue

# 프로그램 
## 이전 hash , stack 프로그램에서 변수만 고치면됨 
  # 메뉴 선택 

Menu = Enum('Menu', ['인큐', '디큐', '피크', '검색', '덤프', '종료'])

def select_menu() -> Menu:
    """메뉴 선택"""
    s = [f'({m.value}){m.name}' for m in Menu]      #(1)푸시 (2) 팝 (3) 피크 ... 
    while True:
        print(*s, sep = '   ', end='')              
        n = int(input(': '))                        # 메뉴를 골라 1~ 6 
        if 1 <= n <= len(Menu):
            return Menu(n)

q = FixedQueue(64)          # capacity = 64인 큐 q

while True : 
    print(f'현재 데이터 개수 : {len(q)} / {q.capacity}')
    menu = select_menu()

    if menu == Menu.인큐:       # 인큐
        x = int(input('인큐할 데이터를 입력하세요 : '))
        try : 
            q.enque(x)
        except FixedQueue.Full : 
            print('큐가 가득 차 있어 enque 할 수 없습니다.')

    elif menu == Menu.디큐 :
        try : 
            x = q.deque()
            print(f'디큐한 데이터는 {x}입니다.')
        except FixedQueue.Empty :
            print('큐가 비어 있어 pop할 수 없습니다.')
    
    elif menu == Menu.피크 :
        try : 
            x = q.peek()
            print(f'피크한 데이터는 {x}입니다.') 
        except FixedQueue.Empty :
            print('큐가 비어있어 peek 할 수 없습니다.')

    elif menu == Menu.검색 : 
        x = int(input('검색할 값을 입력하세요. : '))
        if x in q : 
            print(f'{q.count(x)}개 포함되고, 맨 앞의 위치는 {q.find(x)}입니다.')       
        else : 
            print(f'검색값 {x}를 찾을수 없습니다.')
    
    elif menu == Menu.덤프 :
        q.dump()
    else :              #종료 
        break       

