class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        res = []
        RIGHT, DOWN, LEFT, UP = 1, 2, 3, 4

        i,j =0, 0

        rWall, dWall, lWall, uWall = n, m, -1, 0
        direction = RIGHT
        while len(res) != m*n:
            if direction == RIGHT:
                while j < rWall:
                    res.append(matrix[i][j])
                    j += 1
                i, j = i + 1, j-1
                direction = DOWN
                rWall -= 1
            elif direction == DOWN:
                while i < dWall:
                    res.append(matrix[i][j])
                    i += 1
                i, j = i-1, j-1
                direction = LEFT
                dWall -= 1
            elif direction == LEFT:
                while j > lWall:
                    res.append(matrix[i][j])
                    j -= 1
                i, j = i - 1, j + 1
                direction = UP
                lWall += 1
            else:
                while i > uWall:
                    res.append(matrix[i][j])
                    i -= 1
                i, j = i + 1, j + 1
                direction = RIGHT
                uWall += 1
        return res