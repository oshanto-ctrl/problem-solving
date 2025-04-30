# https://www.geeksforgeeks.org/problems/pascal-triangle0652/1
class Solution:
    def helper(self, n, r):
        ans = 1
        for i in range(r):
            ans = ans * (n - i)
            ans = ans // (i + 1)
        return ans
        
	def nthRowOfPascalTriangle(self, n):
	    ans = []
	    for i in range(1, n+1):
	        ans.append(self.helper(n-1, i-1))
	    return ans
