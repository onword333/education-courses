"""463. Island Perimeter"""


class Solution:

    def is_land_perimeter(self, grid) -> int:
        """находит периметр острова"""
        per = 0

        for i, row in enumerate(grid):
            for j, cell in enumerate(row):

                # Для каждой ячейки с землей, проверим её соседей (слева и сверху).
                # Если соседняя ячейка тоже земля, уменьшить периметр на 2 для
                # каждого общего соседа, так как каждая сторона будет считаться дважды.
                # Т.е. между двумя ячейками земли существует разделяющая линия, при
                # добавлении к переметру 4 + 4 = 8 по факту мы учитываем разделяющую
                # линию между ними дважды, поэтому необходимо уменьшить на 2
                if cell == 1:
                    per += 4

                    if i > 0 and grid[i - 1][j] == 1:
                        per -= 2
                    if j > 0 and grid[i][j - 1] == 1:
                        per -= 2
        return per



grid = [
    [0,1,0,0],
    [1,1,1,0],
    [0,1,0,0],
    [1,1,0,0]
]

grid2 = [[1]]
grid3 = [[1,0]]

print(Solution().is_land_perimeter(grid))
print(Solution().is_land_perimeter(grid2))
print(Solution().is_land_perimeter(grid3))

