with open('Day_6/input.txt', 'r') as f:
    data = [list(map(set, group.splitlines())) for group in f.read().split('\n\n')]

yes = 0
yes_all = 0
for group in data:
    yes += len(set.union(*group))
    yes_all += len(set.intersection(*group))

# Part 1
print(yes)

# Part 2
print(yes_all)