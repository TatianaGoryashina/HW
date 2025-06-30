import pytest
from string_utils import StringUtils


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
    ("привет", "Привет"),
    (" шмель", " Шмель"),
    ("ТАНЯ", "ТАНЯ")
])
def test_capitalize_positive(input_str, expected):
    string_utils = StringUtils()
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("!№;%", "!№;%"),
    ("   ", "   "),
    pytest.param(None, None, marks=pytest.mark.xfail)
])
def test_capitalize_negative(input_str, expected):
    string_utils = StringUtils()
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("  skypro", "skypro"),
    ("skypro  ", "skypro  "),
    (" World alone", "World alone"),
    (" d o n t ", "d o n t ")
    ])
def test_trim_positive(input_str, expected):
    string_utils = StringUtils()
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("  skypro", " skypro"),
    ("skypro  ", "skypro"),
    (" Mark 2", "Mark2")
])
def test_trim_negative(input_str, expected):
    string_utils = StringUtils()
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, search_symbol, expected", [
    ("Skypro", "S", True),
    ("Привет", "П", True),
    ("123", "1", True),
    (" ", " ", True),
    ("Skypro", "Sky", True),
    ("Привет", "Привет", True),
    ("Skypro", "U", False),
    ("Татьяна", "Ю", False),
    ("123456789", "0", False),
    ("Skypro", "1", False),
    ("Таня", "Татьяна", False)
])
def test_contains_positive(input_str, search_symbol, expected):
    string_utils = StringUtils()
    assert string_utils.contains(input_str, search_symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, search_symbol, expected", [
    ("", "a", False),
    ("abc", "", False),
    ("", "", False),
    ("abc", "а", False)
])
def test_contains_edge_cases_negative(input_str, search_symbol, expected):
    string_utils = StringUtils()
    assert string_utils.contains(input_str, search_symbol) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("skypro", "s", "kypro"),
    ("hello world", "w", "hello orld"),
    ("python", "n", "pytho"),
    ("World", "Word", "l"),
    ("Mark1", "1", "Mark"),
    ("хорошо", "о", "хрш")
])
def test_delete_positive(input_str, symbol, expected):
    string_utils = StringUtils()
    assert string_utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("", "s", ""),
    ("  ", "w", "  "),
    ("python", "", "python"),
    ("привет", "e", "привет")
])
def test_delete_negative(input_str, symbol, expected):
    string_utils = StringUtils()
    assert string_utils.delete_symbol(input_str, symbol) == expected
