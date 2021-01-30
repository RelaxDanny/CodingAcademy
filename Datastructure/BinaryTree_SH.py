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
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)
    def _insert(self, data, cur_node):
        #TO Do
        if data < cur_node.data:
            if cur_node.left is None:
                cur_node.left = Node(data)
            else:
                self._insert(data, cur_node.left)
        elif data > cur_node.data:
            if cur_node.right is None:
                cur_node.right = Node(data)
            else:
                self._insert(data, cur_node.right)

    def find(self, data): #True or False
        #To Do
        if self.root:
            is_found = self._find(data, self.root) #Boolean Type (True Or False)
            if is_found:
                return True
            return False
        else: # if no nodes in the tree
            return False

    def _find(self, data, cur_node):
        #To do
        if data > cur_node.data and cur_node.right:
            return self._find(data,cur_node.right)
        elif data < cur_node.data and cur_node.left:
            return self._find(data, cur_node.left)
        ##  결국에 찾을떄 까지
        if data == cur_node.data:
            return True
        

bst = BST()
bst.insert(4)
bst.insert(3)
bst.insert(2)
bst.insert(1)

print(bst.find(5))