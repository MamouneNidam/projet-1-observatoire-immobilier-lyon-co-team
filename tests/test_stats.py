import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from analysis.stats import mean, median


def test_mean_basic():
    assert mean([1, 2, 3, 4, 5]) == 3.0


def test_mean_two_elements():
    assert mean([10, 20]) == 15.0


def test_mean_single():
    assert mean([7]) == 7.0


def test_median_odd():
    assert median([1, 2, 3, 4, 5]) == 3


def test_median_even():
    assert median([1, 2, 3, 4]) == 2.5


def test_median_unsorted():
    assert median([5, 1, 3]) == 3


def test_median_single():
    assert median([42]) == 42
