import json


def read_json_data(path_filename):
    with open(path_filename, 'r', encoding='utf-8') as f:
        json_data = json.load(f)
        list_data = []
        for item in json_data:
            list_data.append(tuple(item.values()))
    return list_data
