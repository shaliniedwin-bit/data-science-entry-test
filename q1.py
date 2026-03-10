def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """
    # Check if both inputs are numeric (int or float)
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        return -1

    # Swapping using only x and y via tuple unpacking
    x, y = y, x

    print(f"Swapped values: x = {x}, y = {y}")


# Task 2
# Invoke the function "swap" using the following scenarios:

# Scenario 1: "Apple", 10
result1 = swap("Apple", 10)
if result1 == -1:
    print(f"Scenario 1 result: {result1} (Non-numeric input)")

# Scenario 2: 9, 17
swap(9, 17)
