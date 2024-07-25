#!/usr/bin/env python3

def divide(num1,num2):
    """
    Define a division operation inside a function (using def) but to get an error, define the denominator as 0. So, type except statement properly.
    """
    try:
        return print(f'{num1} / {num2} = {num1/num2}')
    except:
        return print(f'{num1} / {num2} = error, division by zero')
    
    
if __name__ == "__main__":
    divide(1,3)
    divide(1,0)