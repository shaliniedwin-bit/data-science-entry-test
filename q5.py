def check_divisibility(num, divisor):
    """
    Task 1
    - Checks if num is divisible by divisor.
    - Returns True if remainder is 0, False otherwise.
    """
    # Guard against division by zero to prevent a ZeroDivisionError
    if divisor == 0:
        return False

    return num % divisor == 0


# Task 2: Invoking the function
scenario_1 = check_divisibility(10, 2)
scenario_2 = check_divisibility(7, 3)

print(f"Is 10 divisible by 2? {scenario_1}")
print(f"Is 7 divisible by 3? {scenario_2}")