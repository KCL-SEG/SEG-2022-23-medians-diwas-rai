"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""
def median(numbers):
    numLength = len(numbers)
    numbers.sort()
    
    if (numLength % 2 == 0):
        return (numbers[numLength // 2] + numbers[(numLength // 2) - 1]) / 2
    else:
        return numbers[numLength // 2]


while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(median(numbers))
