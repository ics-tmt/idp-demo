#!/usr/bin/env python3
"""
Python script to find the maximum (best) of two numbers.
"""
import argparse


def best_of_two(a, b):
    """
    Return the larger of two numbers.
    """
    return a if a >= b else b


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Find the maximum (best) of two numbers."
    )
    parser.add_argument("a", type=float, help="First number")
    parser.add_argument("b", type=float, help="Second number")
    args = parser.parse_args()

    result = best_of_two(args.a, args.b)
    print(f"The best (maximum) of {args.a} and {args.b} is {result}")