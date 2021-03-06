#!/usr/bin/env python3

"""
a template for the series assignment
"""

#Fibonacci function, calls "sum_series" with the initial values 0 and 1 (default), returns nth value
def fibonacci(n):
    """ compute the nth Fibonacci number """
    return sum_series(n)
    
    pass

#Lucas function, calls "sum series" with the initial values 2 and 1, returns nth value
def lucas(n):
    """ compute the nth Lucas number """
    return sum_series(n, 2, 1)

    pass


def sum_series(n, n0=0, n1=1):
    """
    compute the nth value of a summation series.

    :param n0=0: value of zeroth element in the series
    :param n1=1: value of first element in the series

    This function should generalize the fibonacci() and the lucas(),
    so that this function works for any first two numbers for a sum series.
    Once generalized that way, sum_series(n, 0, 1) should be equivalent to fibonacci(n).
    And sum_series(n, 2, 1) should be equivalent to lucas(n).

    sum_series(n, 3, 2) should generate antoehr series with no specific name

    The defaults are set to 0, 1, so if you don't pass in any values, you'll
    get the fibonacci sercies
    """
    #Creates a list with the initial values of n0 and n1
    series_list = [n0,n1]
    #iterates to the nth value
    for i in range (2, n+1):
        #Appends a value at the end of the list as a function of the two previous values
        series_list.append(series_list[i-2] + series_list[i-1])
    #Returns the nth value of the list    
    return series_list [n]

    pass

if __name__ == "__main__":
    # run some tests
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13

    assert lucas(0) == 2
    assert lucas(1) == 1

    assert lucas(4) == 7

    # test that sum_series matches fibonacci
    assert sum_series(5) == fibonacci(5)
    assert sum_series(7, 0, 1) == fibonacci(7)

    # test if sum_series matched lucas
    assert sum_series(5, 2, 1) == lucas(5)

    # test if sum_series works for arbitrary initial values
    assert sum_series(0, 3, 2) == 3
    assert sum_series(1, 3, 2) == 2
    assert sum_series(2, 3, 2) == 5
    assert sum_series(3, 3, 2) == 7
    assert sum_series(4, 3, 2) == 12
    assert sum_series(5, 3, 2) == 19

    print("tests passed")
