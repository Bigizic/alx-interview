#!/usr/bin/python3
"""A Technical interview question
"""


def island_perimeter(grid):
    """Created a new list from the grid that forms each cell from each
        column of the original gird, then i count how many times 1 in
        the new list rows and same thing with the grid, then i add both
        and multiply by 2
    """
    n_row = len(grid)
    n_col = len(grid[0])
    perimeter = 0

    for row in range(n_row):
        for col in range(n_col):
            if grid[row][col] == 1:
                if row == 0 or grid[row - 1][col] == 0:
                    perimeter += 1
                if row == n_row - 1 or grid[row + 1][col] == 0:
                    perimeter += 1
                if col == 0 or grid[row][col - 1] == 0:
                    perimeter += 1
                if col == n_col - 1 or grid[row][col + 1] == 0:
                    perimeter += 1
    return perimeter
