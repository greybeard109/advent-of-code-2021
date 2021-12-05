'''
Day 4: Giant Squid
URL  : https://adventofcode.com/2021/day/4
'''
from aocd.models import Puzzle
from colorama import Fore
import numpy as np


class BingoBoard:

    def __init__(self, board_nums, board_id):
        self.id = board_id
        self.board_nums = np.array(board_nums) 
        self.marks = np.zeros((5,5),dtype=int)


    def mark(self, draw_num):
        '''
        Mark the board and keep track of the last number drawn
        '''
        self.draw_num = draw_num
        self.marks[np.where(self.board_nums == draw_num)] = 1 


    def win(self):
        '''
        Check board rows and columns for a win
        '''

        # check the rows
        for i in range(self.marks.shape[0]):
            if np.all(self.marks[i] == self.marks[i][0]) and self.marks[i][0] == 1:
                return True

        # check the columns
        marks_t = self.marks.T
        for i in range(marks_t.shape[0]):
            if np.all(marks_t[i] == marks_t[i][0]) and marks_t[i][0] == 1:
                return True

        return False


    def score(self):
        '''
        Total up all numbers that haven't been marked.
        Then multiply by the last drawn number
        '''
        unmarked = np.where(self.marks == 0)
        total = 0
        for x,y in zip(unmarked[0], unmarked[1]):
            total += self.board_nums[x][y]

        return total * self.draw_num


    def __str__(self):
        bb_str = f'{self.id}:\n'

        for x in range(5):
            for y in range(5):
                if self.marks[x][y] == 1:
                    cell = f'{self.board_nums[x][y]:2} '
                    bb_str += Fore.YELLOW + cell + Fore.RESET
                else:
                    bb_str += f'{self.board_nums[x][y]:2} '
            bb_str += '\n'

        return bb_str


def get_input_data():
    '''
    Input data is a mix of numbers to draw and random boards
    Split into separate inputs 
    Convert all data to numbers so calculations can be performed.
    '''
    puzzle = Puzzle(year=2021, day=4)

    input_data = [data for data in puzzle.input_data.split('\n\n')]

    # split data into draw numbers and boards
    draw_numbers = [int(num) for num in input_data[0].split(',')]

    boards = []
    for entry in input_data[1:]:
        nums = [int(num) for num in entry.split()]
        board = [nums[i:i+5] for i in range(0,25,5)]
        boards.append(board)

    return draw_numbers, boards


def part_1(draw_numbers, boards):
    '''
    Get the score of the first board to win
    '''
    bingo_boards = [BingoBoard(boards[i], i) for i in range(len(boards))]

    for i in range(len(draw_numbers)):
        for bb in bingo_boards:
            bb.mark(draw_numbers[i])
            if bb.win():
                return bb.score()


def part_2(draw_numbers, boards):
    '''
    Get the score of the last board to win
    '''
    board_count = len(boards)
    bingo_boards = [BingoBoard(boards[i], i) for i in range(board_count)]
    winning_boards = []

    for i in range(len(draw_numbers)):
        for bb in bingo_boards:
            if bb.id not in winning_boards:
                bb.mark(draw_numbers[i])
                if bb.win():
                    winning_boards.append(bb.id)

        if len(winning_boards) == board_count:
            break

    last = winning_boards[-1]
    return bingo_boards[last].score()


def test():
    draw_numbers = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,
                    12,22,18,20,8,19,3,26,1]
    boards = \
    [[[22,13,17,11,0],[8,2,23,4,24],[21,9,14,16,7],[6,10,3,18,5],[1,12,20,15,19]],
    [[3,15,0,2,22],[9,18,13,17,5],[19,8,7,25,23],[20,11,10,24,4],[14,21,16,12,6]],
    [[14,21,17,24,4],[10,16,15,9,19],[18,8,23,26,20],[22,11,13,6,5],[2,0,12,3,7]]]


    try:
        test_1 = part_1(draw_numbers, boards)
        assert(test_1 == 4512), f'Test 1: expected 4512 got {test_1}'

        test_2 = part_2(draw_numbers, boards)
        assert(test_2 == 1924), f'Test 2: expected 1924 got {test_2}'

    except AssertionError as err:
        print(err)
        return False

    return True


def solve():
    draw_numbers, boards = get_input_data()
    solution_1 = part_1(draw_numbers, boards)
    solution_2 = part_2(draw_numbers, boards)

    print(f'Part 1: {solution_1}')
    print(f'Part 2: {solution_2}')


if __name__ == '__main__':
    if test():
        solve()
