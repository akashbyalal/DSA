class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        res = []
        TOP, LEFT, RIGHT, BOTTOM = 1, 2, 3, 4

        direction = RIGHT

        i, j = 0, 0

        RIGHT_WALL = n
        LEFT_WALL = -1
        TOP_WALL = 0
        BOTTOM_WALL = m

        while len(res) != m*n:
            if direction == RIGHT:
                while j < RIGHT_WALL:
                    res.append(matrix[i][j])
                    j+=1
                i, j = i+1, j-1
                RIGHT_WALL -= 1
                direction = BOTTOM
            elif direction == BOTTOM:
                while i < BOTTOM_WALL:
                    res.append(matrix[i][j])
                    i += 1
                i, j = i - 1, j - 1
                BOTTOM_WALL -= 1
                direction = LEFT
            elif direction == LEFT:
                while j > LEFT_WALL:
                    res.append(matrix[i][j])
                    j -= 1
                i, j = i-1, j+1
                LEFT_WALL += 1
                direction = TOP
            else:
                while i > TOP_WALL:
                    res.append(matrix[i][j])
                    i -= 1
                i, j = i+1, j+1
                TOP_WALL += 1
                direction = RIGHT
        return res

