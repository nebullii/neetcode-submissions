class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == h:
            return max(piles)
        
        l, r = 1, max(piles)
        while l < r:
            m = l + (r - l) // 2
            total = sum(math.ceil(pile / m) for pile in piles)
            if total <= h:
                r = m
            else:
                l = m + 1
        return l