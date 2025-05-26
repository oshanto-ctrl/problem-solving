# Problem Link: https://www.geeksforgeeks.org/problems/dice-throw5349/1

class Solution:
    def noOfWays(self, m,n,x):
            DP = [[0 for _ in range(x+1)] for _ in range(n+1)]
            DP[0][0] = 1
          
            for i in range(1, n+1):
                for j in range(1, x+1):
                    for k in range(1, m+1):
                        if (j >= k):
                            DP[i][j] += DP[i - 1][j - k]
            
            return DP[n][x]