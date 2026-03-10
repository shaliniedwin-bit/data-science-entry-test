def update_dictionary(dct, key, value):
    """
    Task 1
    - Updates a dictionary with a new key-value pair.
    - If key exists, prints original value before updating.
    """
    if key in dct:
        print(f"Original value for '{key}': {dct[key]}")

    # Updating or adding the key-value pair
    dct[key] = value
    return dct


# Task 2: Invoking the function
scenario_1 = update_dictionary({}, "name", "Alice")
scenario_2 = update_dictionary({"age": 25}, "age", 26)

print(f"Result 1: {scenario_1}")
print(f"Result 2: {scenario_2}")