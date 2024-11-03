#!/usr/bin/python3
def matrix_divided(grid, divisor):
    """
    Creates new matrix with all elements divided by divisor.
    Args:
        grid: input matrix (list of lists containing numbers)
        divisor: value to divide by
    Returns:
        New matrix with divided values
    Raises:
        TypeError: For invalid input types
        ZeroDivisionError: When divisor is 0
    """
    error_msgs = {
        'matrix': "matrix must be a matrix (list of lists) of integers/floats",
        'size': "Each row of the matrix must have the same size",
        'div': "div must be a number"
    }

    # Validate divisor
    if not isinstance(divisor, (int, float)):
        raise TypeError(error_msgs['div'])
    if divisor == 0:
        raise ZeroDivisionError("division by zero")

    # Validate matrix structure
    if not isinstance(grid, list) or not grid or \
       not all(isinstance(row, list) for row in grid):
        raise TypeError(error_msgs['matrix'])

    # Validate row lengths
    expected_length = len(grid[0])
    if not all(len(row) == expected_length for row in grid):
        raise TypeError(error_msgs['size'])

    # Validate all elements are numbers
    for row in grid:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(error_msgs['matrix'])

    # Create new matrix with divided values
    return [
        [round(element / divisor, 2) for element in row]
        for row in grid
    ]
