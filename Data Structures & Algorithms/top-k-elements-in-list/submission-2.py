class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(list)

        for i, num in enumerate(nums):
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        sorted_key = sorted(freq.keys(), key=freq.get, reverse=True)
        return sorted_key[:k]


        