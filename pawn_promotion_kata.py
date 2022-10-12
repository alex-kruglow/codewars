#!/usr/bin/env python3

##########################################################
# 6 kyu Pawn Promotion                                   #
# https://www.codewars.com/kata/62652939385ccf0030cb537a #
# Author: Alexey Kruglov <alexkruglow@gmail.com>         #
##########################################################


def get_unique_items(array: list[str]) -> list[str]:
    '''Return unique items in the list.'''
    result: list[str] = []
    for i in array:
        if i not in result:
            result.append(i)
    return result


def get_diagonal_variants(position: str) -> list[str]:
    '''Return list of diagonal variants.'''
    result: list[str] = []
    x: int = int(position[0])
    y: int = int(position[1])
    xx: int
    yy: int
    directions = [
        [1, 1],
        [1, -1],
        [-1, 1],
        [-1, -1],
    ]
    for d in directions:
        xx, yy = x, y
        while True:
            xx += d[0]
            yy += d[1]
            if xx < 0 or xx > 7 or yy < 0 or yy > 7:
                break
            result.append(f'{xx}{yy}')
    return result


def get_line_variants(position: str) -> list[str]:
    '''Return list of horizontal and vertical variants.'''
    result: list[str] = []
    x: int = int(position[0])
    y: int = int(position[1])
    line_list = list(range(8))
    for xx in line_list:
        result.append(f'{xx}{y}')
    for yy in line_list:
        result.append(f'{x}{yy}')
    return result


def get_queen_variants(position: str) -> list[str]:
    '''Return all variants for Queen chessman.'''
    result: list = []
    result = get_diagonal_variants(position) + get_line_variants(position)
    result = get_unique_items(result)
    return result


def get_rook_variants(position: str) -> list[str]:
    '''Return all variants for Rook chessman.'''
    result: list = []
    result = get_line_variants(position)
    return result


def get_knight_variants(position: str) -> list[str]:
    '''Return all variants for Knight chessman.'''
    result: list = []
    x = int(position[0])
    y = int(position[1])
    variants = [
        {'x': x + 2, 'y': y + 1},
        {'x': x - 2, 'y': y + 1},
        {'x': x + 2, 'y': y - 1},
        {'x': x - 2, 'y': y - 1},
        {'x': x + 1, 'y': y + 2},
        {'x': x - 1, 'y': y + 2},
        {'x': x + 1, 'y': y - 2},
        {'x': x - 1, 'y': y - 2},

    ]
    for variant in variants:
        if variant['x'] < 8 and variant['y'] < 8:
            result.append(f'{variant["x"]}{variant["y"]}')
    return result


def get_bishop_variants(position: str) -> list[str]:
    '''Return all variants for Bishop chessman.'''
    result: list = []
    result = get_diagonal_variants(position)
    return result


def get_position_of_figure(board: list[list], figure: str) -> str:
    '''Return position for a chessman.'''
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] == figure:
                return f'{x}{y}'
    return ''


def get_king_position(board: list[list]) -> str:
    '''Return King position on the board.'''
    return get_position_of_figure(board, 'K')


def get_pawn_position(board: list[list]) -> str:
    '''Return Pawn position on the board.'''
    return get_position_of_figure(board, 'P')


def promotion(board: list[list]) -> list:
    '''Return all chessmen which can be attach the king.'''
    result: list = []
    pawn_position = get_pawn_position(board)
    print(f'Pawn pos: {pawn_position}')
    king_position = get_king_position(board)
    print(f'King pos: {king_position}')
    if pawn_position == '' or king_position == '':
        return []
    if king_position in get_rook_variants(pawn_position):
        result.append('rook')
    if king_position in get_queen_variants(pawn_position):
        result.append('queen')
    if king_position in get_bishop_variants(pawn_position):
        result.append('bishop')
    if king_position in get_knight_variants(pawn_position):
        result.append('knight')
    return result


def main():
    tests = [
        [
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', 'K', ' '],
            [' ', ' ', ' ', ' ', 'P', ' ', ' ', ' '],
        ],
        [
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['P', ' ', ' ', 'K', ' ', ' ', ' ', ' '],
        ],
        [
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', 'K', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', 'P', ' ', ' ', ' ', ' ', ' '],
        ],
        [
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', 'K', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', 'P', ' ', ' ', ' ', ' ', ' ']
          ]
    ]
    for test in tests:
        result = promotion(test)
        print(result)


if __name__ == '__main__':
    main()
