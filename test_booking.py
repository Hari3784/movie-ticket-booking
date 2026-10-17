import pytest
from booking import calculate_total


def test_total_price():
    assert calculate_total(150, 2) == 300


def test_single_ticket():
    assert calculate_total(150, 1) == 150


def test_invalid_tickets():
    with pytest.raises(ValueError):
        calculate_total(150, 0)
        