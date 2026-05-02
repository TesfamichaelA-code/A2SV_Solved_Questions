class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        
        for u, v in edges:
            graph[u].append(v)
        
        ancestors = [set() for _ in range(n)]
        
        def dfs(start, node):
            for nei in graph[node]:
                if start not in ancestors[nei]:
                    ancestors[nei].add(start)
                    dfs(start, nei)
        for i in range(n):
            dfs(i, i)
        return [sorted(list(s)) for s in ancestors]