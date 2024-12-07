import numpy as np
from tqdm import tqdm

grid = open("day6-input.txt").readlines()
grid = [list(line.strip()) for line in grid]

# initial state of the guard
guard_pos = [49, 39]
guard_dir = "up"
print(f"Guard is at {guard_pos[0]+1,guard_pos[1]+1}, facing {guard_dir}")


def off_grid_check(guard_pos, guard_dir, grid):
    """
    Check whether the next move will take the guard off the grid
    """
    if guard_dir == "up" and guard_pos[0] == 0:
        return True
    elif guard_dir == "down" and guard_pos[0] == len(grid) - 1:
        return True
    elif guard_dir == "left" and guard_pos[1] == 0:
        return True
    elif guard_dir == "right" and guard_pos[1] == len(grid[0]) - 1:
        return True
    else:
        return False


def obstruction_check(guard_pos, guard_dir, grid):
    """
    Check whether the next move is obstructed by a #
    """
    if guard_dir == "up" and grid[guard_pos[0] - 1][guard_pos[1]] == "#":
        return True
    elif guard_dir == "down" and grid[guard_pos[0] + 1][guard_pos[1]] == "#":
        return True
    elif guard_dir == "left" and grid[guard_pos[0]][guard_pos[1] - 1] == "#":
        return True
    elif guard_dir == "right" and grid[guard_pos[0]][guard_pos[1] + 1] == "#":
        return True
    else:
        return False


def change_direction(guard_dir):
    """
    Rotate the direction of the guard 90 degrees clockwise
    """
    if guard_dir == "up":
        return "right"
    elif guard_dir == "right":
        return "down"
    elif guard_dir == "down":
        return "left"
    elif guard_dir == "left":
        return "up"


def move_guard(guard_pos, guard_dir, grid):
    """
    Return the new position of the guard
    """
    if guard_dir == "up":
        return [guard_pos[0] - 1, guard_pos[1]]
    elif guard_dir == "down":
        return [guard_pos[0] + 1, guard_pos[1]]
    elif guard_dir == "left":
        return [guard_pos[0], guard_pos[1] - 1]
    elif guard_dir == "right":
        return [guard_pos[0], guard_pos[1] + 1]


guard_pos_log = []
while not off_grid_check(guard_pos, guard_dir, grid):
    if obstruction_check(guard_pos, guard_dir, grid):
        guard_dir = change_direction(guard_dir)
    guard_pos_log.append(guard_pos)
    # move to new position
    guard_pos = move_guard(guard_pos, guard_dir, grid)
# add final position to the list
guard_pos_log.append(guard_pos)

result = len(np.unique(np.array(guard_pos_log), axis=0))
print(f"Part 1 solution: {result}")

# Part 2


def loop_check(guard_pos, guard_dir, grid):
    guard_state_log = []
    while not off_grid_check(guard_pos, guard_dir, grid):
        if obstruction_check(guard_pos, guard_dir, grid):
            guard_dir = change_direction(guard_dir)
        else:  # only move guard once pointing in correct direction!
            guard_state = (
                f"Guard is at {guard_pos[0]+1,guard_pos[1]+1}, facing {guard_dir}"
            )
            if guard_state in guard_state_log:
                return True
            guard_state_log.append(guard_state)
            # move to new position
            guard_pos = move_guard(guard_pos, guard_dir, grid)
    return False


# generate all possible grids with an extra obstruction
grids = []
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == ".":
            new_grid = open("day6-input.txt").readlines()
            new_grid = [list(line.strip()) for line in new_grid]
            new_grid[i][j] = "#"
            grids.append(new_grid)

count = 0
for grid in tqdm(grids):
    guard_pos = [49, 39]
    guard_dir = "up"
    if loop_check(guard_pos, guard_dir, grid):
        count += 1

print(f"Part 2 solution: {count}")
