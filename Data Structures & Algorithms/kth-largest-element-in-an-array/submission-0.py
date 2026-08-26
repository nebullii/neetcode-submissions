class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-a for a in nums]
        heapq.heapify(nums)

        for _ in range(k - 1):
            heapq.heappop(nums)
        return -nums[0]