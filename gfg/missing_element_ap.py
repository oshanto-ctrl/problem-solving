# https://www.geeksforgeeks.org/problems/missing-element-of-ap2228/1
# Partially Solved.
# practice:

# Missed the corner cases: Wrong outputs
def getMissingNumber(arr):
    n = len(arr)
    asc = arr[0] <= arr[-1]

    # the diff
    diff1 = abs(arr[1] - arr[0])
    diff2 = abs(arr[n-1] - arr[n-2])
    diff3 = abs(arr[n-1] - arr[0]) // n

    if diff1 == diff2:
        diff = diff1
    elif diff1 == diff3:
        diff = diff1
    else:
        diff = diff2

    if diff == 0:
        return arr[0]
    
    exp_ans = ((2 * arr[0] + n * diff) * (n + 1)) // 2
    s = sum(arr)
    ans = exp_ans - s
    return ans 

# A simple solution: Partially passed
def getAnswer(arr):
    """
    Find the missing element in array
    by brute force.
    """
    n = len(arr)
    f = arr[0]
    s = arr[1]
    diff = (s - f)
    # diff = (arr[-1] - arr[0]) // n
    missing_element = 0
    found = False
    
    for i in range(n - 1):
        if arr[i+1] - arr[i] != diff:
            missing_element = arr[i] + diff
            found = True
            break
    # if nothing found, last elem + diff
    if not found:
        missing_element = arr[-1] + diff

    return missing_element





# Driver
# arr = [2, 4, 8, 10, 12, 14]
# arr = [1, 6, 11, 16, 21, 31]
# arr = [4, 7, 10, 13, 16] # 19
arr = [41, 21, 11] # 1
# missing_element = getAnswer(arr)
missing_element = getMissingNumber(arr)
print("Missing element: ", missing_element)

