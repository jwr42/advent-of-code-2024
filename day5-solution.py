lines = open("day5-input.txt").readlines()


def rules_check(update, rules):
    follows_rules = True
    for rule in rules:
        rule_val1 = rule[0]
        rule_val2 = rule[1]
        if rule_val1 in update and rule_val2 in update:
            rule_val1_pos = update.index(rule_val1)
            rule_val2_pos = update.index(rule_val2)
            if rule_val1_pos > rule_val2_pos:
                follows_rules = False
    return follows_rules


def reorder_update(update, rules):
    for rule in rules:
        rule_val1 = rule[0]
        rule_val2 = rule[1]
        if rule_val1 in update and rule_val2 in update:
            rule_val1_pos = update.index(rule_val1)
            rule_val2_pos = update.index(rule_val2)
            if rule_val1_pos > rule_val2_pos:
                rule_val1 = update.pop(rule_val1_pos)
                update.insert(rule_val2_pos, rule_val1)
    return update


def sum_middle_index_values(updates):
    middle_index_values = []
    for i in range(len(updates)):
        middle_index = int(len(updates[i]) / 2)
        middle_index_values.append(updates[i][middle_index])
    return sum(middle_index_values)


# Part 1

# remove newline character from each line
lines = [line.strip() for line in lines]

# extract the rules and updates into lists of lists of ints
rules = [[int(_) for _ in rule.split("|")] for rule in lines[0:1176]]
updates = [[int(_) for _ in update.split(",")] for update in lines[1177:]]

# split the updates into valid and invalid
valid_updates = []
invalid_updates = []

for update in updates:
    if rules_check(update, rules):
        valid_updates.append(update)
    else:
        invalid_updates.append(update)

print(f"Total valid updates: {len(valid_updates)}")
print(f"Sum of their middle indices: {sum_middle_index_values(valid_updates)}")


# Part 2

print(invalid_updates[:2])

new_updates = []
for update in invalid_updates:
    while not rules_check(update, rules):
        update = reorder_update(update, rules)
    new_updates.append(update)

print(f"Total new updates: {len(new_updates)}")
print(f"Sum of their middle indices: {sum_middle_index_values(new_updates)}")
