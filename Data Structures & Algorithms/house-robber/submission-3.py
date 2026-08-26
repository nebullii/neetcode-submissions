from functools import lru_cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        @lru_cache(maxsize=None)
        def dfs(i):
            if i >= n: return 0
            return max(dfs(i + 1), nums[i] + dfs(i + 2))
        
        return dfs(0)