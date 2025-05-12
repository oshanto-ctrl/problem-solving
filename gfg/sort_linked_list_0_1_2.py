# https://www.geeksforgeeks.org/problems/given-a-linked-list-of-0s-1s-and-2s-sort-it/1
'''
	Function Arguments: head of the original list.
	Return Type: head of the new list formed.
	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}'''
	
class Solution:
    def segregate(self, head):
        checker = [0, 0, 0]
        p = head
        # get frequencies
        while p:
            checker[p.data] += 1
            p = p.next
        
        i = 0
        p = head # again
        while p:
            if checker[i] == 0:
                i += 1
            else:
                p.data = i
                checker[i] -= 1
                p = p.next # next node
        return head
