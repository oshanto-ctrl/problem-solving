# https://www.geeksforgeeks.org/problems/find-length-of-loop/1
'''
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''

class Solution:
    # Count the nodes in a loop
    def node_counter(self, node):
        cnt = 1
        current_ptr = node
        while current_ptr.next != node:
            cnt += 1
            current_ptr = current_ptr.next
        
        return cnt
    
    
    # Function to find the length of a loop in the linked list.
    def countNodesInLoop(self, head):
        #code here
        slow_ptr = head
        fast_ptr = head
        
        while slow_ptr is not None and fast_ptr is not None and fast_ptr.next is not None:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
            
            # Loop check
            if slow_ptr == fast_ptr:
                return self.node_counter(slow_ptr) # return counted nodes in loop
        
        return 0
