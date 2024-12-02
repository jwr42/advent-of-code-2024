# day 1 solution

lines = open("day1-input.txt").readlines()
list1, list2 = map(list, zip(*[line.split() for line in lines]))

list1.sort()
list2.sort()

diff = [abs(int(list1[i]) - int(list2[i])) for i in range(len(list1))]
print(f"Puzzle 1 solution: {sum(diff):,}")

similarity = [int(i) * int(list2.count(i)) for i in list1]
print(f"Puzzle 2 solution: {sum(similarity):,}")
