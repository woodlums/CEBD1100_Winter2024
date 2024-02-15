# Index
# Value

province_list = [["ON", "Ontario"], ["BC", "British Columbia"], ["MN", "Manitoba"], ["QC", "Quebec"]]

province_dict = {"ON": "Ontario", "BC": "British Columbia", "MN": "Manitoba", "QC": "Quebec"}

customer_file = [[1, "Brendan", "QC", 1, 2, 3]]

# How to find values, list vs. dictionary.

check_value = "QC"
province_name = ""

# LIST
# for x in province_list:
#     if x[0] == check_value:
#         province_name = x[1]
#         break

# DICTIONARY
province_name = province_dict[check_value]

# province_name2 = province_dict["XX"]
province_name2 = province_dict.get("XX", None)

if province_name2 == None:
    print("Value not found")

print(province_name2)
