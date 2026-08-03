class Solution:
    def stoneGameIII(self, stoneValue):
        n=len(stoneValue)
        dp=[0]*(n+3)
        for i in range(n-1,-1,-1):
            total=0
            dp[i]=float("-inf")
            for j in range(3):
                if i+j<n:
                    total+=stoneValue[i+j]
                    dp[i]=max(dp[i],total-dp[i+j+1])
        if dp[0]>0:
            return "Alice"
        elif dp[0]<0:
            return "Bob"
        else:
            return "Tie"
        