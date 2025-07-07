#!/usr/bin/env python3
"""
Python script to check if a number is prime.
"""

import argparse
from math import isqrt

def is_prime(n: int) -> bool:
    """
    Return True if n is a prime number, False otherwise.
    """
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    for i in range(3, isqrt(n) + 1, 2):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check if a number is prime.")
    parser.add_argument("n", type=int, help="Number to check.")
    args = parser.parse_args()
    result = is_prime(args.n)
    print(f"{args.n} is {'a prime' if result else 'not a prime'} number.")