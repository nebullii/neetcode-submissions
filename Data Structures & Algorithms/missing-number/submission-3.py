class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        seen = set(nums)
        n = len(nums)
        for num in range(0, n + 1):
            if num not in nums:
                return num