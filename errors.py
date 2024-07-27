#!/usr/bin/env python3

def divide(num1,num2):
    """
    Define a division operation inside a function (using def) but to get an error, define the denominator as 0. So, type except statement properly.
    """
    try:
        return print(f'{num1} / {num2} = {num1/num2}')
    except:
        return print(f'{num1} / {num2} = error, division by zero')

    
def catch_undefined():
    """
    It is possible to get multiple errors after the execution of one try block. So, please define an error-exception issue with NameError.
    """
    try:
        print(num)
    except NameError as ne:
        print(f'Caught a NameError (no assignment to num specified): {ne}')   
          
        
def catch_value_error(num):
    """
    Please define a function and with this function, generate a ValueError exception simply by entering a string instead of numerical value.
    """
    try:
        result = int(num) + 10
        print(f'Result after num converstion {num} to integer of {num} + 10: {result}')
    except ValueError as ve:
        print(f"Caught ValueError '{num}' (not correct datatype): {ve}")


def circumference(dia='12'):
    """
    Write a function called circumference that takes the diameter of a circle as input and produces the circumference of the circle. Your function should use try...except to check for a type error in the event a string is passed.
    """
    try:
        result = 3.1415 * dia
    except TypeError as te:
        print(f'Caught TypeError (not correct datatype): {te}')
        dia_ = float(dia)
        result = 3.1415 * dia_
        print(f'Updated dia to float: {type(dia_)}\nResult: {result}')
        
    
if __name__ == "__main__":
    divide(1,3)
    divide(1,0)
    catch_undefined()
    catch_value_error('15')
    catch_value_error('abc')
    circumference()
    