class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        total = 0
        available = Counter(chars)
        for word in words:
            word_count = Counter(word)
            for ch in word_count:
                if word_count[ch] > available[ch]:
                    break
            else:
                total += len(word)
        return total

        