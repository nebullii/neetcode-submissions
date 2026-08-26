class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Helper function to count character frequencies
        def word_count(n):
            char_count_n = {}
            for char in n:
                if char in char_count_n:
                    char_count_n[char] += 1
                else:
                    char_count_n[char] = 1
            return char_count_n
        
        # Step S2: Check if lengths are different
        if len(s) != len(t):
            return False
        
        # Step S5: Compare the dictionaries
        return word_count(s) == word_count(t)
