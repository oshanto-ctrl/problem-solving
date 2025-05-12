# https://www.geeksforgeeks.org/problems/find-repetitive-element-from-1-to-n-1/1
class Solution:
    def findDuplicate(self, arr):
        if len(arr) < 2:
            return -1
        
        freq = {x: 0 for x in arr}
        for x in arr:
            freq[x] += 1
        for k, v in freq.items():
            if v == 2:
                return k
        return -1
