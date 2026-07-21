import os
import json


def read_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)


def write_json(file_path, data):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)


def ensure_directory_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def flatten_list(nested_list):
    return [item for sublist in nested_list for item in sublist]


def generate_unique_id(prefix='id_'):
    import uuid
    return f'{prefix}{uuid.uuid4()}'