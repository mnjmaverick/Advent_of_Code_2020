from math import prod

with open('Day_3/input.txt', 'r') as f:
    mat = [[i == '#' for i in line] for line in f.read().splitlines()]


def solve(mat, dx, dy):
    return sum(line[dx * (i + 1) % len(line)] for i, line in enumerate(mat[dy::dy]))


# Part 1
print(solve(mat, 3, 1))

# Part 2
moves = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
print(prod(solve(mat, * i) for i in moves))
