def transform(legacy_data:dict):
    new_data = dict()
    for (score, items) in legacy_data.items():
        lower = "".join(items)
        lower = lower.lower()
        lower_list = list(lower)
        data = dict.fromkeys(lower_list, score)
        new_data.update(data)
    return new_data





diction = dict()
new_dict = transform({1:['A', 'B', 'C', 'D'], 2:['D', 'G']})
print(new_dict)