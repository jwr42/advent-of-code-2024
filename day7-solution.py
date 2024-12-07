from itertools import product
from tqdm import tqdm

# read in the data as a list of strings
calibrations = open("day7-input.txt").readlines()

# removes the newline character
calibrations = [calibration.strip() for calibration in calibrations]


def split_calibration(calibration):
    """
    Split the lines in the input file into a int test value, and a list of ints numbers
    """
    result = calibration.split(": ")
    test_value = int(result[0])
    numbers = result[1].split(" ")
    numbers = [int(number) for number in numbers]
    return test_value, numbers


def check_calibration(test_value, numbers, combinations):
    """
    Check if the has a valid solution
    """
    for combination in combinations:
        total = numbers[0]
        for i in range(len(combination)):
            if combination[i] == "+":
                total += numbers[i + 1]
            elif combination[i] == "*":
                total *= numbers[i + 1]
        if total == test_value:
            return True
    return False


# sums the test values together if there is a valid solution
calibration_sum = 0
for calibration in tqdm(calibrations):
    test_value, numbers = split_calibration(calibration)
    operators = ["+", "*"]
    spaces = len(numbers) - 1
    combinations = list(product(operators, repeat=spaces))
    if check_calibration(test_value, numbers, combinations):
        calibration_sum += test_value

print(f"Part 1 solution: {calibration_sum}")

# Part 2


def new_check_calibration(test_value, numbers, combinations):
    """
    Check if the has a valid solution with +, *, or ||
    """
    for combination in combinations:
        total = numbers[0]
        for i in range(len(combination)):
            if combination[i] == "+":
                total += numbers[i + 1]
            elif combination[i] == "*":
                total *= numbers[i + 1]
            elif combination[i] == "||":
                total = int(str(total) + str(numbers[i + 1]))
        if total == test_value:
            return True
    return False


# sums the test values together if there is a valid solution
new_calibration_sum = 0
for calibration in tqdm(calibrations):
    test_value, numbers = split_calibration(calibration)
    operators = ["+", "*", "||"]
    spaces = len(numbers) - 1
    combinations = list(product(operators, repeat=spaces))
    if new_check_calibration(test_value, numbers, combinations):
        new_calibration_sum += test_value

print(f"Part 2 solution: {new_calibration_sum}")
