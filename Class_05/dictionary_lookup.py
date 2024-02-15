province_dict = {"ON": "Ontario", "BC": "British Columbia", "MN": "Manitoba", "QC": "Quebec"}

province_code = ""
search_value = "Ontario"

for pr in province_dict.items():
    if pr[1] == search_value:
        province_code = pr[0]
        break

print(province_code)

