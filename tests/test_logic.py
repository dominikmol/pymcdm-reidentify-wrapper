import pytest
import numpy as np
from logic import make_bounds, parse_bounds_from_text, get_types_from_cores

def test_make_bounds():
    data_matrix = np.array([[3, 15], [2, 7], [22, 85]])
    expected_bounds = np.array([[2, 22], [7, 85]])
    assert np.array_equal(make_bounds(data_matrix), expected_bounds)


def test_parse_bounds_from_text():
    text = "(2, 22), (7, 85), (5, 10)"
    expected_bounds = np.array([[2, 22], [7, 85], [5, 10]])
    assert np.array_equal(parse_bounds_from_text(text), expected_bounds)


@pytest.mark.parametrize("cores, bounds, expected_types", [
    ([2, 3, 4],   [[0,10],[0,20],[0,30]], [-1,-1,-1]),
    ([8, 18, 28], [[0,10],[0,20],[0,30]], [ 1, 1, 1]),
    ([2, 18, 4],  [[0,10],[0,20],[0,30]], [-1, 1,-1]),
])

def test_get_types_from_cores(cores, bounds, expected_types):
    assert np.array_equal(get_types_from_cores(cores, bounds), expected_types)