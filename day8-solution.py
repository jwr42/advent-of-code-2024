from itertools import combinations


lines = open("day8-input.txt").readlines()
map = [list(line.strip()) for line in lines]


def get_antenna_names(map):
    antennas = []
    for i in range(len(map)):
        antennas.extend(map[i])
    antennas = [_ for _ in antennas if _ != "."]
    return set(antennas)


def get_antenna_locations(map, anteanna):
    anteanna_locations = []
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == anteanna:
                anteanna_locations.append((i, j))
    return anteanna_locations


def in_boundary(x, y):
    return 0 <= x < len(map) and 0 <= y < len(map[0])


def get_all_antenna_locations(map):
    antenna_locations = []
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] != ".":
                antenna_locations.append((i, j))
    return antenna_locations


total_antenna_locations = get_all_antenna_locations(map)

antenna_names = list(get_antenna_names(map))
total_valid_antinode_locations = []
for anteanna in antenna_names:
    antenna_locations = get_antenna_locations(map, anteanna)
    antenna_combinations = combinations(antenna_locations, 2)
    for antenna_combination in antenna_combinations:
        x1, y1 = antenna_combination[0]
        x2, y2 = antenna_combination[1]
        dx = x2 - x1
        dy = y2 - y1

        candidate_antinode_locations = [(x1 - dx, y1 - dy), (x2 + dx, y2 + dy)]

        # new check for part 2
        i = 2
        while i * dx < len(map) + 1 and i * dy < len(map[0]) + 1:
            candidate_antinode_locations.append((x1 - i * dx, y1 - i * dy))
            candidate_antinode_locations.append((x2 + i * dx, y2 + i * dy))
            i += 1

        for candidate_antinode_location in candidate_antinode_locations:
            if (
                candidate_antinode_location not in total_antenna_locations
                and in_boundary(
                    candidate_antinode_location[0], candidate_antinode_location[1]
                )
            ):
                total_valid_antinode_locations.append(candidate_antinode_location)

total_antennas = len(total_antenna_locations)
total_antinodes = len(set(total_valid_antinode_locations))

print(total_antennas + total_antinodes)

print(total_antenna_locations)
print(total_valid_antinode_locations)

for total_valid_antinode_location in total_valid_antinode_locations:
    map[total_valid_antinode_location[0]][total_valid_antinode_location[1]] = "#"

for i in range(len(map)):
    print("".join(map[i]))
