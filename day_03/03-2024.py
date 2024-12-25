import re

def get_lines_file(fileName: str):
    lines = []
    input = open(fileName, 'r')
    for line in input:
        lines.append(line)
    return lines

def get_sum_line(line):
    sum = 0
    find = r"mul\((\d+),(\d+)\)"
    matches = re.findall(find, line)
    for x, y in matches:
        sum += (int(x) * int(y))
    return sum

if __name__ == '__main__':
    lines = get_lines_file('day_03/input.txt')
    val = sum(get_sum_line(line) for line in lines)
    print('The total value after the multiplications is ', val)