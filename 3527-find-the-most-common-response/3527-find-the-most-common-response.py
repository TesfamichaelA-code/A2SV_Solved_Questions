class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        counter = Counter()
        for day in responses:
            unique = set(day)
            for word in unique:
                counter[word] += 1

        max_freq = max(counter.values())
        candidates = [word for word, freq in counter.items() if freq == max_freq]

        return min(candidates)
       
        