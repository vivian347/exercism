def is_armstrong_number(number):
    '''
    :param number: int - number to check
    :return: bool - True if number is an Armstrong number, False otherwise
    '''
    
    digits = len(str(number))
    return sum([int(digit) ** digits for digit in str(number)]) == number

