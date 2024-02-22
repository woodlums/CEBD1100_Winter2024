from functools import reduce

def debugprint(x, y):
    print(f"x={x}, y={y}")
    return x + y

sequences = [1, 2, 3, 4, 5]
answer = reduce(lambda x, y: debugprint(x, y), sequences, 20)
print(answer)

