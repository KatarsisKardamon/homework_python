import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
    ('a', 'A'),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
    ("Auto", "Auto"),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize('input_str, expected', [
    (' cup', 'cup'),
    (' cup cup', 'cup cup')
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize('input_str, expected', [
    ('cup', 'cup'),
    (' ', '')
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize('input_str, input_symbol, expected', [
    ('Hope', 'o', True),
    ('No cow', ' ', True),
])
def test_contains_positive(input_str, input_symbol, expected):
    assert string_utils.contains(input_str, input_symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize('input_str, input_symbol, expected', [
    ('', '', True),
    ('Mall', 'v', False),
])
def test_contains_negative(input_str, input_symbol, expected):
    assert string_utils.contains(input_str, input_symbol) == expected


@pytest.mark.positive
@pytest.mark.parametrize('input_str, input_symbol, expected', [
    ('Cat', 'a', 'Ct'),
    ('Small dog', 'd', 'Small og'),
])
def test_delete_symbol_positive(input_str, input_symbol, expected):
    assert string_utils.delete_symbol(input_str, input_symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize('input_str, input_symbol, expected', [
    ('Cat', 'f', 'Cat'),
    ('Small dog', '', 'Small dog'),
])
def test_delete_symbol_negative(input_str, input_symbol, expected):
    assert string_utils.delete_symbol(input_str, input_symbol) == expected
