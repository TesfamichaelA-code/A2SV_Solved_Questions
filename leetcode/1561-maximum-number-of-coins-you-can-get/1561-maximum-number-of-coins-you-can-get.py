class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        que = deque(piles)
        res = 0
        while len(que) > 0:
            que.pop()
            res += que.pop()
            que.popleft()
        return res

       

        
        