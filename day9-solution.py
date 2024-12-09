# import the puzzle input file
line = open("day9-input.txt").readlines()
line = list(line[0].strip())

# extract the file sizes and free space sizes
file_sizes = line[::2]
free_space_sizes = line[1::2]
file_names = [str(i) for i in range(len(file_sizes))]

# create a list to represent the disk
file_index = 0
free_space_index = 0
disk = []
for i in range(len(line)):
    if i % 2 == 0:
        disk.extend([file_names[file_index]] * int(file_sizes[file_index]))
        file_index += 1
    else:
        disk.extend(["."] * int(free_space_sizes[free_space_index]))
        free_space_index += 1

# compute the total number of free blocks and occupied blocks
total_free_blocks = "".join(disk).count(".")
total_disk_blocks = len(disk)

# once the disk is compacted, this will be the index of the first free block
expected_free_block_index = total_disk_blocks - "".join(disk).count(".")

while disk[expected_free_block_index] != ".":
    # find last value in the disk that isn't free
    for block in disk[::-1]:
        if block != ".":
            block_id = block
            block_index = len(disk) - (disk[::-1].index(block) + 1)
            break

    # find first free space in the disk
    for block in disk:
        if block == ".":
            free_index = disk.index(block)
            break

    # move the block to the free space
    disk[free_index] = block_id
    disk[block_index] = "."

# compute the checksum
checksum = 0
for i in range(len(disk)):
    if disk[i] != ".":
        checksum += i * int(disk[i])

print(checksum)
