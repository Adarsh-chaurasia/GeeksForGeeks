class Solution:
	def perfectSum(self, arr, n, sum):
		dp=[[0 for i in range(sum+1)]for j in range(n+1)]
		
		for i in range(n+1):
		    dp[i][0]=1
		    
		for i in range(1,n+1):
		    for j in range(1,sum+1):
		        if arr[i-1]<=j:
		            dp[i][j]=dp[i-1][j]+dp[i-1][j-arr[i-1]]
		        else:
		            dp[i][j]=dp[i-1][j]
		            
		            
		            
		            
		            
		mod=10**9+7            
		            
	    return dp[n][sum]%mod
		            
