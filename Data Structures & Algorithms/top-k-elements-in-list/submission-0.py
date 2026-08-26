class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_frequency = defaultdict(int)
        for num in nums:
            count_frequency[num] += 1
            
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, freq in count_frequency.items():
            bucket[freq].append(num)
        
        result = []
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result

