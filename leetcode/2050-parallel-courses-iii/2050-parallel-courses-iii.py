class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = defaultdict(list)
        indegree = [0] * n

        for u, v in relations:
            graph[u - 1].append(v - 1)
            indegree[v - 1] += 1
        dp = time[:]

        queue = deque()
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            u = queue.popleft()
            
            for v in graph[u]:
                dp[v] = max(dp[v], dp[u] + time[v])
                indegree[v] -= 1       
                if indegree[v] == 0:
                    queue.append(v)
        
        return max(dp)