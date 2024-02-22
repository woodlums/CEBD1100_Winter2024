def split_str_int(input_list: list):
    list_of_str = []
    list_of_int = []
    for x in input_list:
        if isinstance(x, str):
            list_of_str.append(x)
        if isinstance(x, int):
            list_of_int.append(x)

    return {"strings": list_of_str, "integers": list_of_int}
