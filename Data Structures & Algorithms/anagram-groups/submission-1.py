class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map_res = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for s in word:
                count[ord(s) - ord('a')] += 1
            map_res[tuple(count)].append(word)

        return list(map_res.values())
