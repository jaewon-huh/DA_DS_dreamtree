# 이진 검색트리 binary search tree

from __future__ import annotations
from typing import Any, Type

class Node :

    def __init__(self, key :Any , value : Any, left: Node = None , right : Node = None):
        
        self.key = key 
        self.value = value
        self.left = left
        self.right = right 
    

class BinarySearchTree: 

    def __init__(self) -> None:
        self.root = None        # 루트 

    def search(self, key) -> Any : 
        p = self.root           # 루트를 주목'노드'로 
        while True :
            if p is None :          # 검색 실패 
                return None         
            if key == p.key :
                return p.value
            elif key < p.key :
                p = p.left
            else :
                p = p.right

    def add(self, key , value) -> bool :
        """키 : key, 값 : value 인 노드 삽입"""

        def add_node(node :Node, key, value) :
            """node를 루트로 하는 서브 트리에 노드 삽입
                node : 주목 노드 """
            if key == node.key :
                return False                # 이미 key가 트리 안에 존재 
            elif key < node.key :
                if node.left is None : 
                    node.left = Node(key,value, None ,None )    # 노드 삽입 
                else :
                    add_node(node.left ,key ,value)         
                    # 왼쪽자식 노드 o , 왼쪽 자식 노드를 주목노드로 하고 재귀 
            else:   # key > node.key
                if node.right is None:
                    node.right = Node(key, value, None, None )  # 노드 삽입
                else: 
                    add_node(node.right,key, value)
            return True         # 삽입 완료

        if self.root is None :      # 빈 트리 
                self.root =Node(key,value, None, None)  # 삽입 
                return True
        else :                       # 빈트리 x 
                return add_node(self.root, key, value)   # 이제 진짜 삽입단계로 
    # 삭제 
    def remove(self, key :Any) -> bool : 
        p = self.root               # 스캔중인 노드
        parent = None               # 스캔중인 노드의 부모 
        is_left_child = True        # p가 부모노드의 왼쪽 자식인지 
        while True :
            if p is None : 
                return False        

            if key == p.key :
                break               # 삭제할 것 찾음
            else : 
                parent == p         # 부모노드는 p 
                if key < p.key :
                    is_left_child = True
                    p = p.left      # 왼쪽 서브트리 탐색 
                else : 
                    is_left_child = False
                    p = p.right     # 오른쪽 서브트리 탐색
        
        if p.left is None :         # 삭제할 노드에 왼쪽 자식 X          
            if p is self.root :
               self.root = p.right
            elif is_left_child :
                parent.left = p.right
            else :
                parent.right = p.right
        
        elif p.right is None :      # 삭제할 노드에 오른쪽 자식 X 
            if p is self.root :
                self.root = p.left
            elif is_left_child:
                parent.left = p.left
            else : 
                parent.right = p.left 

        else :                      # 자식 2
            parent = p 
            left = p.left           # 서브트리 중 가장 큰 노드 
            is_left_child = True 
            while left.right is not None : 
                parent = left
                left = left.right
                is_left_child = False
            
            p.key = left.key            # 교체작업 (p와 left)
            p.value = left.value    
            if is_left_child :
                parent.left = left.left
            else :
                parent.right = left.left
        return True
    
    # 오름차순 출력 dump() , 내림차순 reverse
    def dump(self, reverse = False) :
        def print_subtree(node: Node) : 
            if node is not None :  
                print_subtree(node.left)            # 왼쪽 자식 재귀 
                print(f'{node.key} {node.value}')   # 노드 방문 
                print_subtree(node.right)           # 오른쪽 자식 재귀 

        def print_subtree_rev(node: Node) :
            if node is not None :  
                print_subtree_rev(node.right)            
                print(f'{node.key} {node.value}')   
                print_subtree(node.left)           
       
        print_subtree_rev(self.root) if reverse else print_subtree(self.root)

    # 최소 키와 최대 키 반환 
    def min_key(self) :
        if self.root is None :                      # 비어있삼
            return None         
        p = self.root       
        while p.left is not None :                  # 왼쪽 자식 o  
            p = p.left          
        return p.key                            # 왼쪽자식 root가 최소 키 

    def max_key(self) :
        if self.root is None : 
            return None 
        p = self.root 
        while p.right is not None :
            p = p.right
        return p.key                            # 오른쪽 자식 root가 최대 키 
