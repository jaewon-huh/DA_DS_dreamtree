# 고정 길이 스택 클래스 Fixedestack 구현

from typing import Any

class FixedStack :

    class Empty(Exception):
        ''' 비어 있는 stack에 pop or peek 할때 raise'''
        pass                
    class Full(Exception): 
        ''' 가득찬 stack에 push 하려 할때 raise '''
        pass 

    def __init__(self, capacity :int = 256) -> None : 
        ''' 스택을 초기화 ''' 
        self.stk = [None] * capacity    # 스택 배열 
        self.capacity = capacity        # 크기만 정해놓고
        self.ptr = 0                    # 채우진 않았습니다. (포인터 = 0 )

    def __len__(self) :
        return self.ptr                 # 쌓여있는 데이터 개수 확인

    def is_empty(self) : 
        return self.ptr == 0            # bool 자료형 , ptr <= 이면 T (empty)
    def is_full(self) : 
        return self.ptr == self.capacity 

    def push(self, value : Any) -> None :
        if self.is_full():
            raise FixedStack.Full 
        self.stk[self.ptr] = value
        self.ptr += 1                    # 가득 차있으면 FULL raise , 아니면 stk 인덱스에 value 추가하고 ptr +1    

    def pop(self) -> Any :
        if self.is_empty() :
            raise FixedStack.Empty
        self.ptr -= 1 
        return self.stk[self.ptr]        # ptr이 5개라면 pop할 값은 stk[4] 이기 때문. 

    def peek(self) -> Any : 
        if self.is_empty() :
            raise FixedStack.Empty
        return self.stk[self.ptr -1]     # 꼭대기 값만 반환하고 데이터를 입출력하지는 않음.

    def clear(self) -> None :
        self.ptr = 0                     # push, pop 작업은 ptr을 기반으로 이루어지는데 ptr = 0이되면 다 사라짐 

    def find(self, value: Any) -> Any :
        for i in range(self.ptr-1, 0 -1 , -1) :
            """ 검색은 top -> bottom으로 역순 """
            if self.stk[i] == value :       # 찾는 값 o, 그 값의 인덱스 반환 
                return i                    
        return -1               # 검색 실패   
    def count(self, value :Any) -> int : 
        c = 0 
        for i in range(self.ptr) : 
            if self.stk[i] == value :
                c += 1
        return c                    # stk 중에 찾는 값 value의 개수가 총 몇개인가 

    def __contains__(self, value : Any) -> bool :
        return self.count(value) > 0 

    def dump(self) :
        ''' 스택의 모든 데이터를 출력 (bottom ~ top)'''
        if self.is_empty() : 
            print('스택은 비어있습니다.')
        else :
            print(self.stk[:self.ptr])  # index  : 0 ~ ptk-1