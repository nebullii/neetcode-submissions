class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(list)

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        return sorted(freq, key=freq.get, reverse=True)[:k]