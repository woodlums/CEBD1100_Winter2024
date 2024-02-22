my_list = [234, 12, 222, 121, 123, 125]

print(list(filter (lambda x : x > 200, my_list)))

print(list(filter(lambda x: x % 2 == 0, my_list)))

province_dict = {"ON": "Ontario", "BC": "British Columbia", "MN": "Manitoba", "QC": "Quebec"}


#print(list(province_dict.items()))

#print(type(province_dict.items()))


print(dict(filter(lambda x: x[0] == "BC" or x[0] == "QC", list(province_dict.items()))))


sequences = [1,2,3,10,20]
mapped_result = map(lambda x: x*x, sequences)
print(list(mapped_result))


seq = ["1", "2", "3", "4"]

converted1 = [int(x) for x in seq]
converted2 = list(map(lambda x: int(x), seq))

print(converted1, converted2)
