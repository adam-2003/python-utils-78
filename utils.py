import json

def safe_divide(numerator, denominator):
    if not isinstance(numerator, (int, float)):
        raise ValueError('Numerator must be a number.')
    if not isinstance(denominator, (int, float)):
        raise ValueError('Denominator must be a number.')
    if denominator == 0:
        raise ZeroDivisionError('Denominator cannot be zero.')
    return numerator / denominator


def read_json_file(filepath):
    try:
        with open(filepath, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError('File not found. Invalid filepath.')
    except json.JSONDecodeError:
        raise ValueError('Invalid JSON format in file.')


def write_json_file(filepath, data):
    if not isinstance(data, dict):
        raise ValueError('Data must be a dictionary.')
    try:
        with open(filepath, 'w') as file:
            json.dump(data, file)
    except IOError as e:
        raise IOError(f'Error writing to file: {e}')