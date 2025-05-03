# https://www.geeksforgeeks.org/problems/prime-list--170646/1
"""
Definition for singly Link List Node
class Node:
    def __init__(self,x):
        self.val=x
        self.next=None

"""

class Solution:
    
    # check prime
    def is_prime(self, n):
        """Simple condition to check 
        if a number, n is prime or not"""
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while (i*i) <= n:
            if n % i == 0:
                return False
            i += 2
        return True
    
    # Check the nearest prime
    def check_nearest_prime(self, n):
        if self.is_prime(n):
            return n
        l = n - 1
        u = n + 1
        
        while True:
            if self.is_prime(l):
                return l
            if self.is_prime(u):
                return u
            l -= 1
            u += 1
        
    def primeList(self, head):
        curr = head
        while curr:
            curr.val = self.check_nearest_prime(curr.val)
            curr = curr.next
        
        return head
        

