from tools.col import myzip  
from tools.numbers.comp import sum_of_digits,is_palindrome
from tools.numbers.simp import add_numbers,subtract_numbers

class FunctionCallError(Exception):
    """
    Custom exception for invalid function call order.
    """
    pass



def sum_of_digits(number):
    """
    Calculates the sum of digits of a given number.
    """
    if not getattr(test_functions, 'function_called', False):
        raise FunctionCallError("Call add_numbers or subtract_numbers first")
    number_str = str(number)
    digit_sum = sum(int(digit) for digit in number_str)
    return digit_sum

def is_palindrome(number):
    """
    Returns True if the given number is a palindrome, False otherwise.
    """
    if not getattr(test_functions, 'function_called', False):
        raise FunctionCallError("Call add_numbers or subtract_numbers first")
    number_str = str(number)
    return number_str == number_str[::-1]



def test_functions():
    # Set the flag to indicate that at least one function has been called
    test_functions.function_called = True
    
    # Test add_numbers and subtract_numbers functions
    result_addition = add_numbers(5, 3)
    result_subtraction = subtract_numbers(8, 2)
    print("Addition result:", result_addition)
    print("Subtraction result:", result_subtraction)

    # Test sum_of_digits function
    number_to_sum = 234
    result_sum = sum_of_digits(number_to_sum)
    print(f"Sum of digits for {number_to_sum} is: {result_sum}")

    # Test is_palindrome function
    number_palindrome = 121
    result_palindrome = is_palindrome(number_palindrome)
    print(f"{number_palindrome} is a palindrome: {result_palindrome}")

    # Test myzip function
    list1 = [1, 2, 3, 4]
    list2 = ['a', 'b', 'c', 'd']
    result_zip = list(myzip(list1, list2))
    print(f"myzip result: {result_zip}")

# Run the test
test_functions()
