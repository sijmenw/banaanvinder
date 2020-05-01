# created by Sijmen van der Willik
#  16/04/2018 13:41

import numpy as np

grid_width = 13

grid_input = "N A N B A B N B A N A B B N A A N A B B A B N B B N A A N A B A N N B N B A B A A N A A N A B A A A N B N B N A A B A A B B B B N A N B N N A B B B A A B A A B N B B A N A A N A B B B N A B A A A A N B B A N A A N N N N B N A A A A N B A B N A B A N A A N A B B A A A N A B N B A A B N N N B B A B A N B A A N B B A B B A A N N A N B A A N A N B N B A B B N B A N B A A A B A N A B A A A B B A N A A N A B N A B N B B N B A B A A N N A B A B A N B A B N B B A N A B A A N A N B A B N N B A N A N N A A N A B B N N A N A N A B B A A B N N B A B B A N B A N B A B B B B N B A A B B A B A B N B A B B N B A B B B A N A A N B N"

grid_input = grid_input.split(" ")

grid_height = len(grid_input) // grid_width

grid = np.ndarray((grid_height, grid_width), dtype=object)

col_n = 0
for i in range(len(grid_input)):
    if i % grid_height == 0 and i > 0:
        col_n += 1

    row_n = i % grid_height

    grid[row_n][col_n] = grid_input[i]

print("GRID:")
print(grid)


def check_banaan(grid, row, col):
    dirs = [
        [-1,  0],
        [-1, -1],
        [0,   1],
        [1,   1],
        [1,   0],
        [1,  -1],
        [0,  -1],
        [-1, -1]
    ]

    banaan = 'BANAAN'

    result = []

    # for each direction
    for dir in dirs:

        # create empty coord list for this direction
        tmp_coord_list = []

        # check 6 steps
        for i in range(6):
            tmp_row = row + i * dir[0]
            tmp_col = col + i * dir[1]

            # out of bounds
            if tmp_row < 0 or tmp_col < 0 or tmp_row >= grid_height or tmp_col >= grid_width:
                break

            tmp_coord_list.append([tmp_row, tmp_col])

            if grid[tmp_row, tmp_col] == banaan[i]:
                if i == 5:
                    result.append(tmp_coord_list)
            else:
                break

    return result


hits = []

for row_n in range(len(grid)):
    for col_n in range(len(grid[0])):
        tmp_result = check_banaan(grid, row_n, col_n)

        if len(tmp_result) > 0:
            hits += tmp_result

print("\nAantal bananen gevonden: " + str(len(hits)))

coords = []

for banaan in hits:
    for coord in banaan:
        coords.append(coord)

banaan_grid = np.ndarray((grid_height, grid_width), dtype=object)
banaan_grid.fill("_")

for coord in coords:
    banaan_grid[coord[0], coord[1]] = grid[coord[0], coord[1]]

print("\nBANAAN grid:\n", banaan_grid)
