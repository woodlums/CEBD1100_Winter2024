def printsomething():
    print("Hello")
    # None is returned.

def increase_value(n):
    n = n + 1
    return n

def create_salutation(first, last, salutation = "M"):
    return f"Hello, {salutation}. {first} {last}!"

def get_highest_value(input_list):
    return max(input_list)

def get_max(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        return n1
    if n2 > n3:
        return n2
    return n3

def add3nums(n1=0, n2=0, n3=0):
    return sum([n1, n2, n3])

print(increase_value(9))
print(create_salutation("Brendan", "Wood"))

print(get_highest_value([1,2,3]))


print(add3nums(2, n2=3))


def describe_pet(pet_name, animal_type='dog'):
    return pet_name + animal_type

