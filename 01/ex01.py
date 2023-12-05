import re
from typing import List

spelled_out_map = {
    v: str(idx)
    for idx, v in enumerate(["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"], 1)
}
spelled_out_re = f"(?:{'|'.join(spelled_out_map.keys())})"

cal_extract_ex01 = re.compile(r'(\d).*(\d)|(\d)')
cal_extract_ex02 = re.compile(f"(\d|{spelled_out_re}).*(\d|{spelled_out_re})|(\d|{spelled_out_re})")


def obtain_calibrations(lines: List[str], regex: re.Pattern) -> int:
    for calibration in lines:
        d1, d2, ds = map(lambda v: spelled_out_map.get(v, v), regex.search(calibration).groups())
        yield int(ds + ds) if ds else int(d1 + d2)


if __name__ == '__main__':
    with open('data/input', 'r') as f:
        print(f'Solution 01: {sum(obtain_calibrations(f.readlines(), cal_extract_ex01))}')

    with open('data/input', 'r') as f:
        print(f'Solution 02: {sum(obtain_calibrations(f.readlines(), cal_extract_ex02))}')
