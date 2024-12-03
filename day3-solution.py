import re

# Puzzle 1 - find the valid multiplication instructions

# reading the data and converting to a single strign to simplify analysis
memory = open("day3-input.txt").readlines()
memory_string = "".join(memory).replace("\n", "")


def get_total(txt):
    """
    Given a string of text, find the sum of all mul instructions contained in the text e.g. mul(234,456)
    """
    # find the mul instructions e.g. mul(234,456)
    search_results = re.findall(r"mul\([0-9]+,[0-9]+\)", txt)

    # lists the search results e.g. ['234','456']
    listed_results = [
        re.search(r"[0-9]+,[0-9]+", _).group().split(",") for _ in search_results
    ]
    # multiply the search results together e.g. 106704
    multipled_results = [
        int(listed_result[0]) * int(listed_result[1])
        for listed_result in listed_results
    ]
    return sum(multipled_results)


print(f"Puzzle 1 solution: {get_total(memory_string)}")


# Puzzle 2 - find the valid multiplication instructions using the do() and don't() conditional statements

# find the sections of the string when the code is not valid (i.e. after a don't() statement)
sections = memory_string.split("don't()")

# find the sections when the code is valid again (i.e. after a do() statement)
valid_string = sections[0]  # account for the first section
for section in sections:
    # note: section.split("do()")[0] is a string between don't() and do()
    active_sections = section.split("do()")[1:]
    valid_string += "".join(active_sections)

print(f"Puzzle 2 solution: {get_total(valid_string)}")
