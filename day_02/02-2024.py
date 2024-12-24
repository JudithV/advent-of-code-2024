def count_safe_reports(reports):
    safe = 0
    unsafe_diff = False
    for report in reports:   
        sorted_levels = sorted(report)
        sorted_desc_levels = sorted(report, reverse=True)
        if sorted_levels == report or sorted_desc_levels == report:   
            for i in range(len(report)-1):
                if abs(report[i] - report[i+1]) > 3 or abs(report[i]-report[i+1]) < 1:
                    unsafe_diff = True 
            if not unsafe_diff:
                safe += 1
            unsafe_diff = False
    return safe

def levels_from_file(fileName: str):
    reports = []
    input = open(fileName, 'r')
    for line in input:
        reports.append(list(map(int, line.split())))
    return reports

if __name__ == '__main__':
    reports = levels_from_file('day_02/input.txt')
    safe_reports = count_safe_reports(reports)
    print('The total amount of safe reports is: ', safe_reports)