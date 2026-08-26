class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curSum = 0
        res = 0
        prefSum = {0: 1}

        for i in range(len(nums)):
            curSum += nums[i]
            diff = curSum - k
            if diff in prefSum:
                res += prefSum[diff] # be careful here
            
            if curSum in prefSum:
                prefSum[curSum] += 1
            else:
                prefSum[curSum] = 1
        return res