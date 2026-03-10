def find_first_negative(lst):
    """
    Task 1
    - Finds the first negative number using a while loop.
    """
    i = 0
    # Loop as long as 'i' is within the list boundaries
    while i < len(lst):
        if lst[i] < 0:
            return lst[i]  # Return immediately when found
        i += 1  # Move to the next index

    return "No negatives"


# Task 2: Invoking the function
scenario_1 = find_first_negative([3, 5, -1, 7, -2, 8])
scenario_2 = find_first_negative([2, 10, 7, 0])

print(f"Result 1: {scenario_1}")
print(f"Result 2: {scenario_2}")
