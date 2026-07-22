import json


def read_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def write_json(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def merge_dicts(*dicts):
    result = {}
    for d in dicts:
        result.update(d)
    return result


def flatten_list(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list


def filter_dict(data, keys):
    return {k: data[k] for k in keys if k in data}
