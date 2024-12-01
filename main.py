import numpy as np

data = np.loadtxt("day1-puzzle1-input.txt")

# puzzle 1
list1 = np.sort(data[:, 0])
list2 = np.sort(data[:, 1])
sorted = np.column_stack((list1, list2))
print(np.sum(np.abs(np.diff(sorted))))

# puzzle 2
print(np.sum([i * np.sum(np.where(list2 == i, 1, 0)) for i in list1]))
