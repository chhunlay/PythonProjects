"""" Leap Year
💪 This is a difficult challenge! 💪 
Write a program that returns True or False whether if a given year is a leap year.
A normal year has 365 days, leap years have 366, with an extra day in February. 
The reason why we have leap years is really fascinating, this video does it more justice.

This is how you work out whether if a particular year is a leap year. 
- on every year that is divisible by 4 with no remainder
- except every year that is evenly divisible by 100 with no remainder 
- unless the year is also divisible by 400 with no remainder.   
"""

def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

# Example Inputs and Outputs
print(is_leap_year(2400))  # Output: True
print(is_leap_year(1989))  # Output: False
