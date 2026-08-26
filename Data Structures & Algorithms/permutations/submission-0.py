class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def permute(start):
            if start == len(nums):
                result.append(nums[:])

            for i in range(start, len(nums)):
                nums[i], nums[start] = nums[start], nums[i]
                permute(start + 1)
                nums[i], nums[start] = nums[start], nums[i]
            
        permute(0)
        return result