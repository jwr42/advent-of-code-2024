# data for today's puzzles
reports = open("day2-input.txt").readlines()

# Puzzle 1 - count total number of safe reports

safe_reports = 0


def get_gradual_increase_and_decrease(report):
    """
    Returns the number of gradual increases and decreases
    """

    gradual_increases = 0
    gradual_decreases = 0

    for i in range(len(report) - 1):
        if report[i + 1] > report[i] and report[i + 1] <= report[i] + 3:
            gradual_increases += 1
        elif report[i + 1] < report[i] and report[i + 1] >= report[i] - 3:
            gradual_decreases += 1

    return gradual_increases, gradual_decreases


for report in reports:
    report = report.split()  # list of strings e.g. ['43', '44', '47', '48', '50']
    report = [int(_) for _ in report]  # list of ints e.g. [43, 44, 47, 48, 50]

    gradual_increases, gradual_decreases = get_gradual_increase_and_decrease(report)

    if gradual_increases == len(report) - 1 or gradual_decreases == len(report) - 1:
        safe_reports += 1

print(safe_reports)

# Puzzle 2 - count total number of safe reports with Problem Dampener

safe_reports = 0

for report in reports:
    report = report.split()  # list of strings e.g. ['43', '44', '47', '48', '50']
    report = [int(_) for _ in report]  # list of ints e.g. [43, 44, 47, 48, 50]

    safe_permutation = 0
    for i in range(len(report)):
        new_report = report.copy()
        new_report.pop(i)
        gradual_increases, gradual_decreases = get_gradual_increase_and_decrease(
            new_report
        )
        if (
            gradual_increases == len(new_report) - 1
            or gradual_decreases == len(new_report) - 1
        ):
            safe_permutation += 1

    if safe_permutation > 0:
        safe_reports += 1

print(safe_reports)
