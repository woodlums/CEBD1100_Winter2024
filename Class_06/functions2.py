def generate_list(*args, sort=False):
    if sort:
        return sorted(list(args))
    else:
        return list(args)


print(generate_list(1, 10, 6, 8, 2))

print(generate_list(1, 10, 6, 8, 2, sort=True))

