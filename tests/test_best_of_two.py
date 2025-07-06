import best_of_two


def test_a_greater_than_b():
    assert best_of_two.best_of_two(2, 1) == 2


def test_b_greater_than_a():
    assert best_of_two.best_of_two(1, 2) == 2


def test_equal():
    assert best_of_two.best_of_two(2, 2) == 2


def test_negative_numbers():
    assert best_of_two.best_of_two(-1, -2) == -1