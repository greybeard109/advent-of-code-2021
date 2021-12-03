'''
Day 2: Dive!
Puzzle page: https://adventofcode.com/2021/day/2

'''
from aocd.models import Puzzle


class Submarine:
    horizontal = 0
    depth = 0
    aim = 0


    def run_1(self, course):
        for command in course:
            direction, value = command.split()

            if direction == 'forward':
                self.horizontal += int(value)
            elif direction == 'down':
                self.depth += int(value)
            elif direction == 'up':
                self.depth -= int(value)

        return self.horizontal * self.depth


    def run_2(self, course):
        for command in course:
            direction, value = command.split()

            if direction == 'forward':
                self.horizontal += int(value)
                self.depth += int(value) * self.aim
            elif direction == 'down':
                self.aim += int(value)
            elif direction == 'up':
                self.aim -= int(value)


        return self.horizontal * self.depth


    def reset(self):
        self.horizontal = 0
        self.depth = 0
        self.aim = 0


def get_input_data():
    puzzle = Puzzle(year=2021, day=2)
    return [command for command in puzzle.input_data.split('\n')]


def test():
    input_data = ['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']
    sub = Submarine()

    try:
        result = sub.run_1(input_data)
        assert(result == 150), f'Case 1: expected 150, got {result}'

        sub.reset()

        result = sub.run_2(input_data)
        assert(result == 900), f'Case 2: expected 900, got {result}'

    except AssertionError as err:
        print(err)
    else:
        print('Test cases OK')


def solve():
    input_data = get_input_data()

    sub = Submarine()
    part_1 = sub.run_1(input_data)

    sub.reset()

    part_2 = sub.run_2(input_data)

    print(f'Part 1: {part_1}\nPart 2: {part_2}')


if __name__ == '__main__':
    # test()
    solve()
