class Solution:
    
    #Function to find the length of longest common subsequence in two strings.
    def lcs(self,n,m,x,y):
        dp=[[0 for j in range(m+1)]for i in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                if x[i-1]==y[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return dp[n][m]
       
