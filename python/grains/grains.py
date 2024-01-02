def square(number):
    '''
    :param number: int - the number of the square on the chessboard
    :return: int - the number of grains on the square
    '''

    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    
    return 2 ** (number - 1)


def total():
    '''
    :return: int - the total number of grains on the chessboard
    '''

    return sum([square(i) for i in range(1, 65)])
