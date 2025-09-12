#!/usr/bin/python3
"""
This module provides a function to divide all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div using try/except for error handling.

    Args:
        matrix (list of lists of int/float): The matrix to divide.
        div (int/float): The divisor.

    Returns:
        list of lists of float: New matrix with elements divided by div.

    Raises:
        TypeError: If matrix elements are not all int/float, 
                   or rows are not of the same size,
                   or div is not a number.
        ZeroDivisionError: If div is 0.
    """
    try:
        # Check that matrix is a list of lists
        for row in matrix:
            for num in row:
                num + 0  # will raise TypeError if num is not int/float
    except TypeError:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    except Exception:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    try:
        row_length = len(matrix[0])
        for row in matrix:
            if len(row) != row_length:
                raise TypeError("Each row of the matrix must have the same size")
    except Exception:
        raise TypeError("Each row of the matrix must have the same size")

    try:
        result = [[round(num / div, 2) for num in row] for row in matrix]
    except ZeroDivisionError:
        raise ZeroDivisionError("division by zero")
    except TypeError:
        raise TypeError("div must be a number")

    return result
