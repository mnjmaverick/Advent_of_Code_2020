with open('Day_8/input.txt', 'rt') as f:
    instructions = [l.strip().split(' ') for l in f.readlines()]

operations = {
    'acc': lambda x, acc, ip: (acc+x, ip+1),
    'jmp': lambda x, acc, ip: (acc, ip+x),
    'nop': lambda _, acc, ip: (acc, ip+1)
}


def run(instructions):
    acc = 0
    ip = 0
    previous = set()
    history = list()

    while ip >= 0 and ip < len(instructions):
        if ip in previous:
            return False, acc, ip, history
        previous.add(ip)
        i = instructions[ip]
        if i[0] in ('jmp', 'nop'):
            history.append(ip)
        (acc, ip) = operations[i[0]](int(i[1]), acc, ip)
    else:
        return True, acc, ip, history


# Part 1
err, acc, ip, history = run(instructions)
print(acc)

#Part 2
for i in history:
    ic = [[i[0], i[1]] for i in instructions]
    ic[i][0] = 'nop' if ic[i][0] == 'jmp' else 'jmp'
    err, acc, ip, _ = run(ic)
    if err is True:
        print(acc)
        break
