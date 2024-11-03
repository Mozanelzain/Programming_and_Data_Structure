#!/usr/bin/python3

def display_list_elements(input_sequence=[], element_count=0):
    """
    Safely displays a specified number of elements from a sequence
    Args:
        input_sequence: The sequence of elements to display
        element_count: Number of elements to attempt to display
    Returns:
        Number of successfully displayed elements
    """
    displayed = 0
    try:
        while displayed < element_count:
            print("{}".format(input_sequence[displayed]), end="")
            displayed += 1
    except IndexError:
        pass
    finally:
        print("")
    return displayed

def calculate_total(*values):
    """
    Calculates sum of all numeric values provided
    Args:
        *values: Variable number of input values
    Returns:
        Sum of all valid numeric values
    """
    result = 0.0
    for item in values:
        try:
            result += float(item)
        except (ValueError, TypeError):
            pass
    return result

def run_test_cases():
    """Execute various test scenarios"""
    # Test sequence 1: Basic number sequence
    number_sequence = [10, 20, 30, 40, 50]
    print("\nTest 1: Basic number sequence")
    result = display_list_elements(number_sequence, 3)
    print(f"Elements displayed: {result}")

    # Test sequence 2: Mixed data types
    mixed_sequence = [100, "Python", 3.14, [1, 2], {"key": "value"}]
    print("\nTest 2: Mixed data types")
    result = display_list_elements(mixed_sequence, 5)
    print(f"Elements displayed: {result}")

    # Test sequence 3: Empty sequence
    print("\nTest 3: Empty sequence")
    result = display_list_elements([], 3)
    print(f"Elements displayed: {result}")

    # Test sequence 4: Boundary testing
    single_element = [999]
    print("\nTest 4: Boundary testing")
    result = display_list_elements(single_element, 5)
    print(f"Elements displayed: {result}")

    # Test sequence 5: Number summation
    print("\nTest 5: Number summation")
    sum_result = calculate_total(10, 20, "30", "invalid", 40.5)
    print(f"Sum of valid numbers: {sum_result}")

    # Test sequence 6: Complex mixed calculations
    print("\nTest 6: Complex mixed calculations")
    complex_sum = calculate_total(
        "123.5",
        "invalid",
        [1, 2, 3],
        456,
        "789",
        {"key": "value"},
        0.5
    )
    print(f"Complex sum result: {complex_sum}")

if __name__ == "__main__":
    run_test_cases()