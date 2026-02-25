class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s).most_common()
        return ''.join(char * count for char, count in freq)
       
        