# 포인터로 연결리스트 구현 
from __future__ import annotations
from traceback import print_tb # 인자로 자기 타입 전달
from typing import Any,Type

class Node :
    """노드 클래스"""

    def __init__(self, data : Any = None, next : Node = None) :
        self.data = data
        self.next = next
    
class LinkedList :
    """ 연결 리스트 클래스 """

    def __init__(self) -> None:
        self.no = 0                 # 노드의 개수 
        self.head = None            # 머리 노드 (head is None : 빈 연결리스트 )
        self.current = None         # 주목 노드 

    def __len__(self) -> int :
        return self.no

    def search(self, data) -> int :
        """ 값을 검색하고 존재하면 인덱스 반환 """
        cnt = 0                     # 카운터용 변수(인덱스 ) 
        ptr = self.head             # 스캔중인 노드 
        while ptr is not None : 
            if ptr.data == data : 
                self.current = ptr
                return cnt 
            cnt += 1
            ptr = ptr.next
        return - 1                     # 찾지 못함

    def __contains__(self, data :Any) -> bool :
        return self.search(data) >= 0 


    """ 삽입  """

    def add_first(self, data : Any) : 
        ptr = self.head                # 삽입전 머리노드 
        self.head = self.current = Node(data, ptr)      # head를 새 노드로 추가 (현재노드 , 참조값이 링크는 ptr)
        self.no += 1
         
    def add_last(self, data) :
        if self.head is None :                  # 비어있으면 , 맨 앞 노드 추가 
            self.add_first(data)      
        else :
            ptr = self.head
            while ptr.next is not None :        # head 다음 노드가존재함 
                ptr = ptr.next                  # 종료조건 : 다음 노드가 없는 ptr
            ptr.next = self.current = Node(data, None)
            self.no += 1

    """ 삭제 """
    def remove_first(self) :
        if self.head is not None :
            self.head = self.current = self.head.next       # head 노드를 head.next 노드로 변경 
        self.no -= 1
    # 노드가 1개뿐 : head.next = None -> 빈리스트 

    def remove_last(self):
        if self.head is not None :
            if self.head.next is None :                     # 노드가 1개
                self.remove_first   
            else :
                ptr = self.head                             # 스캔중인 노드
                pre = self.head                             # 스캔중인 노드의 앞 노드 

            while ptr.next is not None : 
                pre = ptr                                   # A - B
                ptr = ptr.next                              # A pre B ptr
            pre.next = None                                 # A -x- B
            self.current = pre
            self.no -=1 

    def remove(self, p : Node) :
        """ Node p를 삭제함 """
        if self.head is not None : 
            if p is self.head() :
                self.remove_first()
            else  :                                        # p가 첫번째 head 노드는 아님 
                ptr = self.head
                 
                while ptr.next is not p :                  # head(ptr) - 2 - .. p - 
                    ptr = ptr.next 
                    if ptr is None :                       # head - None   
                        return                             # : ptr은 리스트에 존재하지 않음 
                # 반복문 종료 ptr.next == p       (ptr - p)
                ptr.next = p.next                  #ptr - p.next        
                self.current = ptr
                self.no -= 1

    def remove_current_node(self) :
        self.remove(self.current)

    def clear(self) :
        """ 전체 삭제 """
        while self.head is not None :
            self.remove_first()

        self.current = None
        self.no = 0 
                
    """ 주목노드 """
    def next(self) -> bool :
        """ 주목노드를 한칸 뒤로 이동 """
        if self.current is None or self.current.next is None : 
            return False
        self.current = self.current.next
        return True

    def print_current_node(self) :
        if self.current is None :
            print('주목 노드가 존재하지 않습니다.')
        else :
            print(self.current.data)

    def print(self) : 
        ptr = self.head

        while ptr is not None :
            print(ptr.data)
            ptr = ptr.next 
            
                    