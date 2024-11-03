#!/usr/bin/python3
def add_integer(num1, num2=98):
    """
    Performs addition of two numbers after converting them to integers.
    Args:
        num1: first operand
        num2: second operand, defaults to 98
    Returns:
        Integer sum of num1 and num2
    Raises:
        TypeError: If inputs aren't numeric
    """
    for val, param_name in [(num1, 'a'), (num2, 'b')]:
        if not any(isinstance(val, allowed_type) for allowed_type in [int, float]):
            raise TypeError(f"{param_name} must be an integer")
            
    result = int(num1) + int(num2)
    return result
