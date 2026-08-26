class Solution:
    def climbStairs(self, n: int) -> int:
        prev1 = prev2 = 1

        for i in range(n - 1):
            tmp = prev1 
            prev1 = prev1 + prev2
            prev2 = tmp
        return prev1