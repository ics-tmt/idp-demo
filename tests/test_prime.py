import pytest
from prime import is_prime


@pytest.mark.parametrize(
    "n, expected",
    [
        (2, True),
        (3, True),
        (4, False),
        (17, True),
        (18, False),
        (1, False),
        (0, False),
        (-5, False),
    ],
)
def test_is_prime(n, expected):
    assert is_prime(n) is expected