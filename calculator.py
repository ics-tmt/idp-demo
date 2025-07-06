# Python Calculator Script

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError('Cannot divide by zero')
    return x / y

def is_even(n):
    """Return True if n is an even integer, False otherwise."""
    return n % 2 == 0

if __name__ == '__main__':
    print('Add: ', add(1, 2))
    print('Subtract: ', subtract(4, 2))
    print('Multiply: ', multiply(3, 3))
    print('Divide: ', divide(10, 2))

    try:
        num = int(input("Enter a number to check evenness: "))
        print(f"{num} is {'even' if is_even(num) else 'odd'}.")
    except ValueError:
        print("Invalid input; please enter an integer.")
