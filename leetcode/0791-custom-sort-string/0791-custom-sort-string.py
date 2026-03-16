class Solution:
    def customSortString(self, order: str, s: str) -> str:
        permuted = []
        count =  Counter(s)
        for c in order:
            if c in count:
                permuted.append(c * count[c])
                del count[c]

        for c in count:
            permuted.append(c * count[c])

        return "".join(permuted)

                


        