# Problem link: https://www.geeksforgeeks.org/problems/max-circular-subarray-sum-1587115620/0
#User function Template for python3

#Complete this function
#Function to find maximum circular subarray sum.
def circularSubarraySum(arr):
    # Total sum of arr
    total = sum(arr)
    
    min_subarray_sum = minimum_subarray_sum(arr)
    max_subarray_sum = maximum_subarray_sum(arr)
    
    # Negative case where total sum == min sub-arr sum
    # entire arr is negative
    if total == min_subarray_sum:
        return max_subarray_sum
    
    # max of (max-sub-arr-sum, total - min-sub-arr-sum)
    return max(max_subarray_sum, (total - min_subarray_sum))
    
    
# Get the maximum sub-array sum of linear array (Kadane)
def maximum_subarray_sum(arr):
    max_sum = curr_sum = arr[0]
    
    for num in arr[1:]:
        curr_sum = max(num, curr_sum + num)
        max_sum = max(max_sum, curr_sum)
    
    return max_sum

# Get the minimum sub-array sum of linear array (Kadane: Modified as circular)
def minimum_subarray_sum(arr):
    min_sum = curr_min = arr[0]
    
    for num in arr[1:]:
        curr_min = min(num, curr_min + num)
        min_sum = min(min_sum, curr_min)
    
    return min_sum
