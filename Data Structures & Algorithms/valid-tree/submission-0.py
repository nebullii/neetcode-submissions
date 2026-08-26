class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges: return True

        preMap = {i: [] for i in range(n)}
        for e1, e2 in edges:
            preMap[e1].append(e2)
            preMap[e2].append(e1)

        visit = set()

        def dfs(e, prev):
            if e in visit:
                return False

            visit.add(e)
            for j in preMap[e]:
                if j == prev: continue
                if not dfs(j, e): return False
            return True
        
        return dfs(0, -1) and n == len(visit)
