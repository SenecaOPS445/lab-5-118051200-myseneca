#!/usr/bin/env python3
# Author ID: 118051200

def add(number1, number2):
    try:
        # Attempt to convert both inputs to integers
        number1 = int(number1)
        number2 = int(number2)
        return number1 + number2
    except (ValueError, TypeError):
        return 'error: could not add numbers'

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.readlines()
    except Exception:
        return 'error: could not read file'

if __name__ == '__main__':
    print(add(10, 5))                        # works
    print(add('10', 5))                      # works
    print(add('abc', 5))                     # exception
    print(read_file('seneca2.txt'))          # works if file exists
    print(read_file('file10000.txt'))        # exception if file doesn't exist

