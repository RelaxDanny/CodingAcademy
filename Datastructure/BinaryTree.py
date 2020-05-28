"""
Binary Tree: -> Binary search tree
    1. each node has at most 2 children nodes
    2. left node is always less than the right node
Insertion 할때 balanced and unbalanced가 있음
    Balanced tree => insert : O(log n) , find : O(log n)
    unbalanced tree => O(n)
Preorder : M L R
Inorder: L M R -> Binary search tree
Postorder : L R M

[8,3,10,1,6] 
    1. 8이 먼저 root가 되고 3이 들어왔을때 8보다 작으면 왼쪽 크면 오른쪽 노드에 넣기 이걸 반복
[10,8,6,3,1]
    1.이건 나열 하면 1자로 되어서 log n이 형성이 되지 않음. unbalanced!
Search :
    1. root노드에서 시작 inorder형식으로 계속해서 찾음.
    2. 1을 찾는다고 가정했을때 8에서 3으로 3에서 1은 더작으니 또 왼쪽으로 찾으면 out.
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
        # root가 none이면 들어오는 data가 바로 root가 됨
        if self.root is None:
            self.root = Node(data)
        else:
            # else find the location of the new node
            # is data given less or greater?
            self._insert(data, self.root) #helper method

    def _insert(self, data, cur_node):
        #check where we are
        if data < cur_node.data: 
            if cur_node.left is None:
                cur_node.left = Node(data)
            else:
                self._insert(data, cur_node.left) #recursively go to left if left of the root is not None
        elif data > cur_node.data:
            if cur_node.right is None:
                cur_node.right = Node(data)
            else:
                self._insert(data, cur_node.right)
        else:
            #if data given has duplicate elements
            print("Value is already in the tree.")
    
    def find(self, data):
        if self.root: #if root is not none
            is_found = self._find(data, self.root) #true or false
            if is_found:
                return True
            return False #else
        else:#if no nodes in the tree
            return None

    def _find(self, data, cur_node):
        if data > cur_node.data and cur_node.right:
            return self._find(data, cur_node.right) #recursion
        elif data < cur_node.data and cur_node.left:
            return self._find(data, cur_node.left)
        if data == cur_node.data:
            return True
    
bst = BST()

bst.insert(4)
bst.insert(7)
bst.insert(5)
bst.insert(2)
bst.insert(10)

print(bst.find(11))