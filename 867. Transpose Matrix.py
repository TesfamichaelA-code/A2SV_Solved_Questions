class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        new = []

        for i in range(len(matrix[0])):
            new.append([])
            for j in range(len(matrix)):
                new[i].append(matrix[j][i])
        return new

        