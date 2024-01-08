def sum_of_digits(number):
    """
    Calculates the sum of digits of a given number.
    """
    # Convert the number to a string to iterate through its digits
    number_str = str(number)
    
    # Sum the individual digits
    digit_sum = sum(int(digit) for digit in number_str)
    
    return digit_sum

def is_palindrome(number):
    """
    Returns True if the given number is a palindrome, False otherwise.
    """
    # Convert the number to a string for easy comparison
    number_str = str(number)
    
    # Check if the string is equal to its reverse
    return number_str == number_str[::-1]



