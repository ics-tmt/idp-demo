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

if __name__ == '__main__':
    print('Add: ', add(1, 2))
    print('Subtract: ', subtract(4, 2))
    print('Multiply: ', multiply(3, 3))
    print('Divide: ', divide(10, 2))
