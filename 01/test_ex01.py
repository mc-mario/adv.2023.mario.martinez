import pytest
from ex01 import obtain_calibrations, cal_extract_ex01, cal_extract_ex02


@pytest.mark.parametrize('test_input,expected', [
    ("a1b1", 11),
    ("1abc2", 12),
    ("a1b2c3d4e5f", 15)
])
def test_ex01_finds_two_digits(test_input, expected):
    assert expected == next(obtain_calibrations([test_input], cal_extract_ex01))


@pytest.mark.parametrize('test_input,expected', [
    ("a1", 11),
    ("treb7uchet", 77),
])
def test_ex01_finds_one_digit(test_input, expected):
    assert expected == next(obtain_calibrations([test_input], cal_extract_ex01))


@pytest.mark.parametrize('test_input,expected', [
    ("a1b1", 11),
    ("oneabc2", 12),
    ("a1b2c3d4e5f", 15)
])
def test_ex02_finds_two_digits(test_input, expected):
    assert expected == next(obtain_calibrations([test_input], cal_extract_ex02))


@pytest.mark.parametrize('test_input,expected', [
    ("aone", 11),
    ("trebsevenuchet", 77),
    ("eighthree", 83)
])
def test_ex02_finds_one_digit(test_input, expected):
    assert expected == next(obtain_calibrations([test_input], cal_extract_ex02))


@pytest.mark.parametrize('test_input,expected', [
    ("eightwoxxxeightwo", 82),
    ("oneightxxoneight", 18),
])
def test_ex02_alun_thomas_question(test_input, expected):
    assert expected == next(obtain_calibrations([test_input], cal_extract_ex02))
