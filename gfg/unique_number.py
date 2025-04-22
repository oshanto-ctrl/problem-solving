# https://www.geeksforgeeks.org/problems/find-unique-number/1
class Solution:
    def findUnique(self, arr):
        # for i in arr:
        #     if arr.count(i) == 1:
        #         return i
        # return -1
        
        n = len(arr)
        unique = None
        i = 0
        arr.sort()
        while i < n:
            if(i == n-1 or arr[i] != arr[i + 1]) and (i == 0 or arr[i] != arr[i - 1]):
                unique = arr[i]
                break
            if i < n - 1 and arr[i] == arr[i + 1]:
                i += 2
            else:
                i += 1
        return unique
