# Sets in Python

# A set is an unordered collection of unique elements.
# Sets are mutable, but their elements must be immutable (e.g., numbers, strings, tuples).

# Creating a set
my_set = {1, 2, 3, 4}
print("Set:", my_set)

# Creating a set from a list (duplicates are removed)
my_list = [1, 2, 2, 3, 4, 4]
set_from_list = set(my_list)
print("Set from list:", set_from_list)

# Adding elements
my_set.add(5)
print("After adding 5:", my_set)

# Removing elements
my_set.remove(2)  # Raises KeyError if 2 is not present
print("After removing 2:", my_set)

# Discarding elements (no error if not present)
my_set.discard(10)
print("After discarding 10 (not present):", my_set)

# Set operations
a = {1, 2, 3}
b = {3, 4, 5}

print("Union:", a | b)         # {1, 2, 3, 4, 5}
print("Intersection:", a & b)  # {3}
print("Difference:", a - b)    # {1, 2}
print("Symmetric Difference:", a ^ b)  # {1, 2, 4, 5}

# Membership test
print(1 in a)  # True
print(4 in a)  # False

# Iterating over a set
for item in a:
    print(item)