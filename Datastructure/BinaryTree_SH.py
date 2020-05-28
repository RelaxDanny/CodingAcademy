"""
Binary Tree => Binary Search Tree
    1. Each node has at most 2 children nodes
    2. Left node is always less than the right node.

Insertion을 할때 
    1. balanced Tree => insert: O(log n), search : O(log n)
    2. Unbalanced Tree => insert: O(n), search : O(n)
Insert
[8,3,10,1,6]
    1. 8이 root node가 된다.
    2. 3 < 8 Left Node
    3. 10 > 8 right node
    4. 1 < 3 Left Node
    5. 3 < 6 Right Node

Search:
    1. Root Node에서 시작을 한다.
    2. Inorder 형식또는 Binary Search 의 halving 형식으로 값을 찾는다.
    3. 
"""
class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    def insert(self, data):
        #TO DO
        pass
    def _insert(self, data, cur_node):
        #TO Do
        pass
    def find(self, data): #True or False
        #To Do
        
        pass
    def _find(self, data, cur_node):
        #To do
        pass

bst = BST()
bst.insert()

print(bst.find())