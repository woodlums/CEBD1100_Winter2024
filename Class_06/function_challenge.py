# Write a function that takes in any amount of string and int values,
# and returns two lists back:  one for strings, one for ints.

import list_utilities.utils1 as lu
lists = lu.split_str_int([1,2, 3, "A", 4, "B", "c"])
print(lists["strings"])


