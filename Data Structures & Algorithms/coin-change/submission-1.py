from functools import lru_cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)

        @lru_cache(maxsize=None)
        def dfs(i):
            if i == 0: return 0
            best = float('inf')

            for c in coins:
                if i >= c:
                    best = min(best, 1 + dfs(i - c))
            return best
            
        res = dfs(amount)
        return res if res != float('inf') else -1
