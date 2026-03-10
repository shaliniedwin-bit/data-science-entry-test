def string_reverse(s):
    """
    Task 1
    - Reverses a given string (s) using slicing.
    - Returns the reversed string.
    """
    # Syntax: string[start:stop:step]
    # A step of -1 tells Python to move backwards through the string
    return s[::-1]

# Task 2: Invoking the function
scenario_1 = string_reverse("Hello World")
scenario_2 = string_reverse("Python")

print(f"Scenario 1: {scenario_1}")
print(f"Scenario 2: {scenario_2}")