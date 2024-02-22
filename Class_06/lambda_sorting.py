ids0 = ['id1', 'id2', 'id30', 'id3', 'id22', 'id100']

ids1 = [1, 2, 30, 3, 22, 100]

print(sorted(ids0))

sorted_ids = sorted(ids0, key=lambda n: int(n[2:]))

print(sorted_ids)

