lines = open("day4-input.txt").readlines()

# Puzzle 1

# exclude the last char because it's \n using a slicer [:-1]
array = [list(line)[:-1] for line in lines]

# valid coordinates for the locations of the XMAS letters
"""
Searching with a 4x4 grid of valid coordinates, then addiing the correct letters later
[O,O,O,O]
[O,O,O,O]
[O,O,O,O]
[O,O,O,O]
"""
valid_coords = [
    [(0, 0), (0, 1), (0, 2), (0, 3)],  # start top left, end top right
    [(0, 3), (0, 2), (0, 1), (0, 0)],  # reverse of the above
    [(0, 0), (1, 0), (2, 0), (3, 0)],  # start top left, end bottom left
    [(3, 0), (2, 0), (1, 0), (0, 0)],  # reverse of the above
    [(0, 0), (1, 1), (2, 2), (3, 3)],  # start top left, end bottom right
    [(3, 3), (2, 2), (1, 1), (0, 0)],  # reverse of the above
    [(0, 3), (1, 2), (2, 1), (3, 0)],  # start top right, end bottom left
    [(3, 0), (2, 1), (1, 2), (0, 3)],  # reverse of the above
    [(0, 3), (1, 3), (2, 3), (3, 3)],  # start top right, end bottom right
    [(3, 3), (2, 3), (1, 3), (0, 3)],  # reverse of the above
    [(3, 0), (3, 1), (3, 2), (3, 3)],  # start bottom left, end bottom right
    [(3, 3), (3, 2), (3, 1), (3, 0)],  # reverse of the above
]

match_coords = []

for row in range(len(array[0]) - 3):
    for col in range(len(array) - 3):
        for coords in valid_coords:
            if (
                array[row + coords[0][0]][col + coords[0][1]] == "X"
                and array[row + coords[1][0]][col + coords[1][1]] == "M"
                and array[row + coords[2][0]][col + coords[2][1]] == "A"
                and array[row + coords[3][0]][col + coords[3][1]] == "S"
            ):
                match_coords.append(
                    f"X at {row + coords[0][0]},{col + coords[0][1]} to S at {row + coords[3][0]},{col + coords[3][1]}"
                )

# remove duplicates from the list and return total matches
print(f"Part 1 total matches: {len(set(match_coords))}")

# Puzzle 2

# reset match_coords
match_coords = []

# valid coordinates for the locations of the X-MAS letters
"""
Searching with a 3x3 grid of valid coordinates, then adding the correct letters later
[O,.,O]
[.,O,.]
[O,.,O]
"""
valid_coords = [
    [(0, 0), (0, 2), (1, 1), (2, 0), (2, 2)],  # M.S .A. M.S
    [(0, 2), (2, 2), (1, 1), (0, 0), (2, 0)],  # M.M .A. S.S
    [(2, 2), (2, 0), (1, 1), (0, 2), (0, 0)],  # S.M .A. S.M
    [(2, 0), (0, 0), (1, 1), (2, 2), (0, 2)],  # S.S .A. M.M
]

for row in range(len(array[0]) - 2):
    for col in range(len(array) - 2):
        for coords in valid_coords:
            if (
                array[row + coords[0][0]][col + coords[0][1]] == "M"
                and array[row + coords[1][0]][col + coords[1][1]] == "M"
                and array[row + coords[2][0]][col + coords[2][1]] == "A"
                and array[row + coords[3][0]][col + coords[3][1]] == "S"
                and array[row + coords[4][0]][col + coords[4][1]] == "S"
            ):
                match_coords.append(
                    f"Central A at {row + coords[2][0]},{col + coords[2][1]}"
                )

# remove duplicates from the list and return total matches
print(f"Part 2 total matches: {len(set(match_coords))}")
