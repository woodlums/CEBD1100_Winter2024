import re

input = "J4T 1T1"

result = re.search("^[A-Z][0-9][A-Z] [0-9][A-Z][0-9]$", input, True)

print(result)

