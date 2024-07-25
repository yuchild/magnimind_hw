#!/usr/bin/env python3

def prime(number):
    """
    A prime number is an integer greater than one that is only divisible by one and itself. Write a function that determines whether or not its parameter is prime, returning True if it is, and False otherwise. Write a main program that reads an integer from the user and displays a message indicating whether or not it is prime.
    """
    if (type(number) != int) or (number <= 1):
        return f'{number} is not prime'
    elif number == 2:
        return f'{number} is a prime number'
    elif (number % 2 == 0) and (number != 2):
        return f'{number} is not a prime number'
    for n in range(3,number//2):
        if number % n == 0:
            return f'{number} is not a prime number'
    return f'{number} is a prime number'


def celsius_to_romer(temp_c):
    """
    Write a function, celsius_to_romer that takes a temperature in degrees Celsius and returns the equivalent temperature in degrees Romer
    
    """
    return (80-0)/(100-0)*(temp_c - 0) - 0


def pixelart(wall_size, pixel_size):
    """
    Your function should take two arguments: the size of the wall in millimeters and the size of a pixel in millimeters. It should return True if you can fit an exact number of pixels on the wall, otherwise it should return False. For example is_divisible(4050, 27) should return True, but is_divisible(4066, 27) should return False.
    """
    return wall_size % pixel_size == 0

if __name__ == "__main__":
    print(f'Sample Prime Function of 101: {prime(101)}')
    print(f'Sample Celsius to Romer of 24 {celsius_to_romer(24)}')
    print(f'Sample pixelart of 4050 by 27: {pixelart(4050,27)}')