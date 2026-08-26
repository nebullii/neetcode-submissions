class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)]
        freq = defaultdict(int)
        res = []

        for num in nums:
            freq[num] += 1
        
        for num, count in freq.items():
            buckets[count].append(num)
        
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
