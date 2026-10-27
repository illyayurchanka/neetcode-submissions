class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        l = len(coins)
        dp = {i: -1 for i in range(amount + 1)}
        for i in coins:
            dp[i] = 1
        for i in range(coins[0]+1, amount + 1):
            for c in coins:
                if c >= i:
                    continue
                elif dp[i - c] != -1:
                    if dp[i] == -1:
                        dp[i] = dp[i - c] + 1
                    else:
                        dp[i] = min(dp[i], dp[i - c] + 1)
        return dp[amount]