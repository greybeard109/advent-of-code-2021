'''
Day 3: Binary Diagnostic
URL  : https://adventofcode.com/2021/day/3
'''
from aocd.models import Puzzle


class Diagnostic:

    def __init__(self, input_data):

        self.input_data  = input_data
        self.input_width = len(input_data[0])
        self.bit_strings = [''] * self.input_width 
        self.gamma_bits   = ''
        self.epsilon_bits = ''

        self.gamma_epsilon_bits()


    def gamma_epsilon_bits(self):
        '''
        gamma   - most common bit in position
        epsilon - least common bit in position
        return  - gamma and epsilon bit strings 
        '''

        for entry in self.input_data:
            for i in range(self.input_width):
                self.bit_strings[i] += entry[i] 

        for bit_string in self.bit_strings:
            gamma   = max(set(bit_string), key=bit_string.count)
            self.gamma_bits += gamma

            epsilon = '0' if (gamma == '1') else '1'
            self.epsilon_bits += epsilon


    def get_o2_bit(self, input_data, offset):
        '''
        Can't rely on gamma value because of extra check needed
        '''

        count = [0,0]

        for item in input_data:
            if item[offset] == '0':
                count[0] += 1
            else:
                count[1] += 1

        if count[0] == count[1] or count[1] > count[0]:
            return '1'
        else:
            return '0'


    def get_co2_bit(self, input_data, offset):
        '''
        Can't rely on epsilon value because of extra check needed
        '''

        count = [0,0]

        for item in input_data:
            if item[offset] == '0':
                count[0] += 1
            else:
                count[1] += 1

        if count[0] == count[1] or count[0] < count[1]:
            return '0'
        else:
            return '1'


    def oxygen_rating(self, ratings_list, offset):

        match_list = []

        if len(ratings_list) == 1:
            return ratings_list[0]

        else:
            match_bit = self.get_o2_bit(ratings_list, offset)
            for item in ratings_list:
                if item in match_list:
                    continue
                elif item[offset] == match_bit:
                    match_list.append(item)

            return self.oxygen_rating(match_list, offset + 1)


    def co2_rating(self, ratings_list, offset):

        match_list = []

        if len(ratings_list) == 1:
            return ratings_list[0]

        else:
            match_bit = self.get_co2_bit(ratings_list, offset)
            for item in ratings_list:
                if item in match_list:
                    continue
                elif item[offset] == match_bit:
                    match_list.append(item)

            return self.co2_rating(match_list, offset + 1)


    def part_1(self):
        return  int(self.gamma_bits, 2) * int(self.epsilon_bits, 2)


    def part_2(self):
        oxygen = self.oxygen_rating(self.input_data, 0)
        co2 = self.co2_rating(self.input_data, 0)
        return int(oxygen,2) * int(co2, 2)


def get_input_data():
    puzzle = Puzzle(year=2021, day=3)
    return [bin_num for bin_num in puzzle.input_data.split("\n")]


def test():
    input_data = ['00100', '11110', '10110', '10111', 
                  '10101', '01111', '00111', '11100', 
                  '10000', '11001', '00010', '01010'] 

    try:
        diag = Diagnostic(input_data)

        result_1 = diag.part_1()
        assert(result_1 == 198), f'Test 1: expected 198, got {result_1}'

        result_2 = diag.part_2()
        assert(result_2 == 230), f'Test 2: expected 230, got {result_2}'

    except AssertionError as err:
        print(err)
        return False

    else:
        return True


def solve():
    input_data = get_input_data()

    diag = Diagnostic(input_data)

    solution_1 = diag.part_1()
    solution_2 = diag.part_2()
    print(f'Part 1: {solution_1}\nPart 2: {solution_2}')


if __name__ == '__main__':
    if test():
        solve()
