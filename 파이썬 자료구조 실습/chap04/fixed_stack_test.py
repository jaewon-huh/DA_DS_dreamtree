# 고정 길이 스택 클래스 사용하기 

from ast import While
from enum import Enum 
from fixed_stack import FixedStack

# 프로그램 

  # 메뉴 선택 

Menu = Enum('Menu', ['푸시', '팝', '피크', '검색', '덤프', '종료'])

def select_menu() -> Menu:
    """메뉴 선택"""
    s = [f'({m.value}){m.name}' for m in Menu]      #(1)푸시 (2) 팝 (3) 피크 ... 
    while True:
        print(*s, sep = '   ', end='')              
        n = int(input(': '))                        # 메뉴를 골라 1~ 6 
        if 1 <= n <= len(Menu):                     # *s : unpacking 기능 
            return Menu(n)

s = FixedStack(64)      # s = capacity = 64의 스택 
                        # 클래스형 인스턴스 ! 
while True : 
    print(f'현재 데이터 개수 : {len(s)} / {s.capacity}')
    menu = select_menu()

    if menu == Menu.푸시 :       # 푸시 
        x = int(input('데이터를 입력하세요 : '))
        try : 
            s.push(x)
        except FixedStack.Full : 
            print('스택이 가득 차 있어 push 할 수 없습니다.')

    elif menu == Menu.팝 :
        try : 
            x = s.pop()
            print(f'팝한 데이터는 {x}입니다.')
        except FixedStack.Empty :
            print('스택이 비어 있어 pop할 수 없습니다.')
    
    elif menu == Menu.피크 :
        try : 
            x = s.peek()
            print(f'피크한 데이터는 {x}입니다.') 
        except FixedStack.Empty :
            print('스택이 비어있어 peek 할 수 없습니다.')

    elif menu == Menu.검색 : 
        x = int(input('검색할 값을 입력하세요. : '))
        if x in s : 
            print(f'{s.count(x)}개 포함되고, 맨 앞의 위치는 {s.find(x)}입니다.')        # 맨 위 위치 top
        else : 
            print(f'검색값 {x}를 찾을수 없습니다.')
    
    elif menu == Menu.덤프 :
        s.dump()
    else :              #종료 
        break       
