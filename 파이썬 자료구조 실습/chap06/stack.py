# 고정 길이 스택 클래스 구현 (deque를 사용)

from typing import Any, AnyStr
from collections import deque


class Stack : 

    def __init__(self, maxlen : int = 256) -> None : 
        self.capacity = maxlen
        self.__stk = deque([], maxlen)          # 빈 덱 생성 

    def __len__(self) : 
        return len(self.__stk)

    def is_empty(self) -> bool :
        return not self.__stk                   

    def is_full(self) -> bool : 
        return len(self.__stk) == self.__stk.maxlen      

    def push(self, value : Any) -> None :
        """ 스택에 value push """
        self.__stk.append(value)

    def pop(self) -> Any :
        """ 스택에서 데이터를 pop """
        return self.__stk.pop()
    
    def peek(self) -> Any : 
        return self.__stk[-1]

    def find(self, value: Any) -> Any :
        try :
            return self.__stk.index(value) 
        except ValueError :
            return -1 

    def count(self, value :Any) -> int :
        return self.__stk.count(value)

    def __contains__(self, value :Any ) -> bool : 
        return self.count(value)

    def dump(self) : 
        print(list(self.__stk))