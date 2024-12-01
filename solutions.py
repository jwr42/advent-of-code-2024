import numpy as np

# # day 1 puzzles

# data = np.loadtxt("day1-input.txt")

# # puzzle 1
# list1 = np.sort(data[:, 0])
# list2 = np.sort(data[:, 1])
# sorted = np.column_stack((list1, list2))
# print(np.sum(np.abs(np.diff(sorted))))

# # puzzle 2
# print(np.sum([i * np.sum(np.where(list2 == i, 1, 0)) for i in list1]))

# day 1 puzzles without numpy

lines = open("day1-input.txt").readlines()
list1, list2 = map(list, zip(*[line.split() for line in lines]))

list1.sort()
list2.sort()

diff = [abs(int(list1[i]) - int(list2[i])) for i in range(len(list1))]
print(f"Puzzle 1 solution: {sum(diff):,}")

similarity = [int(i) * int(list2.count(i)) for i in list1]
print(f"Puzzle 2 solution: {sum(similarity):,}")
