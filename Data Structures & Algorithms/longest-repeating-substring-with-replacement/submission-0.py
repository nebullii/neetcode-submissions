class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        map_char = defaultdict(int)
        left = 0
        max_freq = 0

        for right in range(len(s)):
            map_char[s[right]] += 1
            max_freq = max(max_freq, map_char[s[right]])
        
            if (right - left + 1) - max_freq > k:
                map_char[s[left]] -= 1
                left += 1
            
            max_len = max(max_len, right - left + 1)
        
        return max_len

