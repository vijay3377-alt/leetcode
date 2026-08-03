class Solution:
    def stoneGameIII(self, stoneValue):
        n=len(stoneValue)
        dp=[0]*(n+3)
        for i in range(n-1,-1,-1):
            total=0
            dp[i]=float("-inf")
            for k in range(3):
                if i+k<n:
                    total+=stoneValue[i+k]
                    dp[i]=max(dp[i],total-dp[i+k+1])
        if dp[0]>0:
            return "Alice"
        elif dp[0]<0:
            return "Bob"
        else:
            return "Tie"
        