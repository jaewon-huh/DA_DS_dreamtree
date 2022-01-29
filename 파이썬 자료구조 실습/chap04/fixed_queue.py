# 고정 길이 큐 클래스 구현 (FixedQueue)

import re
from typing import Any 

class FixedQueue: 

    class Empty(Exception) :
        pass

    class Full(Exception) :
        pass 

    def __init__(self, capacity : int) -> None :
        """ 큐 초기화 """
        self.no = 0
        self.front = 0
        self.rear = 0 
        self.capacity = capacity 
        self.que = [None] * capacity    # 큐 배열 

    def __len__(self) -> int : 
        return self.no 

    def is_empty(self) : 
        return self.no == 0

    def is_full(self) : 
        return self.no == self.capacity

    def enque(self, x: Any) -> None : 
        if self.is_full():
            raise FixedQueue.Full
        
        self.que[self.rear] = x 
        self.rear += 1 
        self.no += 1
        if self.rear == self. capacity :
            self.rear == 0                  # inque 후 큐가 꽉차서 front == rear 가 같아짐 
        
    def deque(self) -> Any : 
        if self.is_empty() :
            raise FixedQueue.Empty 
        
        x = self.que[self.front]
        self.front += 1 
        self.no -= 1 
        if self.front == self.capacity : 
            self.front == 0                 # 배열의 맨끝 원소가 front , deque -> +1 된 front 값이 인덱스를 넘어감 (front == capacity)           
        return x                            # 그래서 front 값을 0으로 되돌림. (다음 디큐 할 건 배열 맨 첫 원소)

    def peek(self) -> Any :   
        if self.is_empty() :
            raise FixedQueue.Empty
        return self.que[self.front]

    def find(self, value :Any) -> Any :
        """ 배열의 맨앞부터 맨끝까지 선형 검색 따라서 검색 식 """
        for i in range(self.no) :
            idx =(i+self.front) % self.capacity
            if self.que[idx] == value : 
                return idx
        return -1    
    
    def count(self, value :Any) -> bool :
        c = 0
        for i in range(self.no) : 
            idx =(i+self.front) % self.capacity
            if self.que[idx] == value : 
                c += 1 
        return c

    def __contains__(self, value) -> bool :
        return self.count(value)

    def clear(self) -> None : 
        self.no = self.front = self.rear = 0        # no , front, rear 값을 모두 초기화 

    def dump(self) :
        if self.is_empty(): 
            print('큐가 비어있습니다.')
        else :
            for i in range(self.no): 
                print(self.que[ (i+self.front) % self.capacity ], end = ' ')     #self.que[index]
            print()    