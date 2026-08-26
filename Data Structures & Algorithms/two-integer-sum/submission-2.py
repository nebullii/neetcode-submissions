class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = {}
        for i, num in enumerate(nums):
            b = target - num
            if b in a:
                return [a[b], i]
            a[num] = i
