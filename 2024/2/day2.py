import re
import sys
import numpy as np


def main(file: str):
    reports = get_reports(file)
    report_diffs = [np.diff(report) for report in reports]
    safe_reports = [is_safe(report) for report in report_diffs]
    safe_report_total = np.count_nonzero(safe_reports)
    print("Part 1: ", safe_report_total)

    damp_safe = [dampener(report) for report in reports]
    damp_safe_total = np.count_nonzero(damp_safe)
    print("Part 2: ", damp_safe_total)


def dampener(reports: np.array) -> bool:
    for i in range(len(reports)):
        new_rep = np.delete(reports, i)
        new_diffs = np.diff(new_rep)
        if is_safe(new_diffs):
            return True
    return False


def is_safe(rep_diff: np.array) -> bool:
    increasing = all(rep_diff > 0)
    decreasing = all(rep_diff < 0)
    monotone = increasing or decreasing

    abs_diff = abs(rep_diff)
    over = all(abs_diff <= 3)
    under = all(abs_diff >= 1)
    in_range = over and under

    return monotone and in_range


def get_reports(file: str) -> list[np.array]:
    reports = []
    with open(file) as file_str:
        lines = file_str.readlines()
        for line in lines:
            report = np.array([int(num) for num in re.findall(r'\d+', line)])
            reports.append(report)
    return reports


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        main('sample.txt')
    else:
        main('input.txt')
