# 원형 이중 연결리스트 구현 

from __future__ import annotations
from typing import Any, Type

class DoubleLinkedListIterator:
    """DoubleLinkedList의 반복자용 클래스"""

    def __init__(self, head: Node):
        self.head = head
        self.current = head.next

    def __iter__(self) -> DoubleLinkedListIterator:
        return self

    def __next__(self) -> Any:
        if self.current is self.head:
            raise StopIteration
        else:
            data = self.current.data
            self.current = self.current.next
            return data

class DoubleLinkedListReverseIterator:
    """DoubleLinkedList의 내림차순 반복자용 클래스"""

    def __init__(self, head: Node):
        self.head = head
        self.current = head.prev

    def __iter__(self) -> DoubleLinkedListReverseIterator:
        return self

    def __next__(self) -> Any:
        if self.current is self.head:
            raise StopIteration
        else:
            data = self.current.data
            self.current = self.current.prev
            return data        

class Node :

    def __init__(self, data: Any = None, prev : Node = None, next : Node = None):

        self.data = data
        self.prev =prev or self     # 앞쪽 prev 값이 None
        self.next =next or self     # 뒤쪽 next 값이 None - self


class DoubleLinkedList : 

    def __init__(self) : 
        self.head = self.current = Node()        # 더미 head노드 
        self.no = 0

    def __len__(self) : 
        return self.no
    
    def is_empty(self) -> bool : 
        return self.head.next is self.head       
        # 더미의 next가 자기 자신 (원형구조)

    def search(self, data) :
        cnt = 0 
        ptr =self.head.next         # 현재 스캔중인노드 A 첫노드 
        while ptr is not self.head  : # 노드가 비어있지 않음 
            if data == ptr.data : 
                self.current = ptr
                return cnt 
            cnt +=1
            ptr = ptr.next 
        return -1                      # 검색 실패   

    def __contains__(self, data) : 
        return self.search(data) >= 0 


    def print_current_node(self) :
        if self.is_empty(): 
            print('주목 노드는 없습니다.')
        else :
            print(self.current.data)        

    def print(self) : 
        ptr = self.head.next            # 더미 노드 다음 노드 
        while ptr is not self.head :    # 다음 노드가 더미노드가 아닌한 (맨끝 - 다음노드 더미노드 ) 
            print(ptr.data)
            ptr = ptr.next

    def print_reverse(self) : 
        ptr = self.head.prev            # 더미노드 이전노드 (맨뒤)
        while ptr is not self.head :    # 이전노드가 head가 아닌한  (맨 앞노드 이전 - 더미노드 )
            print(ptr.data)
            ptr = ptr.prev         
    # 주목 노드 이동 

    def next(self) -> bool : 
        """주목노드를 한칸뒤로 이동 current node"""       
        if self.is_empty() or self.current.next is self.head : # 노드가 비어있음 or 맨 끝노드임
            return False 
        self.current = self.current.next
        return True                         # 다음 노드가 존재하는 경우에만 이동 

    def prev(self) :

        if self.is_empty() or self.current.prev is self.head: 
            return False
        self.current = self.current.prev
        return True 
    
    # add
    def add(self, data :Any) :
        """ 주목노드 바로뒤에 노드 삽입 """     #  A - B(current) - (D 삽입) - C 
        node = Node(data, self.current, self.current.next)
        self.current.next.prev = node
        self.current.next = node
        self.current = node 
        self.no += 1 

    def add_first(self,data) :
        self.current = self.head
        self.add(data)

    def add_last(self, data) : 
        self.current = self.head.prev  # 맨뒤가 current 
        self.add(data)

    # 삭제 
    def remove_current_node(self) :             # A - B(current) - C  -> A - C 
        if not self.is_empty():
            self.current.prev.next = self.current.next 
            self.current.next.prev = self.current.prev
            self.current = self.current.prev 
            self.no -= 1
            if self.current is self.head :          # dummy - A(current) - B ->  dummy(current) - B - C 
               self.current = self.head.next        # dummy - B(current) - C 

    def remove(self, p: Node) : 
        """ Node p 를 삭제 """                  # dummy - A - B  - C(remove) - D
        ptr = self.head.next                

        while ptr is not self.head() :  # 비어있지 않아 
            if ptr is p :               # ptr = A 
                self.current =p 
                self.remove_current_node()
                break
            ptr = ptr.next              # 다음 검색  c삭제 : A - ptr =/ p , ptr.next = B =/ p , next ..
    
    def remove_first(self) :
        self.current =self.head.next 
        self.remove_current_node()

    def remove_last(self) :
        self.current =self.head.prev
        self.remove_current_node()

    def clear(self) :
        while not self.is_empty():
            self.remove_first()
            self.no =0 

    # 이터레이터 구현 
    def __iter__(self) -> DoubleLinkedListIterator : 
        return DoubleLinkedListIterator(self.head)

    def __reversed__(self) : # 내림차순 이터레이터 
        return DoubleLinkedListReverseIterator(self.head)
        
