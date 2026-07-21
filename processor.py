from typing import List, Dict


def process_data(data: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """
    Process a list of dictionaries by transforming some of their values.

    Args:
        data (List[Dict[str, str]]): A list of dictionaries to be processed.

    Returns:
        List[Dict[str, str]]: A new list of dictionaries with processed values.
    """
    result = []
    for item in data:
        transformed_item = {key: value.upper() if isinstance(value, str) else value
                             for key, value in item.items()}
        result.append(transformed_item)
    return result


def filter_data(data: List[Dict[str, str]], key: str, value: str) -> List[Dict[str, str]]:
    """
    Filter the list of dictionaries based on a key-value pair.

    Args:
        data (List[Dict[str, str]]): A list of dictionaries to filter.
        key (str): The key to filter by.
        value (str): The value to match against.

    Returns:
        List[Dict[str, str]]: A new list containing filtered dictionaries.
    """
    return [item for item in data if item.get(key) == value]
