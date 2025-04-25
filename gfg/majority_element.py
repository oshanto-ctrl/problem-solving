# https://www.geeksforgeeks.org/problems/majority-element-1587115620/1
class Solution:
    def majorityElement(self, arr):
        freq = {}
        for i in arr:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        thresh = len(arr)//2
        result = -1
        for k, v in freq.items():
            if v > thresh:
                result = k
                break
        return result
