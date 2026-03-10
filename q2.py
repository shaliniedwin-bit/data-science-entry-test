def find_and_replace(lst, find_val, replace_val):
    """
    Task 1
    - Searches for all occurrences of find_val and replaces them with replace_val.
    """
    # We use a range-based loop to modify the list in-place via index
    for i in range(len(lst)):
        if lst[i] == find_val:
            lst[i] = replace_val
    return lst

# Task 2: Invoking the function
scenario_1 = find_and_replace([1, 2, 3, 4, 2, 2], 2, 5)
scenario_2 = find_and_replace(["apple", "banana", "apple"], "apple", "orange")

print(f"Scenario 1: {scenario_1}")
print(f"Scenario 2: {scenario_2}")