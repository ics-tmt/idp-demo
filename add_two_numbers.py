"""Simple script to add two numbers entered by the user."""

def add_two_numbers(first, second):
    """Return the sum of two numbers."""
    return first + second


def main():
    """Collect user input and print the sum."""
    first = float(input("Enter the first number: "))
    second = float(input("Enter the second number: "))
    total = add_two_numbers(first, second)
    print(f"The sum is: {total}")


if __name__ == "__main__":
    main()
