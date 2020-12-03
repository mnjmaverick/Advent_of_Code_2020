# Part 1
input = open("Day_2/input.txt", "r")
total = 0
for line in input:
    line = line.split()
    low, high = map(int,line[0].split('-'))
    sign = line[1][0]
    password = line[2]
    if low <= password.count(sign) <= high: total+=1
print(total)

# Part 2
input = open("Day_2/input.txt", "r")
total = 0
for line in input:
    line = line.split()
    pos1, pos2 = map(int,line[0].split('-'))
    sign = line[1][0]
    password = line[2]
    if (password[pos1-1] == sign) != (password[pos2-1] == sign):total+=1
print(total)