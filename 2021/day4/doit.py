#!/usr/bin/python3

import re

with open('input.txt', 'r') as f:
    alldata = f.readlines()
    f.close()

def part1(data):
    # Read in called called numbers and boards:
    called_numbers = []
    board = []
    boards = []
    for line in data:
        if not called_numbers:
            called_numbers = list(map(int, line.strip().split(',')))
        elif not line.strip():
            if board:
                boards.append(board)
            board = []
        else:
            board.append(list(map(int, line.strip().replace('  ', ' ').split(' '))))

    for called_number in called_numbers:
        # Mark all instances of called_number as zeroes:
        for board_idx in range(len(boards)):
            for row in range(len(boards[board_idx])):
                for col in range(len(boards[board_idx][row])):
                    if boards[board_idx][row][col] == called_number:
                        boards[board_idx][row][col] = 0

        # Check if any boards are winning:
        for board_idx in range(len(boards)):
            row_totals = [0, 0, 0, 0, 0]
            col_totals = [0, 0, 0, 0, 0]
            for row in range(len(boards[board_idx])):
                for col in range(len(boards[board_idx][row])):
                    col_totals[col] += boards[board_idx][row][col]
                row_totals[row] = sum(boards[board_idx][row])
            if 0 in row_totals or 0 in col_totals:
                #print('WINNER: called_number: ', called_number, ', board: ', boards[board_idx])
                board_sum = sum(map(sum, boards[board_idx]))
                return board_sum * called_number

def part2(data):
    # Read in called called numbers and boards:
    called_numbers = []
    board = []
    boards = []
    for line in data:
        if not called_numbers:
            called_numbers = list(map(int, line.strip().split(',')))
        elif not line.strip():
            if board:
                boards.append(board)
            board = []
        else:
            board.append(list(map(int, line.strip().replace('  ', ' ').split(' '))))

    winning_boards = [False] * len(boards)
    for called_number in called_numbers:
        # Mark all instances of called_number as zeroes:
        for board_idx in range(len(boards)):
            for row in range(len(boards[board_idx])):
                for col in range(len(boards[board_idx][row])):
                    if boards[board_idx][row][col] == called_number:
                        boards[board_idx][row][col] = 0

        # Check if any boards are winning:
        for board_idx in range(len(boards)):
            row_totals = [0, 0, 0, 0, 0]
            col_totals = [0, 0, 0, 0, 0]
            for row in range(len(boards[board_idx])):
                for col in range(len(boards[board_idx][row])):
                    col_totals[col] += boards[board_idx][row][col]
                row_totals[row] = sum(boards[board_idx][row])
            if 0 in row_totals or 0 in col_totals:
                #print('WINNER: called_number: ', called_number, ', board: ', boards[board_idx])
                winning_boards[board_idx] = True
                if False not in winning_boards:
                    board_sum = sum(map(sum, boards[board_idx]))
                    return board_sum * called_number

print(part1(alldata))
print(part2(alldata))