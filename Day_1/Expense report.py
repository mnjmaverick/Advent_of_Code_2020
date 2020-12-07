# Finding 2 or 3 numbers that sum up to 2020 within the input. Changing the number of combinations from 2 to 3 will give the answer to part 2
from itertools import combinations
from math import prod

with open('Day_1/input.txt', 'r') as f:
    data = f.read().splitlines()
    
print(next(prod(x) for x in combinations([int(x) for x in data], 2) if sum(x) == 2020))