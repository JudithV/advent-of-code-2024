import re

def get_lines_file(fileName: str):
    with open(fileName) as f:
        return f.read()

def get_sum_line(line):
    sum = 0
    find_full = r"(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\))"
    mul = True
    full_coincidences = re.findall(find_full, line)
    for text, x, y in full_coincidences:
        if "don't()" in text:
            mul = False
        if "do()" in text:
            mul = True
        else:
            if mul:
                sum += (int(x) * int(y))
    return sum

if __name__ == '__main__':
    text = get_lines_file('day_03/input.txt')
    val = get_sum_line(text)
    print('The total value after the multiplications is ', val)