import numpy as np

# day 1 puzzles

data = np.loadtxt("day1-input.txt")

# puzzle 1
list1 = np.sort(data[:, 0])
list2 = np.sort(data[:, 1])
sorted = np.column_stack((list1, list2))
print(np.sum(np.abs(np.diff(sorted))))

# puzzle 2
print(np.sum([i * np.sum(np.where(list2 == i, 1, 0)) for i in list1]))

# day 1 puzzles without numpy

f = open(
    "day1-input.txt",
    "r",
)
lines = f.readlines()

list1 = [int(line.split()[0]) for line in lines]
list2 = [int(line.split()[1]) for line in lines]

list1.sort()
list2.sort()

diff = [abs(list1[i] - list2[i]) for i in range(len(list1))]

print(sum(diff))

similarity = [i * list2.count(i) for i in list1]

print(sum(similarity))
