import re

def get_lines_file(fileName: str):
    lines = []
    line = []
    input = open(fileName, 'r')
    for l in input:
        for i in range(len(l)):
            line.append(l[i])
        lines.append(line)
        line = []
    return lines


def count_xmas(lines_matrix, word, directions):
    rows = len(lines_matrix)
    columns = len(lines_matrix[0])
    sum = 0
    found_word = True
    for row in range(rows):
        for column in range(columns):
            for direction_x, direction_y in directions:
                for i in range(4):
                    r, c = row + i * direction_x, column + i * direction_y
                    if r < 0 or c < 0 or r >= rows or c >= columns or lines_matrix[r][c] != word[i]:
                        found_word = False
                if found_word:
                    sum += 1
                found_word = True
    return sum

if __name__ == '__main__':
    lines = get_lines_file('day_04/input.txt')
    # All the possible directions the word can be found
    directions = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
        (1, 1),
        (1, -1),
        (-1, 1),
        (-1, -1)
    ]
    val = count_xmas(lines, "XMAS", directions)
    print('Total amount of XMAS found in input: ', val)
