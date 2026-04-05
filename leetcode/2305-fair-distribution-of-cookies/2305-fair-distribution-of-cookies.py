class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        distribution = [0] * k
        self.ans = float('inf')

        def backtrack(i):
            if i == len(cookies):
                self.ans = min(self.ans, max(distribution))
                return

            for j in range(k):
                distribution[j] += cookies[i]
                if distribution[j] < self.ans:
                    backtrack(i + 1)
                distribution[j] -= cookies[i]
                if distribution[j] == 0:
                    break

        backtrack(0)
        return self.ans
        