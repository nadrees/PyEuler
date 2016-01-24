grid_size = 20

grid = list()
for i in range(0, grid_size + 1):
    grid.append([0] * (grid_size + 1))

def num_paths_at(x, y):
    if grid[x][y] == 0:
        if x == 0 and y == 0:
            grid[x][y] = 1
        elif x == 0:
            grid[x][y] = num_paths_at(x, y - 1)
        elif y == 0:
            grid[x][y] = num_paths_at(x - 1, y)
        else:
            grid[x][y] = num_paths_at(x - 1, y) + num_paths_at(x, y - 1)
    return grid[x][y]

answer = num_paths_at(grid_size, grid_size)

print(answer)