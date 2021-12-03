from aocd.models import Puzzle

def get_data():
    puzzle = Puzzle(year=2021, day=1)
    return [int(x) for x in puzzle.input_data.split()]


def part1(data):
    '''
    Count the number of times a depth measurement increases from the 
    previous measurement.
    '''
    count = 0
    for x,y in zip(data[:],data[1:]):
        if y > x: 
            count += 1

    return count


def part2(data):
    '''
    1. Break data into three-measurement sliding windows
    2. Sum each group of measurements
    3. Count the number of times an increase occurs
    '''

    totals = []
    for x,y,z in zip(data[:],data[1:],data[2:]):
        totals.append(x+y+z)

    return part1(totals)


def test():
    input_data = [199,200,208,210,200,207,240,269,260,263]

    try:
        assert(part1(input_data) == 7), f'expected 7 got {t1}'
        assert(part2(input_data) == 5), f'expected 5 got {t1}'
    except AssertionError as err:
        print(err)


def solve():
    input_data = get_data()
    solution1 = part1(input_data)
    solution2 = part2(input_data)

    return solution1, solution2


if __name__ == '__main__':
    # test()

    solutions = solve()
    print('\n'.join([str(solution) for solution in solutions]))
