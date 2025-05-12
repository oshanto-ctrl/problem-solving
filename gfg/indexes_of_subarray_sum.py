# Problem link: https://www.geeksforgeeks.org/problems/subarray-with-given-sum-1587115621/1
class Solution:
    def subarraySum(self, arr, target):
        low = 0
        current_sum = 0
        n = len(arr)
        for high in range(n):
            current_sum += arr[high]
            
            while current_sum > target and low <= high:
                current_sum -= arr[low]
                low += 1
            
            if current_sum == target:
                return [low+1, high+1]
        
        # Nothing found
        return [-1]
