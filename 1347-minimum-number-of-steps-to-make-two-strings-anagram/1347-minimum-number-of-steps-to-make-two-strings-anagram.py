class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count = Counter(s)
        ans = 0
        for c in t:
            count[c] -= 1
            if count[c] < 0:
                ans += 1
        return ans

        