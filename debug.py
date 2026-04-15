# Question: python code with a bug
def clean_database(record_ids):
    # Requirement: Remove all odd numbers from the list
    for record_id in record_ids:
        if record_id % 2 != 0:
            record_ids.remove(record_id) 

    return record_ids


# Test Case
data = [1, 3, 4, 6, 7, 9, 10]
cleaned = clean_database(data)

print(f"Final List: {cleaned}")
# EXPECTED: [4, 6, 10]
# ACTUAL:   [3, 4, 6, 9, 10]



# Task 2
# 1. The Observation:
#    This is a logic bug on the line record_ids.remove(record_id). The first skipped value happens after removing the element at iterator value 1.
#    Using the original list:[1, 3, 4, 6, 7, 9, 10].The loop sees 1 first and removes it.
#    The list becomes:[3, 4, 6, 7, 9, 10]
#    But the loop then moves to the next position, so 3 is skipped.That is the first number the logic should have caught but missed.

# 2. The Why:
#    When you remove an item from a list while moving forward, all remaining items shift one position to the left and take on a new index.
#    The pointer of the loop still moves forward to the next index, so it jumps past the element that shifted into the current spot(new first index).
#    That makes the iterator "blind" to the next element.

# 3. The Fix:
# Fix A: Modify the original list by looping backward.

def clean_database(record_ids):
    # Requirement: Remove all odd numbers from the list
    for record_id in reversed(record_ids): # Looping backward allows the program to safely remove items without affecting the indices of the remaining items that we have yet to check.
        if record_id % 2 != 0:
            record_ids.remove(record_id)

    return record_ids


# Test Case
data = [1, 3, 4, 6, 7, 9, 10]
cleaned = clean_database(data)

print(f"Final List: {cleaned}")
# EXPECTED: [4, 6, 10]
# ACTUAL:   [4, 6, 10]

# Fix B: Create a new list with only valid values (immutable approach).

def clean_database(record_ids):
    # Requirement: Remove all odd numbers from the list
    for record_id in record_ids:
        if record_id % 2 != 0:
            record_ids.remove(record_id)
# This line creates a new list that includes only the even numbers from the original list.
# effectively filtering out the odd numbers without modifying the original list during iteration.
    return [record_id for record_id in record_ids if record_id % 2 == 0] 
# Test Case
data = [1, 3, 4, 6, 7, 9, 10]
cleaned = clean_database(data)

print(f"Final List: {cleaned}")
# EXPECTED: [4, 6, 10]
# ACTUAL:   [4, 6, 10]