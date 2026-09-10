from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums) #{num: freq}
        heap = [] #[(freq, num)]

        for num, freq in counts.items():
            heapq.heappush(heap, (freq, num))

            if len(heap) > k:
                heapq.heappop(heap)
            
        return [num for freq, num in heap]
