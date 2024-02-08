my_list = [5, 3, 7, 1, 12, 22, 1, 2]

max_val = my_list[0]

for x in my_list[1:]:
    if x > max_val:
        max_val = x

print(max_val)

