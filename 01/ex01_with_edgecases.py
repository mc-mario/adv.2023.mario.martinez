"""
    After submitting the exercise and talking with other teammates
    I noticed that my solution actually would fail against some edge cases
    like 'oneight' -> 18
    My submitted answer gave back 11
    It worked __fine__ because the input of the exercise don't contain those specific lines
    To fix it,
    the only change needed is to add edge_cases to the spelled_out_map and include the according regex.

    I added it as separate exercise since original implementation is more concise and ~cool~ :)
"""

import re
from typing import List

spelled_out_map = {
    v: str(idx)
    for idx, v in enumerate(["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"], 1)
}
spelled_out_re = f"(?:{'|'.join(spelled_out_map.keys())})"
edge_cases = {
    'oneight': '18',
    'twone': '21',
    'threeight': '38',
    'fiveight': '58',
    'sevenine': '79',
    'eightwo': '82',
    'eighthree': '83',
    'nineight': '98',
}
spelled_out_map = {**spelled_out_map, **edge_cases}
edge_cases_re = f"(?:{'|'.join(edge_cases.keys())})"

cal_extract_ex01 = re.compile(r'(\d).*(\d)|(\d)')
cal_extract_ex02 = re.compile(f"(\d|{spelled_out_re}).*(\d|{spelled_out_re})|(\d|{edge_cases_re}|{spelled_out_re})")
print(cal_extract_ex02)
def obtain_calibrations(lines: List[str], regex: re.Pattern) -> int:
    edge_cases_set = set(edge_cases.values())
    for calibration in lines:
        d1, d2, ds = map(lambda v: spelled_out_map.get(v, v), regex.search(calibration).groups())
        if ds in edge_cases_set:
            yield int(ds)
        yield int(ds + ds) if ds else int(d1 + d2)


if __name__ == '__main__':
    with open('data/input', 'r') as f:
        print(f'Solution 01: {sum(obtain_calibrations(f.readlines(), cal_extract_ex01))}')

    with open('data/input', 'r') as f:
        print(f'Solution 02: {sum(obtain_calibrations(f.readlines(), cal_extract_ex02))}')
