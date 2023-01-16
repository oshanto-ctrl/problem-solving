# problem link: https://leetcode.com/problems/sqrtx/


class Solution(object):
    def mySqrt(self, x):
        l = 0
        r = x
        res = 0
        
        while(l <= r):
            m = (l + r) // 2
            
            if m * m <= x:
                res = m
                l = m + 1
            else:
                r = m - 1
        
        return res
        








 