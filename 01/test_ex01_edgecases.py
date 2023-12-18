import pytest
from ex01_edgecases import obtain_calibrations, cal_extract_ex02

@pytest.mark.parametrize('test_input,expected', [
    ("threeight", 38),
    ("oneight", 18),
])
def test_ex02_finds_two_digits_edgecases(test_input, expected):
    assert expected == next(obtain_calibrations([test_input], cal_extract_ex02))

@pytest.mark.parametrize('test_input,expected', [
    ("aone", 11),
    ("trebsevenuchet", 77),
])
def test_ex02_finds_one_digit(test_input, expected):
    assert expected == next(obtain_calibrations([test_input], cal_extract_ex02))