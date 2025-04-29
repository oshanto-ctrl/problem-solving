# https://www.geeksforgeeks.org/problems/kth-smallest-element5635/1?page=1&company=Samsung,Oracle,Hike,Qualcomm,Wipro&sortBy=submissionsclass Solution:
    
    # Sorting algo
    def merge_sort(self, arr):
        n = len(arr)
        if n <= 1:
            return arr
        mid = n // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        
        # to sort
        left_half = self.merge_sort(left_half)
        right_half = self.merge_sort(right_half)
        
        return self.merge(left_half, right_half)
    
    def merge(self, left, right):
        merged = []
        l = 0
        r = 0
        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                merged.append(left[l])
                l+=1
            else:
                merged.append(right[r])
                r+=1
        
        merged.extend(left[l:])
        merged.extend(right[r:])
        return merged

    def kthSmallest(self, arr,k):
        arr = self.merge_sort(arr)
        result = arr[k-1]
        return result
        
        
