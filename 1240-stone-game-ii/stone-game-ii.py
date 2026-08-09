class Solution(object):
    def stoneGameII(self, piles):
        n = len(piles)
        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]
        dp = [[0] * (n + 1) for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for M in range(n, 0, -1):
                if i + 2 * M >= n:
                    dp[i][M] = suffix[i]
                    continue
                best = 0
                for X in range(1, 2 * M + 1):
                    if i + X > n:
                        break
                    current = suffix[i]
                    current -= dp[i + X][max(M, X)]
                    best = max(best, current)
                dp[i][M] = best
        return dp[0][1]