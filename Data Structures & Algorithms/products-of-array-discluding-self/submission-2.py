class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suffix = 1
        preffix = 1
        res = []

        for num in nums:
            res.append(preffix)
            preffix *= num

        for i in range(len(nums) - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        
        return res