class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m, n = len(matrix), len(matrix[0])

        for i in range(m):

            l, r = 0, len(matrix[0])
            while l<r:
                k = (l+r)//2

                if matrix[i][k] == target: return True
                elif matrix[i][k] < target: l = k + 1
                else: r = k
        return False