#!/usr/bin/env python3

def operate(num1, num2, operator):
    if operator == 'add':
        return num1 + num2
    elif operator == 'subtract':
        return num1 - num2
    elif operator == 'multiply':
        return num1 * num2
    else:
        return 'Error: function operator can be "add", "subtract", or "multiply"'
