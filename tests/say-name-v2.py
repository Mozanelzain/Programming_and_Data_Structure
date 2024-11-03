#!/usr/bin/python3
def say_my_name(given_name, family_name=""):
    """
    Displays a formatted string with the provided names.
    Args:
        given_name: person's first name
        family_name: person's last name (optional)
    Raises:
        TypeError: If either name is not a string
    """
    def validate_string(name, param_name):
        """Helper function to validate string parameters"""
        if not isinstance(name, str):
            raise TypeError(f"{param_name} must be a string")

    validate_string(given_name, "first_name")
    validate_string(family_name, "last_name")
    
    formatted_name = f"My name is {given_name} {family_name}"
    print(formatted_name)
