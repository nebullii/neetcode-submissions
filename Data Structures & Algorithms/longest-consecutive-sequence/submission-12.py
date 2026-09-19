class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        maxcount = 0

        for num in nums:
            # chcek if previous number exist
            if num - 1 not in nums:
                curr = num
                count = 1
                # while we have next number in nums
                while (curr + 1) in nums:
                    curr += 1
                    count += 1

                maxcount = max(count, maxcount)
        return maxcount