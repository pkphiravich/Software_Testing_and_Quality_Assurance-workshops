import pytest
from binarysearch import binary_search



def test_bi1():
    assert binary_search([1,2,3,4,5], 3) == 2


def test_bi2():
    assert binary_search([1,2,3,4,5], 1) == 0


def test_bi3():
    assert binary_search([1,2,3,4,5], 5) == 4


def test_bi4():
    assert binary_search([1,2,3,4,5], 10) == -1


def test_bi5():
    assert binary_search([], 1) == -1


def test_bi6():
    assert binary_search([1,2,3,4,5,6], 0) == -1
