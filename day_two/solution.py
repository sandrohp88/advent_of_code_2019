
# part 1


def int_code(noun: int, verb: int, data: [int])-> int:
    data[1] = noun
    data[2] = verb
    for i in range(0, len(data), 4):
        op_code = data[i]
        if op_code == 99:
            return data[0]
        # unpack values(4) into local variables
        op_code, first_position, second_position, result_position = data[i:i + 4]
        result = data[first_position] + \
            data[second_position] if op_code == 1 else data[first_position] * \
            data[second_position]
        data[result_position] = result
    return data[0]

# part 1


def part1(data):
    print(f'part1: {int_code(12,2,data[:])}')

# part 2


def part2(data):
    for noun in range(100):
        for verb in range(100):
                result = int_code(noun,verb,data[:])
                if result == 19690720:
                    print(f'part2: {100 * noun + verb}')
                    return 0

# load data
with open('input.txt', 'rt') as file_input:
    data = [int(number) for number in file_input.read().split(',')]
    part1(data)
    part2(data)
