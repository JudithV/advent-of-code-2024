def count_safe_reports(reports):
    safe = 0
    report_start = True
    unsafe_diff = False
    previous_level = 0
    for report in reports:      
        sorted_levels = sorted(report)
        sorted_desc_levels = sorted(report, reverse=True)
        if sorted_levels == report or sorted_desc_levels == report:
            for level in report:
                if report_start:
                    report_start = False
                else:
                    if abs(level - previous_level) > 3 or abs(level-previous_level) < 1:
                        unsafe_diff = True        
                previous_level = level
            if not unsafe_diff:
                safe += 1
        report_start = True
        unsafe_diff = False
    return safe

def levels_from_file(fileName: str):
    reports = []
    input = open(fileName, 'r')
    for line in input:
        levels_str = line.split()
        levels = list(map(int, levels_str))
        reports.append(levels)
    return reports

if __name__ == '__main__':
    reports = levels_from_file('day_02/input.txt')
    safe_reports = count_safe_reports(reports)
    print('The total amount of safe reports is: ', safe_reports)