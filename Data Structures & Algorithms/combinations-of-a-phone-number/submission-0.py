class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        
        if not digits:
            return []

        digitToLetters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backtrack(index, curString):
            if len(digits) == index:
                result.append(curString)
                return

            letters = digitToLetters[digits[index]]

            for letter in letters:
                backtrack(index + 1, curString + letter)

        backtrack(0, "")
        return result 

