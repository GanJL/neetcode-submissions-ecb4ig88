class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(remaining):
                if remaining == 0:
                    return 0
                if remaining < 0:
                    return float('inf')
                
                if remaining in memo:
                    return memo[remaining]

                minCoins = float('inf')
                
                for coin in coins:
                    res = dfs(remaining - coin)
                    if res != float('inf'):
                        minCoins = min(minCoins, res + 1)
                
                memo[remaining] = minCoins
                return minCoins
                
        ans = dfs(amount)
        return ans if ans != float('inf') else -1
