class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i: [] for i in range(numCourses)}
        for c, p in prerequisites:
            preMap[c].append(p)

        visiting = set()
        visited = set()
        result = []

        def dfs(c):
            if c in visiting:
                return False
            if c in visited:
                return True
            visiting.add(c)

            for p in preMap[c]:
                if not dfs(p):
                    return False
            visiting.remove(c)
            visited.add(c)
            result.append(c)
            return result
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        return result
            