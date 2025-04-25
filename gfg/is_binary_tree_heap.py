# https://www.geeksforgeeks.org/problems/is-binary-tree-heap/1
'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
from collections import deque
class Solution:
    #Your Function Should return True/False
    def isHeap(self, root):
        
        if not root:
            return True
        
        # level-order traversal
        queue = deque()
        queue.append(root)
        
        empty_child = False
        
        while queue:
            curr = queue.popleft()
            
            # left
            if curr.left:
                if empty_child:
                    return False # Isn't complete
                if curr.data < curr.left.data:
                    return False # Isn't max-heap
                queue.append(curr.left)
            else:
                empty_child = True
            
            # right
            if curr.right:
                if empty_child:
                    return False # Isn't complete
                if curr.data < curr.right.data:
                    return False # Isn't max-heap
                queue.append(curr.right)
            else:
                empty_child = True
                
                
        return True
