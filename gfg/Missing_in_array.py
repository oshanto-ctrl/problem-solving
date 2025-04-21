# https://www.geeksforgeeks.org/problems/missing-number-in-array1416/1
class Solution:
    def missingNum(self, arr):
        n = len(arr) + 1
        expected = (n * (n + 1)) // 2
        actual = sum(arr)
        output = expected - actual
        return output
