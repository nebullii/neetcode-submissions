class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []

        def countOnes(n):
            count = 0
            while n:
                count  += n % 2
                n = n >> 1
            return count

        for i in range(n + 1):
            result.append(countOnes(i))
        
        return result