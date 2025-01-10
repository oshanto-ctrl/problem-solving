# https://www.geeksforgeeks.org/problems/count-distinct-elements-in-every-window/1
class Solution:
    def countDistinct(self, arr, k):
        n = len(arr)
        result = [0] * (n-k+1)
        for i in range(n - k + 1):
            wu = set(arr[i:i+k])
            result[i] = len(wu)
        return result
